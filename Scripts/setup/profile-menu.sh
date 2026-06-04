#!/bin/bash

echo "==================="
echo "   PROFILE MENU"
echo "==================="

echo "What type of user are you?"
echo "1. Student"
echo "2. Gamer"
echo "3. Hobbyist"
echo "4. Creator"
echo "5. Linux Beginner"

read -r TYPE

case $TYPE in
    1)
        ../install/install-profile.sh student
        ;;
    2)
        ../install/install-profile.sh gamer
        ;;
    3)
        ../install/install-profile.sh hobbyist
        ;;
    4)
        ../install/install-profile.sh creator
        ;;
    5)
        ../install/install-profile.sh beginner
        ;;
    *)
        echo "Invalid option!"
        ;;
esac