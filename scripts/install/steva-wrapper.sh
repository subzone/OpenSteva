#!/usr/bin/env bash
# jarvis-wrapper.sh — symlinked to ~/.local/bin/jarvis.
# Activates the managed venv and execs the real jarvis CLI.

OPENJARVIS_HOME="${OPENJARVIS_HOME:-$HOME/.opensteva}"
VENV="$OPENJARVIS_HOME/.venv"

if [[ ! -d "$VENV" ]]; then
    echo "jarvis: venv not found at $VENV" >&2
    echo "Re-run the installer: curl -fsSL https://subzone.github.io/OpenSteva/install.sh | bash" >&2
    exit 1
fi

exec "$VENV/bin/jarvis" "$@"
