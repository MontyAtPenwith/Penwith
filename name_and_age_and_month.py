# get name and age
name = input("What is your name?: ")
age = int(input(f"How old are you {name}?: "))
month = input("What month were you born in?: ")
MONTH = 9


def calc_month(month) -> int:
    
    month = month.upper()
    
    if month == "1" or month == "JANUARY" or month == "JAN":
        month = 1
        
    elif month == "2" or month == "FEBRUARY":
        month = 2
        
    elif month == "3" or month == "MARCH":
        month = 3
        
    elif month == "4" or month == "APRIL":
        month = 4
        
    elif month == "5" or month == "MAY":
        month = 5
        
    elif month == "6" or month == "JUNE":
        month = 6
            
    elif month == "7" or month == "JULY":
        month = 7
            
    elif month == "8" or month == "AUGUST":
        month = 8
            
    elif month == "9" or month == "SEPTEMBER":
        month = 9
            
    elif month == "10" or month == "OCTOBER":
        month = 10
            
    elif month == "11" or month == "NOVEMBER":
        month = 11
            
    elif month == "12" or month == "DECEMBER":
        month = 12
            
    else:
        month = 0
    
    return month
    
    



# calculate
if age < 0: 
    print("You arent old enough!")
    
birth_year = 2026 - age
age_months = calc_month(month)
age_in_months = age_months + (age * 12)
#name = name.upper()

# print
print(f"\nYour name is {name}!")
print(f"You are {age} years old!")
print(f"You were born in {birth_year}!")
print(f"You have been alive for {age_in_months} months!")

