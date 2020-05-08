for i in range(1,4) :
    '''
    type(anything)
    will give its type

    st1 + str2 will concatenate the strings

    operator precedence
    parenthesis
    power
    division Multipication
    addition substraction
    left to right

    max() and min()

    for i in range(5) :
        print(i)

    def add(a,b):
        c = a+b
        return c

    def greet() :
        return "Hello"
    print(greet(),"name/pradhuman")

    continue and break

    try:
        pass
    except Exception as e:
        raise
    '''
    print ("hello")

def comparenum() :
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
