#!/bin/bash

echo "================================="
echo "      Welcome to Rewind OS"
echo "================================="

echo "1. Setup my computer"
echo "2. View documentation"
echo "3. Exit"

read -r OPTION

case $OPTION in
    1)
        ./profile-menu.sh
        ;;
    2)
        echo "Opening Kineat Base..."
        ../rewind-apps/kineat-base.sh
        ;;
    3)
        exit
        ;;
    *)
        echo "Invalid option"
        ;;
esac