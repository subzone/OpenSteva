"""Skill source resolvers — Hermes, OpenClaw, generic GitHub."""

from opensteva.skills.sources.base import ResolvedSkill, SourceResolver
from opensteva.skills.sources.github import GitHubResolver
from opensteva.skills.sources.hermes import HERMES_REPO_URL, HermesResolver
from opensteva.skills.sources.openclaw import OPENCLAW_REPO_URL, OpenClawResolver

__all__ = [
    "GitHubResolver",
    "HERMES_REPO_URL",
    "HermesResolver",
    "OPENCLAW_REPO_URL",
    "OpenClawResolver",
    "ResolvedSkill",
    "SourceResolver",
]
