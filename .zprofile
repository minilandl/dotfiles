#
#!/bin/zsh
#

#exports 
export __GL_SHADER_DISK_CACHE=1 
export __GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1

export VK_ICD_FILENAMES="/usr/share/vulkan/icd.d/radeon_icd.x86_64.json:/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/amd_icd.x86_64.json:/usr/share/vulkan/icd.d/amd_icd.i686.json"



export PATH="${PATH}:/home/jasper/.bin"

export PATH="${PATH}:/home/jasper/.local/.bin"

export WINEPREFIX="/mnt/Games/SteamLibrarynative/steamapps/compatdata/wine"

export VK_ICD_FILENAMES="/usr/share/vulkan/icd.d/radeon_icd.x86_64.json:/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/amd_icd.x86_64.json:/usr/share/vulkan/icd.d/amd_icd.i686.json"

# default applications


# default applications
export EDITOR="nvim"
export TERMINAL="urxvt"
export TERMCMD="urxvt"
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
