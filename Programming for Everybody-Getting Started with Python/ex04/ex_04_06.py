# prompt the user for hours and rate per hour using input to compute gross pay. 
# a function of compute pay
def computepay(h,r):
    if h > 40:
        pay = 40 * r + (h - 40) * r * 1.5
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("Error! Please input number")
p = computepay(fh,fr)
print(p)
