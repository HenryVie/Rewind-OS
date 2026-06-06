#!/bin/bash

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
        ./profile-menu.sh
        ;;
    2)
        echo "Opening Kineat Base..."
        ./kineat-base.sh welcome
        ;;
    3)
        ./rewind-settings.sh welcome
        ;;
    4)
        ./rewind-technician.sh welcome
        ;;
    5)
        clear && exit
        ;;
    *)
        echo "Invalid option"
        ;;
esac