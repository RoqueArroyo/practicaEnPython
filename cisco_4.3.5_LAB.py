# Hacer una función que determine si un año es biciesto y otra que nos diga cuántos dias tiene un mes de tal año

def is_year_leap(year): #Función de año biciesto
    if type(year) == int:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
    else:
        return None

def days_in_month(year, month): #Función de días en mes
    if type(month) == int:    
        if month >= 1 and month <= 12: 
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            res  = days[month - 1]
            if month == 2 and is_year_leap(year):
                res = 29
            return res
        else:
            return None
    else:
        return None

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")