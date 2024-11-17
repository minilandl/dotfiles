#!/bin/bash

for dir in /sys/class/hwmon/hwmon*; do
# check if the directory exists and is a directory
if [ -d "$dir" ]; then
# execute the cat name command in the directory
echo "$dir "
cat "$dir/name"
echo
fi
done 
