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

def checkIntegrity():
    """ Function: checkIntegrity().

    Purpose: This function checks to see if the root folder is organized in the
        particular manner required for all other functions. If this function
        detects that the root folder is organized in some other manner, then
        it will throw an error.

    Argument(s): This program does not accept any arguments.

    Return Value(s): This program does not return any values.

    Error(s): This program will throw the InvalidRootOrganizationError error.

    Usage: This function is meant to be used at the start of the main program.

    """
    isInCanonicalForm = True

    if not isInCanonicalForm:
        print("Throwing an error.")

        # We mean to actually throw an error here. However, we must first
        # create those custom errors.


def loadDatabase(pathToDatabase):
    try:
        db = open(pathToDatabase)
    except IOError:
        # Clearly the state of the system is off. We need to alert the user
        # and issue an exit.
        print("Error. Exiting Now!")
    else:
        return db


def main(): 
    # These are the global variables used in this program.
    system = platform.system()

    # This is the root folder, which houses all the programs. All other 
    # programs, data, or relevant files, are located within this folder. We 
    # expect that this root folder is the folder where this program was ran.
    rootFolder = os.getcwd()

    # These are the main directories that house all the other files that this
    # program will need.
    dataFolder = os.path.join(rootFolder, "data")
    databaseFolder = os.path.join(rootFolder, "database")
    sourceFolder = os.path.join(rootFolder, "source")
    
    # Now we wish to load in the database. We have a function that handles
    # this for us nicely.
    pathToDatabase = os.path.join(databaseFolder, "database.p")
    
    # ... #

    # Cleanup checks.
    #   1. Are all files that were opened, now closed?
    #   2. Are all files that were written to, now saved?
    #   3. Are there any errors that needed to be handled?
    #   4. Do we need to do anything with the state of the database (i.e. Do 
    #       we need to cleanup anything?)
    #   5. Do we need to wipe any temporary files?
