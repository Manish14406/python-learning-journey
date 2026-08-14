def convert(C):
    F = (9/5)*C +32 
    return F

C = float(input("Enter celcius : "))
print(f"Fahrenheit is {convert(C)}")