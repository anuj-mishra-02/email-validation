Email = input("Enter your email : ")
k,j,l =0,0,0
if len(Email)>=6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count('@')==1):
            if (Email[-4]=='.') ^ (Email[-3]=='.'):
                for i in Email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        l=1
                if j==1 or k==1 or l==1 :
                    print("Incorrect mail")
                else:
                    print("It is a correct mail")
            else:
                print("Positioning of . is incorrect")

        else:
            print("@ should contains only once")
        pass
    else:
        print("Email should contains alphabets")
else:
    print("Email should be greater then 6")