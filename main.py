##############################################################################
#
#   File: main.py
#
#   Author: Dravin Flores <flores69@msu.edu>
#
#   Created: 24 October 2020
#
#   Last Modified: 28 October 2020
#
#   Purpose: This program acts as the main GUI-based interface to the database
#       and Swager Station for the sMDT Project. 
#
###############################################################################

# These are all the modules that are required for this program to run.
import platform
import pickle
import sys
import os

# This is apparently a more friendly way of dealing with paths in Python 3.6+.
from pathlib import Path

# Here are our user defined things.
from source.database-gui import dg
from source.swager-gui import sg
from source.open-utility.py import *

import source.database-gui as dg
import source.swage-gui as sg
import source.open-utility as ou

def main(): 
    # These are the global variables used in this program.
    system = platform.system()

    # Just for note, we will assume that we are working in the root folder for
    # this project. This root folder is likely named "sMDT", however it doesn't
    # really matter.
    
    # Here are all the directories which store files.
    dataFolder = Path("data")
    databaseFolder = Path("database")
    sourceFolder = Path("source")
    
    # Here is the path to the database pickle file itself. How nice for the
    # path to be so idiomatic.
    dbFile = databaseFolder / "database.p"

    openedDB = ou.loadDatabase(dbFile)

    # Cleanup checks.
    #   1. Are all files that were opened, now closed?
    #   2. Are all files that were written to, now saved?
    #   3. Are there any errors that needed to be handled?
    #   4. Do we need to do anything with the state of the database (i.e. Do 
    #       we need to cleanup anything?)
    #   5. Do we need to wipe any temporary files?
