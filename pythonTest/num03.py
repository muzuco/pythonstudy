def printNext(x):
    print("output")
    i = 0;
    for char in x:
        print('No. {0} is {1}'.format(i+1, x[i]))
        i += 1;
friends = ['john', 'pat', 'gary', 'michael']
printNext(friends)
