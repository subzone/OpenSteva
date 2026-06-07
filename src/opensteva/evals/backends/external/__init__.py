"""External-framework subprocess backends (Hermes Agent, OpenClaw)."""

from opensteva.evals.backends.external.hermes_agent import HermesBackend
from opensteva.evals.backends.external.openclaw import OpenClawBackend

__all__ = ["HermesBackend", "OpenClawBackend"]
