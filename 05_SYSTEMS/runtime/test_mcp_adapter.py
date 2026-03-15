"""
Tests for the MCP Adapter — validates external integration prototype.

Part of Agent Maestro v0.4.0 (Phase D — G3).

Tests the complete governance → MCP adapter → mock response pipeline.
"""

import json
import os
import sys
import tempfile
import unittest
import yaml

# Ensure sibling imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcp_adapter import MCPAdapter, MCPServerConfig, _get_mcp_adapter
from tool_interface import ToolResult


class TestMCPServerConfig(unittest.TestCase):
    """Tests for MCPServerConfig parsing."""

    def test_parse_config(self):
        data = {
            "server_id": "slack",
            "server_name": "Slack (via MCP)",
            "transport": "mock",
            "available_tools": ["send_message", "search_messages"],
            "status": "prototype",
        }
        config = MCPServerConfig(data)
        self.assertEqual(config.server_id, "slack")
        self.assertEqual(config.transport, "mock")
        self.assertEqual(len(config.available_tools), 2)
        self.assertEqual(config.status, "prototype")

    def test_defaults(self):
        config = MCPServerConfig({"server_id": "test"})
        self.assertEqual(config.transport, "stdio")
        self.assertEqual(config.available_tools, [])
        self.assertEqual(config.status, "configured")


class TestMCPAdapter(unittest.TestCase):
    """Tests for the MCP Adapter core functionality."""

    def setUp(self):
        self.vault_dir = tempfile.mkdtemp()
        runtime_dir = os.path.join(self.vault_dir, "05_SYSTEMS", "runtime")
        os.makedirs(runtime_dir, exist_ok=True)

        # Create test MCP config
        config = {
            "servers": [
                {
                    "server_id": "slack",
                    "server_name": "Slack (Mock)",
                    "transport": "mock",
                    "available_tools": ["send_message", "search_messages"],
                    "status": "prototype",
                },
                {
                    "server_id": "github",
                    "server_name": "GitHub (Mock)",
                    "transport": "mock",
                    "available_tools": ["create_issue"],
                    "status": "planned",
                },
            ]
        }
        config_path = os.path.join(runtime_dir, "mcp_servers.yaml")
        with open(config_path, 'w') as f:
            yaml.dump(config, f)

        # Create logs directory
        os.makedirs(os.path.join(self.vault_dir, "06_EXECUTION", "logs"), exist_ok=True)

        self.adapter = MCPAdapter(self.vault_dir)
        self.adapter.load_config()

    def test_load_config(self):
        self.assertEqual(len(self.adapter.servers), 2)
        self.assertIn("slack", self.adapter.servers)
        self.assertIn("github", self.adapter.servers)

    def test_list_servers(self):
        servers = self.adapter.list_servers()
        self.assertEqual(len(servers), 2)
        self.assertEqual(servers[0]["server_id"], "slack")

    def test_list_tools(self):
        tools = self.adapter.list_tools("slack")
        self.assertEqual(tools, ["send_message", "search_messages"])

    def test_list_tools_unknown_server(self):
        tools = self.adapter.list_tools("nonexistent")
        self.assertEqual(tools, [])

    def test_mock_call_slack_send_message(self):
        result = self.adapter.call_tool("slack", "send_message", {
            "channel": "#agent-maestro",
            "text": "Hello from Agent Maestro!",
        })
        self.assertTrue(result.success)
        self.assertEqual(result.data["channel"], "#agent-maestro")
        self.assertTrue(result.data["ok"])
        self.assertTrue(result.data["mock"])

    def test_mock_call_github_create_issue(self):
        result = self.adapter.call_tool("github", "create_issue", {
            "title": "Test issue",
            "body": "Created by Agent Maestro test",
        })
        self.assertTrue(result.success)
        self.assertEqual(result.data["issue_number"], 1)
        self.assertIn("html_url", result.data)

    def test_call_unknown_server(self):
        result = self.adapter.call_tool("nonexistent", "anything", {})
        self.assertFalse(result.success)
        self.assertIn("not configured", result.error)

    def test_call_unavailable_tool(self):
        result = self.adapter.call_tool("slack", "delete_channel", {})
        self.assertFalse(result.success)
        self.assertIn("not available", result.error)

    def test_call_log_recorded(self):
        self.adapter.call_tool("slack", "send_message", {"text": "test"})
        self.adapter.call_tool("github", "create_issue", {"title": "test"})

        log = self.adapter.get_call_log()
        self.assertEqual(len(log), 2)
        self.assertEqual(log[0]["server_id"], "slack")
        self.assertEqual(log[1]["server_id"], "github")
        self.assertTrue(log[0]["success"])

    def test_export_call_log(self):
        self.adapter.call_tool("slack", "send_message", {"text": "test"})
        path = self.adapter.export_call_log()

        self.assertTrue(os.path.exists(path))
        with open(path) as f:
            data = json.load(f)
        self.assertEqual(data["total_calls"], 1)

    def test_stdio_transport_returns_not_implemented(self):
        """stdio transport correctly reports not-yet-implemented."""
        # Temporarily change slack to stdio
        self.adapter.servers["slack"].transport = "stdio"
        result = self.adapter.call_tool("slack", "send_message", {"text": "test"})
        self.assertFalse(result.success)
        self.assertIn("not yet implemented", result.error)


class TestMCPGovernanceIntegration(unittest.TestCase):
    """Tests that MCP tools integrate correctly with the governance layer."""

    def setUp(self):
        self.vault_dir = tempfile.mkdtemp()
        runtime_dir = os.path.join(self.vault_dir, "05_SYSTEMS", "runtime")
        os.makedirs(runtime_dir, exist_ok=True)

        # Create MCP config
        config = {
            "servers": [{
                "server_id": "slack",
                "transport": "mock",
                "available_tools": ["send_message"],
                "status": "prototype",
            }]
        }
        with open(os.path.join(runtime_dir, "mcp_servers.yaml"), 'w') as f:
            yaml.dump(config, f)

        # Create minimal compiled authority pack
        artifacts_dir = os.path.join(
            self.vault_dir, "05_SYSTEMS", "authority_architecture",
            "compiler", "prototype", "artifacts"
        )
        os.makedirs(artifacts_dir, exist_ok=True)
        os.makedirs(os.path.join(self.vault_dir, "06_EXECUTION", "logs"), exist_ok=True)

        self.pack_path = os.path.join(artifacts_dir, "test_mcp_agent.json")
        pack = {
            "artifact_id": "TEST.mcp_agent",
            "compiled_from": {
                "pack_id": "TEST.mcp_agent",
                "pack_name": "MCP Test Agent",
                "agent_role": "specialist",
                "constellation": "test",
            },
            "governance": {
                "governed_actions": [
                    {"action": "send external message", "permission": "allowed", "conditions": ""},
                    {"action": "read registry", "permission": "allowed", "conditions": ""},
                ],
                "rules": [],
                "control_gates": [],
                "evidence_requirements": [],
                "escalation": {"escalates_to": "supervisor"},
                "failure_semantics": {"on_execution_failure": "escalate"},
            },
        }
        with open(self.pack_path, 'w') as f:
            json.dump(pack, f)

    def test_governed_mcp_call(self):
        """Full pipeline: GovernedAgent → attempt_action → MCP tool → mock response."""
        from governed_agent import GovernedAgent
        from mcp_adapter import tool_send_mcp_message

        agent = GovernedAgent(self.pack_path, self.vault_dir)

        # The execute function wraps the MCP tool call
        def execute_fn(ctx):
            result = tool_send_mcp_message(
                vault_path=self.vault_dir,
                server_name="slack",
                tool_name="send_message",
                arguments={"channel": "#test", "text": "Governed MCP call"},
            )
            return result.to_dict()

        action_result = agent.attempt_action("send external message", execute_fn)

        self.assertEqual(action_result.permission.value, "allowed")
        self.assertTrue(action_result.executed)
        self.assertIn("success", action_result.outcome)

    def test_ungoverned_mcp_call_escalates(self):
        """Agent without permission gets escalated, not executed."""
        from governed_agent import GovernedAgent

        # Create a pack WITHOUT mcp permission
        pack = {
            "artifact_id": "TEST.no_mcp",
            "compiled_from": {
                "pack_id": "TEST.no_mcp",
                "pack_name": "No MCP Agent",
                "agent_role": "specialist",
                "constellation": "test",
            },
            "governance": {
                "governed_actions": [
                    {"action": "read note", "permission": "allowed", "conditions": ""},
                ],
                "rules": [],
                "control_gates": [],
                "evidence_requirements": [],
                "escalation": {"escalates_to": "supervisor"},
                "failure_semantics": {},
            },
        }
        no_mcp_pack = os.path.join(os.path.dirname(self.pack_path), "no_mcp.json")
        with open(no_mcp_pack, 'w') as f:
            json.dump(pack, f)

        agent = GovernedAgent(no_mcp_pack, self.vault_dir)
        result = agent.attempt_action("send external message")

        self.assertEqual(result.permission.value, "requires_escalation")
        self.assertFalse(result.executed)


if __name__ == "__main__":
    unittest.main()
