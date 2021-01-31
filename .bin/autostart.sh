#! /bin/sh 
# start Firefox

firefox &

#Start LibreOffice

#soffice &


#Start Dropbox

urxvt &

urxvt -e htop &

urxvt -e ranger &


urxvt -e ncmpcpp -s search_engine &


urxvt -e ncmpcpp -s playlist &


urxvt -e ncmpcpp -s browser &


urxvt -e vis &

dropbox &

onedrivemount.sh & 

#vmware &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#VirtualBox &

#spotify &


steam-runtime &

