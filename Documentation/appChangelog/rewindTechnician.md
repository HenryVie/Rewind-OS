# Rewind Technician Changelog

## 06/6/2026
### Version Prototype 1.0
- The first prototype of Rewind Technician
- Added Technician menu
- Added feature: System Information. This feature shows the user information about based-distro version, kernel version, and hostname
- Added feature: Internet Status. This diagnostic feature shows the user connection status of their internet
- Added feature: Disk Space. This diagnostic feature shows the user current status of their disk space, includes: used space, available space, and percentage of used space
- Added feature: Memory Usage. This diagnostic feature shows the user current status of their RAM, includes: total RAM, used RAM, and available RAM
### Version Prototype 1.1
- Connected Rewind Technician to Rewind Welcome. From now, if Technician is launched from Welcome, when the user choose exit, it returns to Welcome instead of killing the whole shell
### Version Prototype 1.2
- Added feature: Check for Updates. This feature automatically checks to see if there is any package in the system that can be updated
- Added feature: Refresh Package Cache. This feature will refresh the caches automatically
- Added feature: Installed Repositories. This feature shows the installed packages on the machine
- Added feature: System Uptime. This feature shows how long the system is running

## 07/6/2026
### Version Prototype 1.2.1
- Fixed the bug which caused Rewind Technician to be unable to be launched from Welcome when Welcome is ran via app launcher

## 17/6/2026
### Version Prototype 2.0
- Technician now became GUI app, given a simple graphical user interface by using Python and GTK toolkit
- Connected as a function inside the new Rewind Hub app