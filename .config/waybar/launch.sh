#!/bin/sh

# Terminate already running bar instances
killall -q waybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# Launch
waybar

echo "Bar launched..."
