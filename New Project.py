ans = "yes"

while ans!="no":
    try:
        Age= int(input("Enter your age:"))
    except:
        print("please enter a number")
        continue
    if Age >= 18:
        print("Party Time")
    elif Age >16:
        print("you can watch")
    else:
        print("you are not eligible")
        print("rukja bhai")
    ans = input("do you want to continue?\n")