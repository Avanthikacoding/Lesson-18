try:
   num1 = int(input("Enter your first number:"))
   print("The number entered is :" , num1)

except ValueError as ex:
   print("Exception ," , ex) 