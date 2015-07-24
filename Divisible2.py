__author__ = 'Mattia'
'''Create a function isDivisible(n,...) that checks if the first agrument n is divisible by all other arguments
(return true if no other arguments)'''

def isDivisible(*arg):
    cont = 0
    for i in range(len(arg)):
        if (arg[0]%arg[i] == 0):
            cont += 1
    if(cont == len(arg)):
        print True
        return True
    else:
        print False
        return False

isDivisible(4,2,4)
