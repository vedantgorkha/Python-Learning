password= input("ENTER YOUR PASSWORD:-")
length= len(password)
if length < 6:
    print("YOUR PASSWORD IS TOO WEAK")
elif length < 10:
    print("YOUR PASSWORD IS MEDIUM")
else:
    print("YOUR PASSWORD IS STRONG")
print(f"PASSWORD LENGTH IS:- {length}")
