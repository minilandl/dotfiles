# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from pathlib import Path
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen 
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401
from spotify import Spotify
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration




@hook.subscribe.startup_once
def autostart():
    home = Path('/home/jasper/.bin/autostart.sh').expanduser()
    subprocess.run(home)



mod = "mod4"#Super
mod1 = "mod1"#Alt

terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "c", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], 'space', lazy.spawn('rofi -show drun -theme purple ')),
    Key([mod], 'w', lazy.spawn('rofi -show window -theme purple ')),
    Key([mod], 'e', lazy.spawn('rofi -show emoji -theme purple ')),
    #Key([mod1], 'n', lazy.spawn('mpc --host= next')),
    Key([mod1], 'n', lazy.spawn('mpc --host 192.168.1.28 --port 6600 next')),
    #Key([mod1], 'b', lazy.spawn('playerctl -p spotify previous')),
    Key([mod1], 'b', lazy.spawn('mpc --host 192.168.1.28 --port 6600 prev')),
    Key([mod, "mod1"], 'h', lazy.spawn('systemctl hibernate')),
    #Key([mod1], 'p', lazy.spawn('playerctl -a play-pause')),
    Key([mod1], 'p', lazy.spawn('mpc --host 192.168.1.28 --port 6600 toggle')),
    Key([mod], 'f', lazy.window.toggle_fullscreen()),
    Key([mod1], '3', lazy.spawn('scrot -t 1 -f -s -z /home/jasper/Pictures/screenshots/%Y-%m-%d-%T-screenshot.png')),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), lazy.spawn("/home/jasper/.config/polybar/launch.sh")),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod1], "u", lazy.spawn('amixer sset Master 5%+ unmute')),
    Key([mod1], "d", lazy.spawn('amixer sset Master 5%- unmute')),
    Key([mod, "mod1"], 'f', lazy.spawn('firefox')),
    Key([mod, "mod1"], 's', lazy.spawn('steam')),
    Key([mod], 't', lazy.spawn('/home/jasper/.bin/transon')),
    Key([mod, "mod1"], 't', lazy.spawn('/home/jasper/.bin/transoff')),
    ]

groups = [Group(i) for i in "1234567890"]


groups = [Group("1", layout='monadthreecol'),
          Group("2", layout='monadthreecol'),
          Group("3", layout='monadthreecol'),
          Group("4", layout='monadthreecol'),
          Group("5", layout='monadthreecol'),
          Group("6", layout='monadthreecol'),
          Group("7", layout='monadthreecol'),
          Group("8", layout='Columns'),
          Group("9", layout='monadthreecol'),
          Group("0", layout='monadthreecol')]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key( [mod], i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layout_theme = {"border_width": 3,
                "margin": 15,
                "border_focus": "0D8CA8",
                "border_normal": "bbcfd8",
                }


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.Bsp(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]


colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

colors = []
cache='/home/jasper/.cache/wal/colors' 
def load_colors(cache): 
    with open(cache, 'r') as file:         
        for i in range(8):             
            colors.append(file.readline().strip())     
    colors.append('#ffffff')     
    lazy.reload() 
load_colors(cache) 



widget_defaults = dict(
    font="TerminusTTF Nerd Font",
    fontsize=12,
    #padding=15,
)
extension_defaults = widget_defaults.copy()



screens = [     
    Screen( 

wallpaper='~/Pictures/wallpapers/wallpaper.jpg',
wallpaper_mode='fill',
      
           ),
]



#screens = [
#    Screen(
#     wallpaper='~/Pictures/wallpapers/wallpaper.jpg',
#        wallpaper_mode='fill',
#        ), 
#screens = [   
#   Screen(
#        top=bar.Bar(
#            [
#                widget.GroupBox(
#                    fmt=' {} ', 
#                    background=colors[1], 
#                    this_current_screen_border=colors[0], 
#                    this_screen_border=colors[0], 
#                    inactive=colors[0]
#                    ),
#                Spotify(), 
#                widget.WindowName(format=' {state}{name} '),
                #widget.Bluetooth(hci='/dev_41_42_30_00_18_CD', fmt=' Bluetooth: {} ', background=colors[6]),
                #widget.KeyboardLayout(fmt=' Keyboard: {} ', background=colors[1], configured_keyboards=['us', 'es']),
				#widget.Battery(charge_char='+', discharge_char='-', full_char='', show_short_text=False, format=' Power: {char}{percent:2.0%} ', background=colors[6], notify_below=10),
#				widget.Volume(background=colors[1], fmt=' Volume: {} '),
#                widget.CPU( format=' CPU: {freq_current}GHz {load_percent}% '),
#                widget.Memory(background=colors[1], fmt=' RAM: {} '),
                #widget.Wlan(interface='wlan0', background=colors[6], disconnected_message=' Disconnected ', format=' Network: {essid} '),
#                widget.Clock(format=' %A, %B %d %I:%M %p ', background=colors[1]),
#            ],
#            20,
#			background=colors[0],
#        ),    
     
#        wallpaper='~/Pictures/wallpapers/wallpaper.jpg',
#        wallpaper_mode='fill',
      

#        ),
#    ]







# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
#wl_input_rules = False

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
