def reverse(x):
    changeTuple=tuple(x)
    reverseTuple=changeTuple[::-1]
    print(''.join(reverseTuple))

test = "this is test string"
reverse(test)
