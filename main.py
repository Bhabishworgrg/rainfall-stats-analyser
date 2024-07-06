def check_exception(uInput):
    """Checks any exceptions that might occur."""

    try:
        value = int(uInput[:-2])

        if uInput[-2:] != "mm":
            raise Exception 
    except ValueError:
        print("Please enter valid data")
        
        return False,
    except Exception:
        print("Please provide data in 'mm' units")

        return False,
    else:
        return True, value

def calculate_average(data):
    """Calculates average."""

    total = 0
    
    for i in data:
        total += i
    
    avg = total / 12
    return round(avg, 2)

def calculate_sd(data, avg):
    """Calculates standard deviation."""
    
    summation = 0
    
    for i in data:
        summation += (i - avg) ** 2
    
    sd = (summation / 11) ** (1/2)    
    return round(sd, 2)

if __name__ == "__main__":
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rainfall = []

    for month in months:
        while True:
            userInput = input(f"Enter rainfall for {month}: ")
            
            if check_exception(userInput)[0]:
                break
        
        rainfall.append(check_exception(userInput)[1])

    maxRain = max(rainfall)
    minRain = min(rainfall)
    average = calculate_average(rainfall)
    stdDeviation = calculate_sd(rainfall, average)

    print(f"""
Max Rainfall: {maxRain}mm in {months[rainfall.index(maxRain)]}
Min Rainfall: {minRain}mm in {months[rainfall.index(minRain)]}

Average:            {round(average, 2)}mm
Standard Deviation: {round(stdDeviation, 2)}mm
    """)
