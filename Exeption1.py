x = input("Enter a first number        :")
y = input("Enter a second number       :")
try:
    result=(int(x)/int(y))
except ZeroDivisionError:
    print ("Sorry you cannot divide by Zero")
except ValueError:
    print("Please use values 0 - 9 (Except as a divisor !)")
except Exception:
    print("An unknown error occured")
else:
    print (result)
