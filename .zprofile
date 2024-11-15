#
#!/bin/zsh
#

#exports 

export WLR_DRM_DEVICES=/dev/dri/card1
export PATH="${PATH}:/home/jasper/.bin"

export PATH="${PATH}:/home/jasper/.local/.bin"

export WINEPREFIX="/mnt/Games/SteamLibrarynative/steamapps/compatdata/wine"


# default applications


# default applications
export EDITOR="nvim"
export TERMINAL="alacritty"
export TERMCMD="alacrity"
export BROWSER="firefox"
export READER="zathura"
export EDITOR="nvim crontab -e"



# XDG shit
export XDG_DESKTOP_DIR="$HOME/Downloads"
export XDG_DOCUMENTS_DIR="$HOME/Documents"
export XDG_DOWNLOAD_DIR="$HOME/Downloads"
export XDG_MUSIC_DIR="$HOME/Music"
export XDG_PICTURES_DIR="$HOME/Pictures"
export XDG_VIDEOS_DIR="$HOME/Videos"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_CONFIG_HOME="$HOME/.config" 
