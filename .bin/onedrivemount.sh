#!/bin/bash
umount -l /mnt/onedrive
rclone mount --vfs-cache-mode writes onedrive: /mnt/onedrive
