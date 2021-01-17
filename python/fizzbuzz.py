counter = 0
while counter < 100:
    counter += 1
    if(counter % 3 == 0):
        if(counter % 5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif(counter % 5 == 0):
        if(counter % 3 == 0):
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(counter)
    