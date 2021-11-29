while True:
        print("1-To upper case")
        print("2-To lower case \n sdad ")
        print("3-To find length")
        print("4-To extract whole string")
        print("5-To chek whether is a digit or not")
        print("6-to enter 2 strings and check whether they are equal or not")
        print("7-to  print  the max character")
        print("8-to print the min chararcter")
        print("9- to searc h for a character in the given string")
        print("10-to reverse the string")
        print("0-exit")
        choice=int(input("ENTER YOUR CHOICE"))
        if choice==1:
                s=input("enter string")
                if s.upper()==s:
                        print("no change required")
                else:
                        print(s.upper())
        elif choice==2:
                s=input("enter a string")
                if s.lower()==s:
                        print("no change required")
                else:
                        print(s.lower())
        elif choice==3:
                s=input("enter string")
                print(len(s))
        elif choice==4:
                s=input("Enter a string")
                print(s[-1])
        elif choice==6:
                s=input("enter a string")
                s1=input("Enter the second string")
                if s==s1:
                        print("both strings equal")
                else:
                        print("not equal")
        elif choice==5:
                s=input("enter a string")
                if s.isdigit :
                        print("it is a digit")
                else:
                        print("it is a string")
        elif choice==7:
                s=input("enter a string")
                print(max(s))
        elif choice==8:
                s=input("enter a string")
                print(min(s))
        elif choice==9:
                s=input("enter a string")
                c=input("enter a character")
                if c in s:
                        print("character present")
                else:
                        print("character missing")
        elif choice==10:
                s=input("enter a string")
                s1=""
                for i in range(len(s)):
                        s1=s[i]+s1
                print("reversed string is  {} ".format(s1))
        elif choice==0:
                print("EXITING PROGRAM")
                break
