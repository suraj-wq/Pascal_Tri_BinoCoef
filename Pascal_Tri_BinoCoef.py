def printPascal(height):
    for i in range(1, height+1):
        for j in range(0, height- i+1):
            print(' ', end='')
#since first element is always 1
        onevalue = 1
        
        for j in range(1, i+1):
            #first value of every line is always 1

            print(' ', onevalue, sep="", end="")


            onevalue = onevalue * (i-j) //j
        print()


height = 5

printPascal(height)
