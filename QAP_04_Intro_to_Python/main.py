#Description: Python code for The One Stop Insurance Company - allows the user (employee)
            # to enter user information and print an invoice, takes data from insurance.data
            # and Const.dat, parses the data, and appends or replaces the information in those
            # files.
#Name: Jennifer Lyver
#Date: July 16 2024 - July 26, 2024

#Import Libraries
import FormatValues as fv
import utils


#Definitions
CONSTANTS = ["PK_ClaimNumber", "FEE_BASICPREMIUM", "DISCOUNT_ADDITIONALCARS", "FEE_EXTRALIABILITYCOVERAGE", "FEE_GLASSCOVERAGE","FEE_LOANERCAR", "RATE_HST", "FEE_PROCESSING"]
PK_ClaimNumber = 0
FEE_BASICPREMIUM = 0.0
DISCOUNT_ADDITIONALCARS = 0.0
FEE_EXTRALIABILITYCOVERAGE = 0.0
FEE_GLASSCOVERAGE = 0.0
FEE_LOANERCAR = 0.0
RATE_HST = 0.0
FEE_PROCESSING = 0.0
INSURANCE_DOWNPAYMENT_PERIOD = 8 #months

dat_header = ['PK_ClaimNumber', 'Date_Claim', 'cust_firstname', 'cust_lastname', 'cust_streetaddress', 'cust_city', 'cust_provinceabv', 'cust_postal_code', 'cust_phone_number', 'insurance_num_of_cars', 'insurance_optional_insurance', 'insurance_optional_glass_coverage', 'insurance_optional_loaner_car_coverage', 'insurance_payment_type', "insurance_downpayment_amount", 'insurance_total_notax']

first_entry = True #tracks if this is the first entry in the data

def load_constants(file_path, constants_list):
    with open(file_path, "r") as f:
        const_values = f.read().split(", ") #reads file and seperates data in accordance with .csv formatting
        
    if len(const_values) == len(constants_list): #makes sure lists are the same size - error handling
        for i, (constant, value) in enumerate(zip(constants_list, const_values), start=1): #enumerate is used to dynamically change the progress bar to move with the list
            globals()[constant] = float(value) #globals allows the variables to change for the global scope
                #it is important to not put the progress bar in a print statement
                #progress bar increases as the loop increases, needs to be -1 of the size of the list or it will print over 100%
            progress = utils.ProgressBar(iteration=i-1, total=len(CONSTANTS) - 1, prefix='Loading Data ...')
            #print(f"{constant} = {value}") #testing
        if i == len(CONSTANTS): #prints a new line after progress bar (else next print statement is directly after it)
            print("\n")
    else:
        print(f"ERROR: {file_path} does not contain the correct number of entries.")

def save_constants(file_path, constants_list):
    constants_data = []
    with open(file_path, "w") as f:
        for i, variable in enumerate(constants_list, start=1):
            value = globals()[variable]  # Get the value of the variable
            constants_data.append(value)
            #print(f"{variable} = {value}") #testing
            progress = utils.ProgressBar(iteration=i-1, total=len(constants_list) - 1, prefix='Updating Data ...')
        #print(fv.make_csv(constants_data)) #testing
        f.write(fv.make_csv(constants_data))  # Write the data followed by a newline
        print("\n\nConstant Data saved successfully")

def append_data(file_path, data_list):
    customer_data = []
    with open(file_path, "a") as f:
        for i, variable in enumerate(data_list, start=1):
            value = globals()[variable]  # Get the value of the variable
            customer_data.append(value) # Write the value followed by a comma
            #print(f"{variable} = {value}") #testing
            #it is important to not put the progress bar in a print statement
            #progress bar increases as the loop increases, needs to be -1 of the size of the list or it will print over 100%
            progress = utils.ProgressBar(iteration=i-1, total=len(data_list) - 1, prefix='Writing Customer Data ...')
        #print(fv.make_csv(customer_data)) #tesing
        f.write("\n" + fv.make_csv(customer_data))  # Write a newline at the end of each line
        print("\n\nCustomer Data Saved Successfully!")

def print_cust_data (file_path, firstname, lastname):
    with open(file_path, "r") as f:
        data_lines = f.readlines()
        length = len(data_lines)  # Determine size of the file for progress bar

        # Start printing
        print("\n")
        print(fv.center_60("ONE STOP INSURANCE COMPANY - Customer History"))
        print("")
        print(f"    {lastname}, {firstname}\n")
        print(fv.cell_center("Claim Number:") + fv.cell_center("Claim Date:") + fv.cell_center("Insurance Subtotal:"))
        print(fv.center_60("_" * 60))
        
        for line in data_lines:  # Iterate over lines of data
            data = line.strip().split(", ")  # Split the line into a list
            
            if data[2] == firstname and data[3] == lastname:  # If the name matches, print the claim number, claim date, and insurance subtotal
                print(fv.cell_center(data[0]) + fv.cell_center(data[1]) + fv.cell_center(data[-1]))
        
        print(fv.center_60("" * 60))
        print("\n") 

#Main Loop
while True:
    #Get default values 
    print("\n") 
    load_constants("./QAP_04_Intro_to_Python/Const.dat", CONSTANTS)
    Date_Payment = fv.payment_date()
    Date_Claim = fv.current_date()
    PK_ClaimNumber = int(PK_ClaimNumber)+1 #increase the claim number by 1
    
    #Information input
    print()
    print(fv.center_60("ONE STOP INSURANCE COMPANY"))
    
    
    print(fv.center_60("="*60))
    print(fv.center_60("*Input \"END\" at any point to exit program*"))
    print(fv.center_60("**Current customer entry will not be saved on exit**"))
    print("\n")
    if not first_entry: #Little message for new entries
        print("")
        print(fv.center_60("New Entry"))
    #customer information input
    print("     Customer Information")
    print(fv.center_60("-"*60))
    
        
    cust_firstname = utils.get_firstname()
    cust_lastname = utils.get_lastname()
    cust_streetaddress = utils.get_streetaddress()
    cust_city = utils.get_city()
    cust_provinceabv = utils.get_province_abv()
    cust_postal_code = utils.get_postal_code()
    cust_phone_number = fv.phone_dsp(utils.get_phone_number())
    print("\n")
    
    #Insurance information input
    print("    Insurance Information")
    print(fv.center_60("-"*60))
    insurance_num_of_cars = utils.get_num_of_cars_insured()
    insurance_optional_insurance = utils.get_insurance_optional()
    insurance_optional_glass_coverage = utils.get_glass_coverage_optional()
    insurance_optional_loaner_car_coverage = utils.get_loaner_car_coverage_optional()
    
    #calculations
    insurance_premium = FEE_BASICPREMIUM +(FEE_BASICPREMIUM*DISCOUNT_ADDITIONALCARS*(insurance_num_of_cars-1))
    insurance_extracosts = 0.0
    if insurance_optional_insurance:
        insurance_extracosts += FEE_EXTRALIABILITYCOVERAGE
    if insurance_optional_glass_coverage:
        insurance_extracosts += FEE_GLASSCOVERAGE
    if insurance_optional_loaner_car_coverage:
        insurance_extracosts += FEE_LOANERCAR * insurance_num_of_cars
    insurance_total_notax = insurance_premium + insurance_extracosts
    insurance_total_tax = insurance_total_notax * RATE_HST
    insurance_total_amount = insurance_total_tax + insurance_total_notax
    
    #payment information input
    insurance_payment_type = utils.get_payment_type()
    insurance_downpayment_amount = 0.0
    if insurance_payment_type == "DOWNPAYMENT":
        insurance_downpayment_amount = utils.get_downpayment_amount(insurance_total_amount)
        insurance_payment_type = "MONTHLY" #if there is a downpayment, payment type is monthly
    
    #last calculation    
    insurance_monthly_payment = ((insurance_total_tax - insurance_downpayment_amount)+FEE_PROCESSING) / INSURANCE_DOWNPAYMENT_PERIOD
    
    #append insurance information
    append_data("./QAP_04_Intro_to_Python/InsuranceData.dat", dat_header)
    
    #print invoice
    print("\n\n")
    print(fv.center_60("="*60))
    print()
    print(fv.center_60("ONE STOP INSURANCE COMPANY INVOICE"))
    print()
    print(fv.center_60("-"*60))
    print (fv.center_60(f"Claim number: {PK_ClaimNumber} | date: {Date_Claim}"))
    print(fv.cell_center(f"Date: {Date_Claim}"))
    
    #print receipt
    print("\n\n")
    print(fv.center_60("="*60))
    print()
    print(fv.center_60("ONE STOP INSURANCE COMPANY INVOICE"))
    print()
    print(fv.center_60("-"*60))
    print (fv.center_60(f"Claim number: {PK_ClaimNumber} | date: {Date_Claim}"))
    print(fv.cell_center(f"Date: {Date_Claim}")+fv.cell_center(f"Number of cars: {insurance_num_of_cars}")+(fv.cell_center(insurance_payment_type)))
    print()
    print((" "*5)+fv.cell_left("Name:")+fv.cell_left(f"{cust_firstname} + {cust_lastname}"))
    print((" "*5)+fv.cell_left("Street Address:")+fv.cell_left(cust_streetaddress))
    print(fv.cell_left(" "*10)+fv.cell_left(f"{cust_city}, {cust_provinceabv} {cust_postal_code}"))
    print((" "*10)+fv.cell_left("Phone Number:")+fv.cell_left(cust_phone_number))
    print()
    print((" "*10)+fv.cell_left("Basic Premium")+fv.cell_right(fv.moneydsp(FEE_BASICPREMIUM)))
    print((" "*10)+fv.cell_left("Additional Cars:")+fv.cell_right(fv.moneydsp(FEE_BASICPREMIUM*DISCOUNT_ADDITIONALCARS*(insurance_num_of_cars-1))))
    print((" "*10)+fv.cell_left("Insurance Premium:")+fv.cell_righttot(fv.moneydsp(insurance_premium)))
    if insurance_optional_insurance:
        print((" "*10)+fv.cell_left("Extra Liability:")+(fv.cell_right(fv.moneydsp(FEE_EXTRALIABILITYCOVERAGE))))
    if insurance_optional_glass_coverage:
        print((" "*10)+fv.cell_left("Glass Coverage:")+(fv.cell_right(fv.moneydsp(FEE_GLASSCOVERAGE))))
    if insurance_optional_loaner_car_coverage:
        print((" "*10)+fv.cell_left("Loaner Car Coverage:")+fv.cell_right(fv.moneydsp(FEE_PROCESSING*insurance_num_of_cars)))
    print((" "*10)+fv.cell_left("Insurance Add-Ons:")+fv.cell_righttot(fv.moneydsp(insurance_extracosts)))
    print((" "*10)+fv.cell_left("")+fv.cell_center("_"*20))
    print((" "*10)+fv.cell_left("Subtotal:")+fv.cell_right(fv.moneydsp(insurance_total_notax)))
    print((" "*10)+fv.cell_left("HST:")+fv.cell_right(fv.moneydsp(insurance_total_tax)))
    if insurance_downpayment_amount > 0:
        print((" "*10)+fv.cell_left("Down Payment:")+fv.cell_right("-"+fv.moneydsp(insurance_downpayment_amount)))
    print((" "*10)+fv.cell_left("")+fv.cell_center("_"*20))
    print((" "*10)+fv.cell_left("     Total:")+fv.cell_righttot(fv.moneydsp(insurance_total_amount-insurance_downpayment_amount)))
    print("")
    if insurance_payment_type == "MONTHLY":
        print((" "*5)+fv.cell_left("Payment Type:")+fv.cell_left(insurance_payment_type))
        print((" "*5)+fv.cell_left("Next Payment:")+fv.cell_left(Date_Payment))
        print((" "*5)+fv.cell_left("Monthly Payment:")+fv.cell_left(fv.moneydsp(insurance_monthly_payment)))
        
    else:
        print(fv.center_60("PAID IN FULL"))
    print("")
    print(fv.center_60("="*60))
    print
    
    #print previous customer data
    print_cust_data("./QAP_04_Intro_to_Python/InsuranceData.dat", cust_firstname, cust_lastname)
    first_entry = False
    
    #Resave Constants
    save_constants("./QAP_04_Intro_to_Python/Const.dat", CONSTANTS)
    

    
        
