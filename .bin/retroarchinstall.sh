!#/bin/bash

cd $HOME/.config/retroarch/cores

wget -A "*.zip" -v -r -nd -l 1 https://buildbot.libretro.com/nightly/linux/x86_64/latest/

