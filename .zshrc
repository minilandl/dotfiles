# Lines configured by zsh-newuser-install

PROMPT="%B%F{magenta}%n%F{yellow}@%F{cyan}%M %F{white}%~ %F{green}$ %f%b"
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

export PATH="${PATH}:${HOME}/jasper/.bin/"

export PATH="${PATH}:${HOME}/jasper/.local/bin/"

source /usr/share/zsh/plugins/zsh-bd/bd.plugin.zsh
source /usr/share/zsh/plugins/zsh-colored-man-pages/colored-man-pages.plugin.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh 
source ~/.bin/shortcuts/commands
source $HOME/.config/vifm

ZSH_AUTOSUGGEST_STRATEGY=(completion history)
zstyle ':completion:*' menu select
zmodload zsh/complist
HISTFILE=~/.cache/zsh/history 
HISTSIZE=10000 
SAVEHIST=10000

setopt SHARE_HISTORY
setopt HIST_IGNORE_SPACE
setopt HIST_IGNORE_ALL_DUPS
setopt autocd
setopt completealiases
autoload -Uz compinit
compinit



bindkey '^A' vi-beginning-of-line

bindkey '^L' vi-end-of-line

bindkey '^x' vi-delete-char

# End of lines added by compinstall
export PATH="$PATH:/home/username/.local/bin"
