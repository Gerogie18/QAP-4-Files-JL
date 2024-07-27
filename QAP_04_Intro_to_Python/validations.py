#Description: A general validation library for commonly used validations
            # Referenced by the utils python script.
#Name: Jennifer Lyver
#Date: July 16 2024 - July 19 2024

#Import Libraries

#Definitions
#YES / NO Validators
def Y_N(string):
    string = string.upper().strip()
    errormessage = None
    if_yes = None
    if string == "YES" or string == "Y":
        val = True
        if_yes = True
    elif string == "NO" or string == "N":
        val = True
        if_yes = False
    else:
        val = False
        errormessage = "\nInvalid response. Please enter Y or N.\n"
        
    return val, errormessage, if_yes

#validate list of strings - List should be capitalized
def validate_list(string, list):
    string = string.upper()
    if string in list:
        val = True
    else:
        val = False
        
    return val

def phone_number_national(string):
    canadian_area_codes = [ #chatgbt
    "204", "236", "249", "250", "289", "306", "343", "365", "403", "416",
    "418", "431", "437", "438", "450", "506", "514", "519", "548", "579",
    "581", "587", "604", "613", "639", "647", "672", "705", "709", "742",
    "778", "780", "782", "807", "819", "825", "867", "873", "902", "905"]

    val = None
    type = "Phone Number"
    string = "".join(filter(str.isdigit, string))
    #check if blank
    val, errormessage = not_empty(string, type)
    if not val:
        return val, errormessage
    #check if not 10 digits
    if len(string) != 10:
        val = False
        errormessage = f"{type} must be 10 digits"
    #check if not a Canadian area code
    elif string[:3] not in canadian_area_codes:
        errormessage = f"{type} must be a Canadian area code"
    else:
        val = True
    return val, errormessage

def val_province_abv(string):
    errormessage = None
    provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
    if len(string) != 2:
        val = False
        errormessage = "Province must be exactly 2 characters"
    else:
        string = string.upper()
        if string not in provinces:
            val = False
            errormessage = "Invalid province"
        else:
            val = True
    return val, errormessage

def not_empty(string, type):
    errormessage = None
    if string == "":
        errormessage = f"\n{type} cannot be empty\n"
        val = False
    else:
        val = True
    return val, errormessage

def validate_isalpha(string, type):
    errormessage = None
    # Remove spaces and apostrophes
    modified_string = string.replace(" ", "").replace("'", "")
    if not modified_string.isalpha():
        errormessage = f"\n{type} should only contain letters, spaces, and apostrophes\n"
        val = False
    else:
        val = True
    return val, errormessage

def validate_streetaddress(string):
    type = "Street address"
    errormessage = None
    #check if empty
    val, errormessage = not_empty(string, type)
    if not val:
        return val, errormessage
    #check if first character is a number
    if not string[0].isdigit():
        errormessage = f"\n{type} should start with a number\n"
        val = False
    else:
        val = True
    return val, errormessage

def validate_postal_code(string):
    type = "Postal code"
    string = string.replace(" ", "")  # removes spaces
    errormessage = None

    # Check if empty
    val, errormessage = not_empty(string, type)
    if not val:
        return val, errormessage

    # Check if exactly 6 characters
    if len(string) != 6:
        errormessage = f"\n{type} should be exactly 6 characters long.\n"
        val = False
    # Check if in the format A#A#A#
    elif not (string[0].isalpha() and string[1].isdigit() and
              string[2].isalpha() and string[3].isdigit() and
              string[4].isalpha() and string[5].isdigit()):
        errormessage = f"\n{type} should be in the format A#A#A# where A is a letter and # is a digit.\n"
        val = False
    else:
        val = True
    return val, errormessage

def validate_positive_integer(string, type):
    errormessage = None
    if not string.isdigit():
        errormessage = f"\n{type} should only contain numbers\n"
        val = False
    else:
        if not int(string) > 0:
            errormessage = f"\n{type} should be a positive number\n"
            val = False
        else:
            val = True
    return val, errormessage