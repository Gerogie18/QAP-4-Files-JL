#Description: Formatting library referened by the main python script.
#Name: Jennifer Lyver
#Date: July 17, 2024

#Import Libraries
from datetime import datetime
from datetime import date


def moneydsp(money):
    moneyDSP = "${:,.2f}".format(money) 
    return moneyDSP

def phone_dsp(phone_number):
    phone_number = phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]
    return phone_number

def center_60(string):
    return "{:^60}".format(string)

def cell_center(string):
    return "{:^20}".format(string)

def cell_left(string):
    return "{:<20}".format(string)

def cell_righttot(string):
    return "{:>20}".format(string)

def cell_right(string):
    return "{:>12}".format(string)

def make_csv(list):
    return ", ".join(str(item) for item in list)

def current_date():
    current_date = date.today()
    current_date_str = current_date.strftime("%Y-%m-%d")
    return current_date_str

def payment_date():
    current_year = datetime.now().year
    current_month = datetime.now().month
    payment_day = 1
    if current_month == 12:
        payment_month = 1
        payment_year = current_year + 1
    else:
        payment_month = current_month + 1
        payment_year = current_year
    payment_date = date(payment_year, payment_month, payment_day)
    payment_date_str = payment_date.strftime("%Y-%m-%d")
    return payment_date_str


