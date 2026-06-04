#!/bin/bash

personalize_wallpaper() {
    WALLPAPER_PROPERTY=$(xfconf-query -c xfce4-desktop -l | grep last-image)
    WIN98_CLASSIC="/home/nam/Rewind-OS/Themes/wallpapers/windows98_classic"
    WIN98_BLUE="/home/nam/Rewind-OS/Themes/wallpapers/windows98_blue"

    echo "What wallpaper do you want to set?"
    echo "1. Windows 98 Classic"
    echo "2. Windows 98 Blue"

    read -r BG_CHOICE

    case "$BG_CHOICE" in
        1)
            BG=$WIN98_CLASSIC
            ;;
        2)
            BG=$WIN98_BLUE
            ;;
    esac

    xfconf-query \
    -c xfce4-desktop \
    -p "$WALLPAPER_PROPERTY" \
    -s "$BG"
}

while true; do
    clear

    echo "====================="
    echo "   REWIND SETTINGS"
    echo "====================="

    echo "1. Personalization"
    echo "2. Taskbar"
    echo "3. Applications"
    echo "4. About"
    echo "5. Return"

    read -r SETTINGS_OPTION

    case $SETTINGS_OPTION in
        1)
            clear
            echo "PERSONALIZATION"
            echo "1. Change Wallpaper"
            echo "2. Change theme"
            echo "3. Change accent color"

            read -r PERSONALIZE_CHOICE
            
            case $PERSONALIZE_CHOICE in
                1)
                    personalize_wallpaper "$PERSONALIZE_CHOICE"
                    ;;
            esac

            echo ""
            read -rp "Press Enter to return..."
            ;;
        2)
            clear
            echo "TASKBAR"
            
            echo ""
            read -rp "Press Enter to return..."
            ;;
        3)
            clear
            echo "APPLICATIONS"

            echo ""
            read -rp "Press Enter to return..."
            ;;
        4)
            clear
            echo "====================="
            echo "   ABOUT REWIND OS"
            echo "====================="

            echo "Version: Prototype v0.1"
            echo "Developer: Nguyen Dinh Nam a.k.a HenryVie"

            echo ""
            echo "System Information:"
            echo "Fedora Version: $(grep '^PRETTY_NAME=' /etc/os-release | cut -d= -f2 | tr -d '"')"
            echo "Kernel Version: $(uname -r)"
            echo "Hostname: $(hostname)"
            echo "XFCE Version: $(xfce4-about --version | head -n 1)"

            echo ""
            read -rp "Press Enter to return..."
            ;;
        5)
            clear
            ./rewind-welcome.sh
            ;;
        *)
            echo "Invalid option"
            continue
    esac
done