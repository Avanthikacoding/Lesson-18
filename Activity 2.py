try:
    num1,num2 = eval(input("Enter 2 numbers witha comma in between. "))
    print(num1/num2)

except ZeroDivisionError:
    print("Numbers can not be divided by zero! It is not possible! ZeroDivisionError found!")
except SyntaxError:
    print("You are supposed to seperate the numbers by a comma! SyntaxError found! \n I won't be able to excute this without the comma!")
except:
    print("Wrong input! You are supposed to provide numbers! Error found!")

finally:
    print("This answer is not copyright! Computer has figured it out by itself! ")