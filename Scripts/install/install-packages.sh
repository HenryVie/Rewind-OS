#!/bin/bash

PACKAGE_FILE="$1"

if [ ! -f "$PACKAGE_FILE" ]; then
	echo "Package list not found."
	exit 1
fi

sudo dnf install -y $(cat "$PACKAGE_FILE")
