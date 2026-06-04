#!/bin/bash

while true; do
    clear

    echo "==================="
    echo "   KINEAT BASE"
    echo "==================="

    echo ""

    echo "1. About Rewind OS"
    echo "2. User profiles"
    echo "3. Return to Startup menu"

    read -r KINEAT_OPTION

    case $KINEAT_OPTION in
        1)
            clear
            cat ../../Documentation/Kineat/about-rewind.md
            echo ""
            read -rp "Press Enter to return..."
            ;;
        2)
            clear
            cat ../../Documentation/Kineat/user-profiles.md
            echo ""
            read -rp "Press Enter to return..."
            ;;
        3)
            clear
            ../setup/rewind-welcome.sh
            ;;
        *)
            echo "Invalid option"
            continue
    esac
done