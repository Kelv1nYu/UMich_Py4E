# prompt the user for hours and rate per hour using input to compute gross pay. 
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
# check the hour
if h > 40:
    pay = 40 * r + (h - 40) * 1.5 * r
else :
    pay = h * r
print(pay)
