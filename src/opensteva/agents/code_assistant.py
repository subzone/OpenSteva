"""CodeAssistantAgent — specialized agent for coding tasks.

Wraps the NativeReActAgent with a code-oriented system prompt and
pre-configured tool set for file operations, shell execution, and git.
"""

from __future__ import annotations

from opensteva.agents.native_react import NativeReActAgent
from opensteva.core.registry import AgentRegistry

CODE_SYSTEM_PROMPT = """\
You are Steva, a local-first AI code assistant. You help developers write,
debug, refactor, and understand code.

For each step, respond with exactly one of:

1. To think and act:
Thought: <your reasoning>
Action: <tool_name>
Action Input: <json arguments>

2. To give a final answer:
Thought: <your reasoning>
Final Answer: <your answer>

CODING PRINCIPLES:
- Read existing code before modifying it
- Match project style and conventions
- Write minimal, correct implementations
- Verify changes compile/pass tests when possible
- Explain root causes when debugging

{tool_descriptions}"""


@AgentRegistry.register("code_assistant")
class CodeAssistantAgent(NativeReActAgent):
    """Code-focused ReAct agent with file, shell, and git tools."""

    agent_id = "code_assistant"
    default_tools = [
        "file_read",
        "file_write",
        "shell_exec",
        "code_interpreter",
        "git_tool",
        "apply_patch",
        "web_search",
        "think",
    ]

    @classmethod
    def system_prompt_template(cls) -> str:
        return CODE_SYSTEM_PROMPT
