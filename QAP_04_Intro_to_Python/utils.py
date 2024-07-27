#Description: This file contains the main utiity functions for then main
            # python script.  This file has the exit funtion, loading bar,
            # and user input functions.  It references the Validations
            # python file.
#Name: Jenn Lyver
#Date: July 16 2024 - July 19, 2024
#Edit: July 26, 2024 - changed validations file name

#import Libraries
import validations as VAL
import sys

#default that input does not end main until true

#Utilities
def end(string):
    if string.upper().strip() == "END":
        print("\nProgram exit - data not saved.\n")
        sys.exit()
    else:
        pass

#loading bar
    # From the url: https://handhikayp.medium.com/creating-terminal-progress-bar-using-python-without-external-library-b51dd907129c
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

#Customer Information
def get_firstname():
    print()
    while True:
        firstname = input("First Name: ").title().strip()
        end(firstname) #check if end

        #check if empty
        if not firstname:
            print("First name cannot be empty.")
        #check if only contains letters
        elif not VAL.validate_isalpha(firstname, "First name"):
            print("First name can only contain letters.")
        else:
            return firstname

def get_lastname():
    print()
    while True:
        lastname = input("Last Name: ").title().strip()
        end(lastname) #check if end
        #check if empty
        if not lastname:
            print("Last name cannot be empty.")
        #check if only contains letters
        elif not VAL.validate_isalpha(lastname, "Last Name"):
            print("Last name can only contain letters.")
        else:
            return lastname
        
def get_streetaddress():
    print()
    while True:
        streetaddress = input("Street address: ").title().strip()
        end(streetaddress) #check if end
        val, errormessage = VAL.validate_streetaddress(streetaddress)
        if not val:
            print(errormessage)
        else:
            return streetaddress

def get_city():
    print()
    while True:
        city = input("City: ").title().strip()
        end(city) #check if end
        #check if empty
        val, errormessage = VAL.not_empty(city, "City")
        if not val:
            print(errormessage)
        else:
            #check if only contains letters
            val, errormessage = VAL.validate_isalpha(city, "City")
            if not val:
                print(errormessage)
            else:
                return city
    #Province
def get_province_abv():
    print()
    while True:
        province = input("Province: ").upper().strip()
        end(province) #check if end
        #validate province
        val, errormessage = VAL.val_province_abv(province)
        if not val:
            print(errormessage)
        else:
            return province
            
def get_postal_code():
    print()
    while True:
        postal_code = input("Postal Code: ").upper().strip()
        end(postal_code) #check if end
        #validate postal code
        val, errormessage = VAL.validate_postal_code(postal_code)
        if not val:
            print(errormessage)
        else:
            return postal_code

def get_phone_number():
    print()
    while True:
        phone_number = input("Phone Number: ")
        end(phone_number) #check if end
        #validate phone number
        val, errormessage = VAL.phone_number_national(phone_number)
        if not val:
            print(errormessage)
        else:
            phone_number = ''.join(filter(str.isdigit, phone_number))
            return phone_number


#Insurance Information
def get_num_of_cars_insured():
    print()
    while True:
        num_of_cars_insured = input("Number of Cars Insured: ").strip()
        #validate positive integer - not max number of cars
        end(num_of_cars_insured) #check if end
        val, errormessage = VAL.validate_positive_integer(num_of_cars_insured, "Number of Cars Insured: ")
        if not val:
            print(errormessage)
        else:
            return int(num_of_cars_insured)
        
        
def get_insurance_optional():
    print()
    while True:
        insurance_optional = input("Optional Insurance (Y/N): ").upper().strip()
        end(insurance_optional) #check if end
        val, errormessage, if_yes = VAL.Y_N(insurance_optional)
        if not val:
            print(errormessage)
        else:
            return if_yes

def get_glass_coverage_optional():
    print()
    while True:
        glass_coverage_optional = input("Optional Glass Coverage (Y/N): ").upper().strip()
        end(glass_coverage_optional) #check if end
        #validate Y/N
        val, errormessage, if_yes = VAL.Y_N(glass_coverage_optional)
        if not val:
            print(errormessage)
        else:
            return if_yes
        
        
def get_loaner_car_coverage_optional():
    print()
    while True:
        loaner_car_coverage_optional = input("Optional Loaner Car Coverage (Y/N): ").upper().strip()
        end(loaner_car_coverage_optional) #check if end
        #validate Y/N
        val, errormessage, if_yes = VAL.Y_N(loaner_car_coverage_optional)
        if not val:
            print(errormessage)
        else:
            return if_yes
        

def get_payment_type():
    print()
    while True:
        print("    Payment Options: input full, monthly, or downpayment\n")
        pay_options = ["FULL", "MONTHLY", "DOWNPAYMENT"]
        payment_type = input("Payment Type: ").upper().strip()
        end(payment_type) #check if end
        #validate list
        val = VAL.validate_list(payment_type, pay_options)
        if not val:
            print("Invalid payment type. Please choose from: FULL, MONTHLY, or DOWNPAYMENT.")
        else:
            return payment_type

def get_downpayment_amount(insurance_total_amount):
    print()
    while True:
        insurance_total_amount = round(insurance_total_amount, 2)
        print(f"Total Insurance Amount: ${insurance_total_amount}\n")
        downpayment_amount = input("Downpayment Amount: ").strip()
        end(downpayment_amount) #check if end
        #validate positive integer
        val, errormessage = VAL.validate_positive_integer(downpayment_amount, "Downpayment Amount")
        if not val:
            print(errormessage)
        else:
            downpayment_amount = float(downpayment_amount)
            if downpayment_amount >= (insurance_total_amount):
                print("Downpayment amount cannot be greater than total insurance amount.")
            
            else:
                return float(downpayment_amount)
        
        
#Data Processing
# File path: ./QAP_04_Intro_to_Python/Const.dat

