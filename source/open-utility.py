##############################################################################
#
#   File: open-utility.py
#
#   Author: Dravin Flores <flores69@msu.edu>
#
#   Created: 4 November 2020
#
#   Last Modified: 4 November 2020
#
#   Purpose: This file holds all the utilities for handling files that pertain
#       to the sMDT Project.
#
###############################################################################

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


def loadDatabase(pathToDatabaseStr):
    try:
        db = pickle.load(pathToDatabaseStr, 'rb')
    except IOError:
        # Clearly the state of the system is off. We need to alert the user
        # and issue an exit.
        print("Error. Exiting Now!")

        # This is just a terrible way of alerting the user. We really want
        # to get the user to see an error, which would be so much nicer than
        # just returning something.
        return None
    else:
        return db

