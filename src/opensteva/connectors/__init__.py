"""Data source connectors for Deep Research."""

from opensteva.connectors._stubs import (
    Attachment,
    BaseConnector,
    Document,
    SyncStatus,
)
from opensteva.connectors.store import KnowledgeStore

__all__ = ["Attachment", "BaseConnector", "Document", "KnowledgeStore", "SyncStatus"]

# Auto-register built-in connectors
import opensteva.connectors.obsidian  # noqa: F401

try:
    import opensteva.connectors.gmail  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.gmail_imap  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.gdrive  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import opensteva.connectors.notion  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.granola  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.gcontacts  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.imessage  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.apple_notes  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.apple_music  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.apple_contacts  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.slack_connector  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.outlook  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.gcalendar  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.dropbox  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import opensteva.connectors.whatsapp  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.oura  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.apple_health  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.strava  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.spotify  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.google_tasks  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.weather  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.github_notifications  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.hackernews  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.connectors.news_rss  # noqa: F401
except ImportError:
    pass
