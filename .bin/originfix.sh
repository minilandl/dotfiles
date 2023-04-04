#!/bin/sh
wineprefix=/mnt/Games/SteamLibrarynative/steamapps/compatdata/wine

sudo rsync -avP $wineprefix/drive_c/ProgramData/Origin/SelfUpdate/Staged/ $wineprefix/drive_c/Program\ Files\ \(x86\)/Origin/

sudo rsync -avP  "$wineprefix/drive_c/Program Files/Electronic Arts/EA Desktop/StagedEADesktop/EA Desktop/"  "$wineprefix/drive_c/Program Files/Electronic Arts/EA Desktop/EA Desktop/"

