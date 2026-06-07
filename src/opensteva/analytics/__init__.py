"""External anonymous usage analytics.

Sends anonymized events to PostHog so the OpenSteva team can measure
setup success, retention, feature usage, and churn — without ever
collecting chat content, prompts, file paths, emails, IPs, or hardware
identifiers.

Distinct from :mod:`opensteva.telemetry`, which stores local FLOPs and
energy metrics in a SQLite DB and never leaves the machine.

Disable: set ``[analytics] enabled = false`` in ``~/.opensteva/config.toml``.
"""

from opensteva.analytics.aggregator import SessionAggregator
from opensteva.analytics.bridge import EventBridge
from opensteva.analytics.client import AnalyticsClient
from opensteva.analytics.identity import (
    get_or_create_anon_id,
    is_analytics_enabled,
    reset_anon_id,
)
from opensteva.analytics.redaction import hash_id, redact

__all__ = [
    "AnalyticsClient",
    "EventBridge",
    "SessionAggregator",
    "get_or_create_anon_id",
    "is_analytics_enabled",
    "reset_anon_id",
    "redact",
    "hash_id",
]
