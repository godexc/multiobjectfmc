# Basic Multiple Object Creation Script for Firepower Management Center

This Python script allows you to create multiple objects, that are retrieved from a file, on Firepower Management Center. You can use it to create bulk objects or even it can help with the migration scenarios.

# Requirements

- Python
- Json and Requests Library
- Network Connectivity to Firepower Management Center

# How it works

You should run the script # python create_obj.py USERNAME PASSWORD FMCIP after that the script reads the create_obj.txt file in the format that has been shown on the example and posts the data to FMC.
