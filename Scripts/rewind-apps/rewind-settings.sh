#!/bin/bash

personalize_wallpaper() {
    clear

    WALLPAPER_PROPERTY=$(xfconf-query -c xfce4-desktop -l | grep last-image)
    WIN98_CLASSIC="$HOME/Rewind-OS/Themes/wallpapers/windows98_classic"
    WIN98_BLUE="$HOME/Rewind-OS/Themes/wallpapers/windows98_blue"
    WIN98_CLASSIC_BLANK="$HOME/Rewind-OS/Themes/wallpapers/windows98_classic_blank"
    WIN98_SKY_BLANK="$HOME/Rewind-OS/Themes/wallpapers/windows98_sky_blank"
    F43_NIGHT="$HOME/Rewind-OS/Themes/wallpapers/the_final_f43_night"
    FEDORA_BLUE="$HOME/Rewind-OS/Themes/wallpapers/fedora_darkblue"

    echo "What wallpaper do you want to set?"
    echo "1. Windows 98 Classic"
    echo "2. Windows 98 Blue"
    echo "3. Windows 98 Classic Blank"
    echo "4. Windows 98 Sky Blank"
    echo "5. The Final F43 Night"
    echo "6. Fedora Dark Blue"

    read -r BG_CHOICE

    case "$BG_CHOICE" in
        1)
            BG=$WIN98_CLASSIC
            BG_MESSAGE="Windows 98 Classic"
            ;;
        2)
            BG=$WIN98_BLUE
            BG_MESSAGE="Windows 98 Blue"
            ;;
        3)
            BG=$WIN98_CLASSIC_BLANK
            BG_MESSAGE="Windows 98 Classic Blank"
            ;;
        4)
            BG=$WIN98_SKY_BLANK
            BG_MESSAGE="Windows 98 Sky Blank"
            ;;
        5)
            BG=$F43_NIGHT
            BG_MESSAGE="The Final F43 Night"
            ;;
        6)
            BG=$FEDORA_BLUE
            BG_MESSAGE="Fedora Blue"
            ;;
    esac

    xfconf-query \
    -c xfce4-desktop \
    -p "$WALLPAPER_PROPERTY" \
    -s "$BG"

    echo "Your wallpaper has changed to $BG_MESSAGE!"

    echo ""
    read -rp "Press Enter to return"
}

default_browser() {
    clear

    CURRENT_DEFAULT_BROWSER=$(xdg-settings get default-web-browser)

    case $CURRENT_DEFAULT_BROWSER in
        "brave-browser.desktop")
            CURRENT_DEFAULT_BROWSER="Brave"
            ;;
        "chromium-browser.desktop")
            CURRENT_DEFAULT_BROWSER="Chromium"
            ;;
        "org.mozilla.firefox.desktop")
            CURRENT_DEFAULT_BROWSER="FireFox"
            ;;
    esac

    echo "Current default web browser: $CURRENT_DEFAULT_BROWSER"
    echo ""

    echo "SELECT DEFAULT BROWSER:"
    echo "1. Brave"
    echo "2. Chromium"
    echo "3. FireFox"
    echo ""

    read -r BROWSER_OPTION

    case $BROWSER_OPTION in
        1)
            xdg-settings set default-web-browser brave-browser.desktop
            CURRENT_DEFAULT_BROWSER="Brave"
            echo "$CURRENT_DEFAULT_BROWSER is now the default browser"
            ;;
        2)
            xdg-settings set default-web-browser chromium-browser.desktop
            CURRENT_DEFAULT_BROWSER="Chromium"
            echo "$CURRENT_DEFAULT_BROWSER is now the default browser"
            ;;
        3)
            xdg-settings set default-web-browser org.mozilla.firefox.desktop
            CURRENT_DEFAULT_BROWSER="FireFox"
            echo "$CURRENT_DEFAULT_BROWSER is now the default browser"
            ;;
    esac

    
    echo ""
    read -rp "Press Enter to return"
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
            while true; do
                clear
                echo "PERSONALIZATION"
                echo "1. Change Wallpaper"
                echo "2. Change theme"
                echo "3. Change accent color"
                echo "4. Return"

                read -r PERSONALIZE_CHOICE
                
                case $PERSONALIZE_CHOICE in
                    1)
                        personalize_wallpaper
                        ;;
                    4)
                        break
                        ;;
                esac
            done
            ;;
        2)
            while true; do
                clear
                echo "TASKBAR"
            done
            ;;
        3)
            while true; do
                clear
                echo "APPLICATIONS"
                echo "1. Set default web browser"
                echo "2. Return"

                read -r APPLICATION_CHOICE

                case $APPLICATION_CHOICE in
                    1)
                        default_browser
                        ;;
                    2)
                        break
                        ;;
                esac
            done
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