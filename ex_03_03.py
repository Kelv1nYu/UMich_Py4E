score = input("Enter Score: ")
try:
    fs = float(score)
except:
    print("Error! Please input a number")

if fs > 1.0 or fs < 0:
    print("Error! Please input a number between 0.0 and 1.0")
    quit()
else:
    if fs >= 0.9:
        print("A")
    elif fs >= 0.8:
        print("B")
    elif fs >= 0.7:
        print("C")
    elif fs >= 0.6:
        print("D")
    else:
        print("F")
