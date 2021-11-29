while True:
    choice = int((input('''
    Press 1 to convert string to uppercase
    Press 2 to convert string to lowercase
    Press 3 to check if 'a' is in the string
    Press 4 to reverse string
    Press 5 to check count of 'a' in string
    Press 6 to slice string from 0 to 5th character
    Press 7 to check if string is a digit
    Press 8 to split a string
    Press 9 to the index of 'a' in the string
    Press 10 to concatenate strings
    Press 0 to exit
    ''')))

    if choice==1:
        s = input("Enter your string\n")
        print(s.upper())
    elif choice==2:
        s = input("Enter your string\n")
        print(s.lower())
    elif choice==3:
        s = input("Enter your string\n")
        print('a' in s)
    elif choice==4:
        s = input("Enter your string\n")
        print(s[::-1])
    elif choice==5:
        s = input("Enter your string\n")
        print(s.count('a'))
    elif choice==6:
        s = input("Enter your string\n")
        print(s[0:5])
    elif choice==7:
        s = input("Enter your string\n")
        print(s.isdigit())
    elif choice==8:
        s = input("Enter your string\n")
        print(s.split())
    elif choice==9:
        s = input("Enter your string\n")
        print(s.index('a'))
    elif choice==10:
        s1 = input("Enter string 1\n")
        s2 = input("Enter String 2\n")
        print(s1 + s2)
    elif choice==0:
        print('Exiting')
        break
    else:
        print("Invalid option entered")