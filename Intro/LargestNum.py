largest = None
smallest = None
x = 0
while True:
    num = input('Enter a number: ')
    if num == 'done' :
        break
    try :
        nval = int(num)
    except :
        print('Invalid input')
        continue
    if x == 0 :
        smallest = nval
    x = x+1
    if largest ==  None :
        largest = nval
    if smallest == None :
        smallest = nval
    if largest < nval :
        largest = nval
    if smallest > nval :
        smallest = nval
print("Maximum is", largest)
print("Minimum is", smallest)
