#!/bin/sh
OUTPUT="$(swaymsg -t get_outputs | jq -r '.[]|select(.focused)|.name')"
WORKSPACE="$1"
# Switch to workspace and move it to the focused output. Focus it again, because move just moves.
swaymsg workspace "$WORKSPACE" \; move workspace to output "$OUTPUT" \; workspace "$WORKSPACE"
