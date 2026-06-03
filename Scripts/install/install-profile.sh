#!/bin/bash

PROFILE="$1"
if [ -z "$PROFILE" ]; then
    echo "Usage: ./install-profile.sh $PROFILE"
    exit 1
fi

PROFILE_FILE="../../Packages/$PROFILE.txt"

if [ ! -f "$PROFILE_FILE" ]; then
    echo "Profile not found.
          Available profiles:
            - student
            - gamer
            - creator
            - hobbyist
            - beginner"
    exit 1
fi

echo "Installing essential packages..."
./install-packages.sh ../../Packages/essentials.txt

echo "Installing $PROFILE profile"
./install-packages.sh "$PROFILE_FILE"

echo "Installation completed!"