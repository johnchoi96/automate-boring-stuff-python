#!/usr/bin/python3

# mapIt.py - Launches a map in the browser using an address from file
# command line or clipboard

import webbrowser
import sys
import pyperclip
import requests

if len(sys.argv) > 1:
    # Get address from command line
    address = "".join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
