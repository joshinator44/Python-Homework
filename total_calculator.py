print("The Total Calculator program")
print()
print()
while True:
    try:
        price = float(input("Enter price: "))
        break
    except ValueError:
        print("Invalid decimal number. Please try again")
while True:
    try:
        amount = int(input("Enter quantity: "))
        break
    except ValueError:
        print("Invalid Integer. Please try again")
        
       

print("PRICE: ", price)
print("QUANTITY: ", amount)
print("TOTAL: ", price * amount)

    

    

    


