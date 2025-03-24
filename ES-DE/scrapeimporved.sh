#bin/sh

declare -a platforms=("nds" "snes" "atari2600" "atari7800" "atarilynx" "atarilynx" "c64" "daphne" "dreamcast" "arcade" "fds" "gamegear" "gb" "gbc" "gba" "gc" "intellivion" "mastersystem" "megadrive" "msx" "msx2" "n64" "nes" "neogeo" "ngp" "ports" "ps2" "ps3" "psp" "psx" "scummvm " "sega32x" "segacd" "sufami" "switch" "pcenginecd" "zxspectrum" "wiiu" "wii" "vectrex" "wonderswan" "wonderswancolor" "amiga")

for i in "${platforms[@]}"
do
  Skyscraper -s screenscraper -p "$i"
  Skyscraper -p "$i"
done

