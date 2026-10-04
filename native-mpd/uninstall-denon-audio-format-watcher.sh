#!/bin/bash
set -euo pipefail

label="fi.sulopuisto.denon-audio-format-watcher"
install_dir="$HOME/.local/opt/denon-audio-format-watcher"
plist="$HOME/Library/LaunchAgents/$label.plist"
launchctl bootout "gui/$(id -u)/$label" 2>/dev/null || true
rm -f "$plist"
rm -rf "$install_dir"
printf 'Removed %s\n' "$label"
