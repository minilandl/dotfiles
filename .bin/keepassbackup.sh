#!/bin/bash 

date=$(date +%Y-%m-%d)

rsync -avP ~/OneDrive/Documents/databasemacbook2.kdbx ~/Dropbox/databasemacbook2.kdbx

notify-send "Backup Keepass database to Dropbox 1/3"

rsync -avP ~/OneDrive/Documents/databasemacbook2.kdbx ~/databasemacbook2.kdbx

notify-send "Backup Keepass database to Local Storage 2/3"

rsync -avP ~/OneDrive/Documents/databasemacbook2.kdbx ~/OneDrive/databasemacbook2.kdbx

notify-send "Backup Keepass database to OneDrive 3/3"
