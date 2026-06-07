#!/bin/bash

REWIND_ROOT="$HOME/Rewind-OS"

while true; do
    clear

    CALLER="$1"

    echo "==================="
    echo "   KINEAT BASE"
    echo "==================="

    echo ""

    echo "1. About Rewind OS"
    echo "2. User profiles"
    echo "3. Exit"

    read -r KINEAT_OPTION

    case $KINEAT_OPTION in
        1)
            clear
            cat "$REWIND_ROOT/Documentation/Kineat/about-rewind.md"
            echo ""
            read -rp "Press Enter to return..."
            ;;
        2)
            clear
            cat "$REWIND_ROOT/Documentation/Kineat/user-profiles.md"
            echo ""
            read -rp "Press Enter to return..."
            ;;
        3)
            if [ "$CALLER" = "welcome" ]; then
                clear && ./rewind-welcome.sh
                exit
            else
                clear
                exit
            fi
            ;;
        *)
            echo "Invalid option"
            continue
    esac
done