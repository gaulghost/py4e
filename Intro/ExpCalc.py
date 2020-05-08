print("which mathematical expression would you like to preform")
print("power / 1 / '**'")
print("division / 2 / '/'")
print("multipication / 3 / '*'")
print("substraction / 4 / '-'")
print("addition / 5 / '+'")
print("remainder / 6 / '%' \n")
x = None
y = None
operand = None
m = 0
while True:
    try :
        if m == 0 :
            x = float(input("Enter the first num \n"))
            y = float(input("Enter the second num \n"))
        else :
            x = output
            y = float(input("Enter the second num \n"))
    except :
        print("You have entered wrong input")
        exit()
    operand = input("Operation you want to preform \n")
    if operand.lower() == "power" or operand == "1" or operand == "**" :
        output = x ** y
    elif operand.lower() == "division" or operand == "2" or operand == "/":
        output = x / y
    elif operand.lower() == "multipication" or operand == "3" or operand == "*":
        output = x * y
    elif operand.lower() == "substraction" or operand == "4" or operand == "-":
        output = x - y
    elif operand.lower() == "addition" or operand == "5" or operand == "+":
        output = x + y
    elif operand.lower() == "remainder" or operand == "6" or operand == "%":
        output = x % y
    print("Output is : ",output)
    m = m + 1
    k = input("Want to further calculate on the output? If no type done else press any key to continue\n")
    if k.lower() == "done" :
        break
print("Your final output is :",output)
