"""
MCP Adapter — Model Context Protocol client for external integrations.

Part of Agent Maestro v0.4.0 Runtime Engine (Phase D — G3).

This adapter bridges the Tool Interface with external MCP servers,
enabling governed agents to interact with services like Slack, GitHub,
email, etc. through the standard governance pipeline.

Architecture:
    Tool Interface → MCP Adapter → MCP Server → External Service

The adapter:
    1. Manages MCP server configurations (from mcp_servers.yaml)
    2. Translates tool calls into MCP tool invocations
    3. Returns results as standard ToolResult objects
    4. Logs all external interactions for audit

Usage:
    adapter = MCPAdapter(vault_path)
    adapter.load_config()
    result = adapter.call_tool("slack", "send_message", {"channel": "#general", "text": "Hello"})

Note: This is a PROTOTYPE. In production, MCP communication would use the
standard MCP protocol (JSON-RPC over stdio/SSE). This prototype simulates
the adapter pattern and validates the governance integration.
"""

import json
import os
import sys
import yaml
from datetime import datetime, timezone
from typing import Any, Optional

# Ensure sibling imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tool_interface import ToolResult, register_tool, _log_state_change


class MCPServerConfig:
    """Configuration for a single MCP server connection."""

    def __init__(self, data: dict):
        self.server_id = data["server_id"]
        self.server_name = data.get("server_name", self.server_id)
        self.transport = data.get("transport", "stdio")  # stdio, sse, or mock
        self.command = data.get("command")  # For stdio transport
        self.url = data.get("url")  # For SSE transport
        self.env = data.get("env", {})  # Environment variables (tokens, etc.)
        self.available_tools = data.get("available_tools", [])
        self.status = data.get("status", "configured")  # configured, connected, error

    def to_dict(self) -> dict:
        return {
            "server_id": self.server_id,
            "server_name": self.server_name,
            "transport": self.transport,
            "available_tools": self.available_tools,
            "status": self.status,
        }


class MCPAdapter:
    """
    Model Context Protocol adapter for external service integration.

    Manages MCP server configurations and translates tool calls into
    MCP tool invocations. All calls pass through the governance layer
    before reaching this adapter.
    """

    def __init__(self, vault_path: str):
        self.vault_path = vault_path
        self.config_path = os.path.join(
            vault_path, "05_SYSTEMS", "runtime", "mcp_servers.yaml"
        )
        self.servers: dict[str, MCPServerConfig] = {}
        self.call_log: list[dict] = []

    def load_config(self) -> list[MCPServerConfig]:
        """Load MCP server configurations from mcp_servers.yaml."""
        if not os.path.exists(self.config_path):
            return []

        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}

        servers = []
        for server_data in data.get("servers", []):
            config = MCPServerConfig(server_data)
            self.servers[config.server_id] = config
            servers.append(config)

        return servers

    def list_servers(self) -> list[dict]:
        """List all configured MCP servers."""
        return [s.to_dict() for s in self.servers.values()]

    def list_tools(self, server_id: str) -> list[str]:
        """List available tools for a specific MCP server."""
        server = self.servers.get(server_id)
        if not server:
            return []
        return server.available_tools

    def call_tool(self, server_id: str, tool_name: str,
                  arguments: dict) -> ToolResult:
        """
        Call an MCP tool on a configured server.

        In production, this would use the MCP protocol (JSON-RPC over
        stdio or SSE). This prototype validates the adapter pattern
        and logs the call for governance audit.

        Args:
            server_id: The MCP server to call
            tool_name: The MCP tool name on that server
            arguments: Arguments to pass to the MCP tool

        Returns:
            ToolResult with the response data
        """
        server = self.servers.get(server_id)
        if not server:
            return ToolResult(
                f"mcp:{server_id}.{tool_name}", False,
                error=f"MCP server not configured: {server_id}"
            )

        if tool_name not in server.available_tools:
            return ToolResult(
                f"mcp:{server_id}.{tool_name}", False,
                error=f"Tool '{tool_name}' not available on server '{server_id}'. "
                      f"Available: {server.available_tools}"
            )

        # Record the call for audit
        call_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "server_id": server_id,
            "tool_name": tool_name,
            "arguments": arguments,
            "transport": server.transport,
        }

        # Route by transport type
        if server.transport == "mock":
            result = self._mock_call(server, tool_name, arguments)
        elif server.transport == "stdio":
            result = self._stdio_call(server, tool_name, arguments)
        elif server.transport == "sse":
            result = self._sse_call(server, tool_name, arguments)
        else:
            result = ToolResult(
                f"mcp:{server_id}.{tool_name}", False,
                error=f"Unknown transport: {server.transport}"
            )

        call_record["success"] = result.success
        call_record["error"] = result.error
        self.call_log.append(call_record)

        return result

    def _mock_call(self, server: MCPServerConfig, tool_name: str,
                   arguments: dict) -> ToolResult:
        """
        Mock MCP call for testing and prototyping.

        Returns a simulated successful response that matches the
        expected shape of the real MCP tool's response.
        """
        response = {
            "server_id": server.server_id,
            "tool_name": tool_name,
            "arguments_received": arguments,
            "mock": True,
            "message": f"Mock call to {server.server_id}.{tool_name} succeeded",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        # Add tool-specific mock responses
        if tool_name == "send_message" and "slack" in server.server_id:
            response["channel"] = arguments.get("channel", "unknown")
            response["message_ts"] = "mock_1234567890.123456"
            response["ok"] = True
        elif tool_name == "search_messages" and "slack" in server.server_id:
            response["messages"] = []
            response["total"] = 0
        elif tool_name == "create_issue" and "github" in server.server_id:
            response["issue_number"] = 1
            response["html_url"] = f"https://github.com/mock/repo/issues/1"

        return ToolResult(
            f"mcp:{server.server_id}.{tool_name}", True,
            data=response
        )

    def _stdio_call(self, server: MCPServerConfig, tool_name: str,
                    arguments: dict) -> ToolResult:
        """
        Call an MCP server via stdio transport.

        This would spawn the MCP server process, send a JSON-RPC request
        over stdin, and read the response from stdout. Currently returns
        a not-implemented result — to be completed when connecting to
        real MCP servers.
        """
        return ToolResult(
            f"mcp:{server.server_id}.{tool_name}", False,
            error="stdio transport not yet implemented — use mock transport for prototyping"
        )

    def _sse_call(self, server: MCPServerConfig, tool_name: str,
                  arguments: dict) -> ToolResult:
        """
        Call an MCP server via SSE (Server-Sent Events) transport.

        This would connect to the MCP server's SSE endpoint and send
        a JSON-RPC request. Currently returns a not-implemented result.
        """
        return ToolResult(
            f"mcp:{server.server_id}.{tool_name}", False,
            error="SSE transport not yet implemented — use mock transport for prototyping"
        )

    def get_call_log(self) -> list[dict]:
        """Return the audit log of all MCP calls in this session."""
        return self.call_log

    def export_call_log(self, output_path: str = None) -> str:
        """Export the call log to a JSON file for audit purposes."""
        if output_path is None:
            output_path = os.path.join(
                self.vault_path, "06_EXECUTION", "logs",
                f"mcp_call_log_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
            )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                "export_timestamp": datetime.now(timezone.utc).isoformat(),
                "total_calls": len(self.call_log),
                "calls": self.call_log,
            }, f, indent=2)
        return output_path


# ── MCP-backed Tool Registration ──────────────────────────────

# Module-level adapter instance (lazy-loaded)
_mcp_adapter: Optional[MCPAdapter] = None


def _get_mcp_adapter(vault_path: str) -> MCPAdapter:
    """Get or create the module-level MCP adapter."""
    global _mcp_adapter
    if _mcp_adapter is None:
        _mcp_adapter = MCPAdapter(vault_path)
        _mcp_adapter.load_config()
    return _mcp_adapter


@register_tool("send_mcp_message", "send external message",
                "Send a message via MCP to an external service (e.g., Slack)")
def tool_send_mcp_message(vault_path: str, server_name: str,
                          tool_name: str, arguments: dict,
                          **kwargs) -> ToolResult:
    """
    Send a message or call a tool via MCP on an external service.

    This is the governed entry point for all MCP-based external interactions.
    The agent must have "send external message" in its governed_actions.

    Args:
        vault_path: Root path of the vault
        server_name: MCP server ID (e.g., "slack", "github")
        tool_name: Tool name on the MCP server (e.g., "send_message")
        arguments: Arguments to pass to the MCP tool

    Returns:
        ToolResult with the MCP response data
    """
    adapter = _get_mcp_adapter(vault_path)
    result = adapter.call_tool(server_name, tool_name, arguments)

    # Log the external interaction as a state change
    _log_state_change(
        vault_path, "modify",
        f"06_EXECUTION/logs/mcp_interactions",
        agent_id="mcp_adapter",
        agent_role="integration",
        constellation="runtime",
        field_changed="external_call",
        after_state=f"{server_name}.{tool_name}",
        justification=f"MCP call to {server_name}.{tool_name}",
        artifact_type="external",
    )

    return result


@register_tool("list_mcp_servers", "read registry",
                "List all configured MCP servers and their available tools")
def tool_list_mcp_servers(vault_path: str, **kwargs) -> ToolResult:
    """
    List all configured MCP servers.

    Uses the "read registry" permission since this is a read-only
    operation against the MCP configuration.

    Args:
        vault_path: Root path of the vault

    Returns:
        ToolResult with server list and their available tools
    """
    adapter = _get_mcp_adapter(vault_path)
    servers = adapter.list_servers()

    return ToolResult("list_mcp_servers", True, data={
        "servers": servers,
        "count": len(servers),
    })
