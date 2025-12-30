num= int(input("Enter a number: "))
if num<=1:
    print(f"{num} is neither prime nor composite.")
else:
    for i in range(2,num):
        if num % i ==0:
            print(" composite.")
            break
        else:
            print(" prime.")