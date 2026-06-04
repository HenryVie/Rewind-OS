#!/bin/bash



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
            cat ../../Documentation/Kineat/about-rewind.md
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