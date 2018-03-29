# prompts a user for integer numbers until the user enters 'done'. 
# find the max num and min num
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        n = int(num)
    except:
        print("Invalid input")
    
    if n > largest:
        largest = n
    if smallest is None:
        smallest = n
    elif smallest > n:
        smallest = n
    

print("Maximum is", largest)
print("Minimum is", smallest)
