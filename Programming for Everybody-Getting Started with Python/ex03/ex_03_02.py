# base on the ex_03_01.py, add try-except

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, pleas input a number!")
    quit()

if h > 40:
    pay = 40 * r + (h - 40) * 1.5 * r
else :
    pay = h * r
print(pay)
