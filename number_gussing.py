import random
secret = random.randint(1,20)
while True:
    guess =int(input("GUESS A NUMBER BETWEEN 1 TO 20:-"))
    if guess > secret:
        print("TOO HIGH")
    elif guess < secret:
        print("TOO LOW")
    else:
     print("YESS CORRECT GUESS")
    break
