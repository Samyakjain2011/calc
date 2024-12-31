while True:

    choice=input('''enter what operation you need to use
                1. +
             2. -
             3. *
             4. /
             ''')

    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    if choice=="1":
        print("the ans is",n1+n2)
    elif choice=="2":
        print("ans is", n1-n2)
    elif choice=="3":
        print("the ans is", n1*n2)
    elif choice=="4":
        print("the ans is", n1/n2)