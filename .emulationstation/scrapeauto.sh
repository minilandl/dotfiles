#!/bin/sh

i=0
rm -rf $HOME/.emulationstation/gamelists/*/gamelist.xml

if i=0
then
Skyscraper -s sreenscraper -p nes
Skyscraper -s screenscraper -p dreamcast
Skyscraper -s screenscraper -p nds
Skyscraper -s screenscraper -p gbc
Skyscraper -s screenscraper -p gc
Skyscraper -s screenscraper -p gba
Skyscraper -s screenscraper -p megadrive
Skyscraper -s screenscraper -p n64
Skyscraper -s screenscraper -p neogeo
Skyscraper -s screenscraper -p nes
Skyscraper -s screenscraper -p ps2
Skyscraper -s screenscraper -p psp
Skyscraper -s screenscraper -p segacd
Skyscraper -s screenscraper -p wii
Skyscraper -s screenscraper -p wiiu
Skyscraper -s screenscraper -p snes
Skyscraper -s screenscraper -p psx
Skyscraper -s screenscraper -p fds
Skyscraper -s screenscraper -p gb
i=$((i+1)) 
echo $i
elif i=1
then
Skyscraper -p fds
Skyscraper -p nes
Skyscraper -p nds  
Skyscraper -p gbc
Skyscraper -p gc
Skyscraper -p gba  
Skyscraper -p megadrive
Skyscraper -p neogeo
Skyscraper -p ps2
Skyscraper -p psp
Skyscraper -p dreamcast 
Skyscraper -p n64
Skyscraper -p psx 
Skyscraper -p nds
Skyscraper -p gbc
Skyscraper -p gb
Skyscraper -p segacd
Skyscraper -p snes
Skyscraper -p gc
Skyscraper -p wiiu
Skyscraper -p wii
Skyscraper -p gba  
else echo "all done"
fi
