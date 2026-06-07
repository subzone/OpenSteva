"""Storage primitive — persistent searchable storage."""

from __future__ import annotations

# Always-available backend
import opensteva.tools.storage.sqlite  # noqa: F401

# Optional backends — import to trigger registration
try:
    import opensteva.tools.storage.bm25  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.storage.faiss_backend  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.storage.colbert_backend  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.storage.hybrid  # noqa: F401
except ImportError:
    pass

try:
    import opensteva.tools.storage.dense  # noqa: F401
except ImportError:
    pass

from opensteva.tools.storage._stubs import MemoryBackend, RetrievalResult
from opensteva.tools.storage.chunking import Chunk, ChunkConfig, chunk_text
from opensteva.tools.storage.context import ContextConfig, inject_context
from opensteva.tools.storage.ingest import ingest_path, read_document

__all__ = [
    "Chunk",
    "ChunkConfig",
    "ContextConfig",
    "MemoryBackend",
    "RetrievalResult",
    "chunk_text",
    "inject_context",
    "ingest_path",
    "read_document",
]
