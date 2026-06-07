#!/bin/bash

REWIND_ROOT="$HOME/Rewind-OS"

sys_info() {
    clear

    echo "SYSTEM STATUS"
    echo ""

    echo "Distro: $(grep '^PRETTY_NAME=' /etc/os-release | cut -d= -f2 | tr -d '"')"
    echo "Kernel Version: $(uname -r)"
    echo "Device Name: $(hostname)"

    echo ""
    read -rp "Press Enter to return"
}

internet_stat() {
    clear

    echo "INTERNET STATUS"
    echo ""

    if ping -c 1 8.8.8.8 > /dev/null 2>&1; then
        echo "Status: Internet connected"
    else
        echo "Status: No Internet connection"
    fi

    echo ""
    read -rp "Press Enter to return"
}

disk_space() {
    clear
    echo "DISK SPACE"
    echo ""

    USED=$(df -h / | awk 'NR==2 {print $3}')
    AVAILABLE=$(df -h / | awk 'NR==2 {print $4}')
    PERCENT=$(df -h / | awk 'NR==2 {print $5}')

    echo "Used: $USED"
    echo "Available: $AVAILABLE"
    echo "Usage:$PERCENT"

    echo ""
    read -rp "Press Enter to return"
}

mem_usage() {
    clear
    echo "MEMORY USAGE"
    echo ""

    TOTAL_RAM=$(free -h | awk '/Mem:/ {print $2}')
    USED_RAM=$(free -h | awk '/Mem:/ {print $3}')
    AVAILABLE_RAM=$(free -h | awk '/Mem:/ {print $7}')

    echo "Total RAN: $TOTAL_RAM"
    echo "Used RAM: $USED_RAM"
    echo "Available RAM: $AVAILABLE_RAM"

    echo ""
    read -rp "Press Enter to return"
}

update_checker() {
    clear

    echo "CHECK FOR UPDATES"
    echo ""

    echo "Checking..."

    dnf check-update
    
    echo ""
    read -rp "Press Enter to return"
}

refresh_packcache() {
    clear

    echo "REFRESH PACKAGE CACHE"
    echo ""

    sudo dnf makecache
    echo ""
    echo "Package cache refreshed successfully!"

    echo ""
    read -rp "Press Enter to return"
}

installed_repo() {
    clear

    echo "INSTALLED REPOSITORIES"
    echo ""

    dnf repolist

    echo ""
    read -rp "Press Enter to return"
}

sys_uptime() {
    clear
    echo "SYSTEM UPTIME"
    echo ""

    UPTIME=$(uptime -p | sed 's/^./\U&/')
    echo "$UPTIME"

    echo ""
    read -rp "Press Enter to return"
}

while true; do
    clear

    CALLER="$1"        

    echo "======================"
    echo "  REWIND TECHNICIAN"
    echo "======================"

    echo "1. System Information"
    echo "2. Internet Status"
    echo "3. Disk Space"
    echo "4. Memory Usage"
    echo "5. Check for Updates"
    echo "6. Refresh Package Cache"
    echo "7. Installed Repositories"
    echo "8. System Uptime"
    echo "9. Exit"
    
    read -r TECHINICAN_MENU
    case $TECHINICAN_MENU in
        1)
            sys_info
            ;;
        2)
            internet_stat
            ;;
        3)
            disk_space
            ;;
        4)
            mem_usage
            ;;
        5)
            update_checker
            ;;
        6)
            refresh_packcache
            ;;
        7)
            installed_repo
            ;;
        8)
            sys_uptime
            ;;
        9)
            if [ "$CALLER" = "welcome" ]; then
                clear && "$REWIND_ROOT/Scripts/rewind-apps/rewind-welcome.sh"
                exit
            else
                clear
                exit
            fi
            ;;
        *)
            echo "Invalid choice. Please try again"
            echo ""
            read -rp "Press Enter to continue"
            ;;
    esac
done