# This program checks for un-encrypted credentials in a file directory
# You must provide it a directory.  
# From there, the program will check for files that may contain sensitive data and produce a report

#Import clear function
import os
clear = lambda: os.system('clear')
clear()

from os import listdir
from os.path import isfile, join


my_directory = input("What directory would you like to check? example 'c:\myscripts\'")

onlyfiles = [f for f in listdir(my_directory) if isfile(join(my_directory, f))]





