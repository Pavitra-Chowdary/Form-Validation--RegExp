import re

# Function to convert month number to month name
def get_month_name(month_number):
    months = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April',
        '05': 'May', '06': 'June', '07': 'July', '08': 'August',
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    return months.get(month_number, "Invalid Month")

# Name
while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    text = input("Enter Your Name: ")
    res = pattern.fullmatch(text)
    if res is not None:
        name = res.group()
        break
    else:
        print("Enter Name in Correct Format !")

# Date of Birth (in DD-MM-YYYY format)
while True:
    pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    text = input("Enter Date of Birth: ")
    res = pattern.fullmatch(text)
    if res is not None:
        day, month, year = res.groups()
        month_name = get_month_name(month)
        dob = f"Date: {day}, Month: {month_name}, Year: {year}"
        break
    else:
        print("Enter DOB in Correct Format !")

# Email id
while True:
    pattern = re.compile(r'[a-z0-9]+@gmail.com\Z')
    text = input("Enter Email id: ")
    res = pattern.fullmatch(text)
    if res is not None:
        mailid = res.group()
        break
    else:
        print("Enter Mail id in correct format !")

# Mobile Number (in xxx-xxx-xxxx format)
while True:
    pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    text = input("Enter Mobile Number: ")
    res = pattern.fullmatch(text)
    if res is not None:
        mobile = res.group()
        break
    else:
        print("Enter Mobile Number in correct Format !")

# Remove hyphens from the mobile number for display
mobile_display = mobile.replace("-", "")

# Display the details
print(f"Name: {name}")
print(f"DOB: {dob}")
print(f"Mail id: {mailid}")
print(f"Mobile: {mobile_display}")
