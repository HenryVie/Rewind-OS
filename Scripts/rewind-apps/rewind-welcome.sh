#!/bin/bash

REWIND_ROOT="$HOME/Rewind-OS"

clear

echo "================================="
echo "      Welcome to Rewind OS"
echo "================================="

echo "1. Setup my computer"
echo "2. View documentation"
echo "3. Settings"
echo "4. Technician"
echo "5. Exit"

read -r OPTION

case $OPTION in
    1)
        "$REWIND_ROOT/Scripts/install/profile-menu.sh"
        ;;
    2)
        echo "Opening Kineat Base..."
        "$REWIND_ROOT/Scripts/rewind-apps/kineat-base.sh" welcome
        ;;
    3)
        "$REWIND_ROOT/Scripts/rewind-apps/rewind-settings.sh" welcome
        ;;
    4)
        "$REWIND_ROOT/Scripts/rewind-apps/rewind-technician.sh" welcome
        ;;
    5)
        clear && exit
        ;;
    *)
        echo "Invalid option"
        ;;
esac