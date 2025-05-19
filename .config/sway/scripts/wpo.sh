#!/bin/sh
OUTPUT_INDEX="$(swaymsg -t get_outputs | jq 'map(.focused)|to_entries|.[]|select(.value)|.key+1')"
NUMBER=$1
# Prefix every workspace with output index:
# - If it doesn't exist yet, it will be created on the current, focused output.
# - If it exists it must be on the current output and it will be focused.
swaymsg workspace "$OUTPUT_INDEX-$NUMBER"
