"""Tools primitive — tool system with ABC interface and built-in tools."""

from __future__ import annotations

from opensteva.tools._stubs import BaseTool, ToolExecutor, ToolSpec

# Import built-in tools to trigger @ToolRegistry.register() decorators.
# Each is wrapped in try/except so the package loads even before the
# individual tool modules are created.
try:
    import opensteva.tools.calculator  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.think  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.retrieval  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.llm_tool  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.file_read  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.web_search  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.code_interpreter  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.code_interpreter_docker  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.repl  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.storage_tools  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.mcp_adapter  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.channel_tools  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.http_request  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.docker_shell_exec  # noqa: F401
    import opensteva.tools.shell_exec  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.memory_manage  # noqa: F401
except ImportError:
    pass
try:
    import opensteva.tools.user_profile_manage  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.skill_manage  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.file_write  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.apply_patch  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.git_tool  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.db_query  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.pdf_tool  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.image_tool  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.audio_tool  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.knowledge_tools  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.text_to_speech  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.digest_collect  # noqa: F401
except ImportError:
    pass

__all__ = ["BaseTool", "ToolExecutor", "ToolSpec"]
