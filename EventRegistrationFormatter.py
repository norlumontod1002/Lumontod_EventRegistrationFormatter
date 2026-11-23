# Version 1

print("STUDENT EVENT REGISTRATION")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

print("\nRegistration Summary")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Section:", section)
print("Event:", event_name)
print("Event Year:", year)
print("Event Month:", month)
print("Event Day:", day)

# Version 2

print("\nSTUDENT EVENT REGISTRATION")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

print("\nRegistration Summary")
print("Name:", first_name + " " + last_name)
print("Name Code:", (first_name + " " + last_name).upper())
print("Section:", section)
print("Event:", event_name)

# Version 3

from datetime import datetime

print("\nSTUDENT EVENT REGISTRATION")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

full_name = first_name + " " + last_name

event_date = datetime(year, month, day)
formatted_date = f"{event_date.strftime('%B')} {day}, {year}"

print("\nStudent Event Registration Summary")
print("\nName:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", formatted_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")

print("\nRegistration record created successfully.")
