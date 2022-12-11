email = input("Enter your EMail : ")#g@g.in
k=0
j=0
d=0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == "." ) ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i == i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1:
                    print("Wrong Email : contains space")
                if j == 1:
                    print("Wrong Email : contains Uppercase letter")
                if d == 1:
                    print("Wrong Email : contains invalid special char")
                else:
                    print("Correct EMail")
            else:
                print("Wrong EMail : . position is not correct")
        else:
            print("Wrong Email : @ more than one or not present")
    else:
        print("Wrong EMail : start char is not Alpha")
else:
    print("Wrong Email : less than 6 char")