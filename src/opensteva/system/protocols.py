"""Structural protocols for substituting fakes in place of StevaSystem."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Protocol

if TYPE_CHECKING:
    from opensteva.core.config import StevaConfig
    from opensteva.core.events import EventBus
    from opensteva.engine._stubs import InferenceEngine
    from opensteva.security.capabilities import CapabilityPolicy
    from opensteva.sessions.session import SessionStore
    from opensteva.tools._stubs import BaseTool
    from opensteva.tools.storage._stubs import MemoryBackend
    from opensteva.traces.collector import TraceCollector
    from opensteva.traces.store import TraceStore


class OrchestratorDeps(Protocol):
    """Minimum surface of StevaSystem that QueryOrchestrator depends on.

    Tests can satisfy this with a lightweight class — no need to construct
    the full StevaSystem dataclass or materialize every subsystem.
    """

    config: StevaConfig
    bus: EventBus
    engine: InferenceEngine
    engine_key: str
    model: str
    agent_name: str
    tools: List[BaseTool]
    memory_backend: Optional[MemoryBackend]
    capability_policy: Optional[CapabilityPolicy]
    session_store: Optional[SessionStore]
    trace_store: Optional[TraceStore]
    trace_collector: Optional[TraceCollector]  # written by _run_agent

    # Optional attribute (getattr with default) — declared for type clarity.
    _skill_few_shot_examples: Any
