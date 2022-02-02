def to_add():
    total = 0
    while True:
        x = input("Enter a number: ")
        if x == "stop":
            break
        else:
            total = total + int(x)
            print(total)

def to_multiply():
    total = 1
    while True:
        x = input("Enter a number: ")
        if x == "stop":
            break
        else:
            total = total * int(x)
            print(total)

def to_choose(x):
    if x == 1:
        return to_add()
    elif x == 2:
        return to_multiply()
