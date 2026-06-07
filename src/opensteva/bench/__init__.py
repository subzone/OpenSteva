"""Benchmarking framework for OpenSteva inference engines."""

from __future__ import annotations

from opensteva.bench._stubs import BaseBenchmark, BenchmarkResult, BenchmarkSuite
from opensteva.core.registry import BenchmarkRegistry


def ensure_registered() -> None:
    """Ensure all benchmark implementations are registered."""
    from opensteva.bench.energy import ensure_registered as _reg_energy
    from opensteva.bench.latency import ensure_registered as _reg_latency
    from opensteva.bench.throughput import ensure_registered as _reg_throughput

    _reg_latency()
    _reg_throughput()
    _reg_energy()


# Trigger registration on import
ensure_registered()

__all__ = [
    "BaseBenchmark",
    "BenchmarkRegistry",
    "BenchmarkResult",
    "BenchmarkSuite",
    "ensure_registered",
]
