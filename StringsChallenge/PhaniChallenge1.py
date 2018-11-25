//Function for comparing two strings
def compare(x,y):
    st1=""
    st2=""
    ques="?"
    p=0
    q=0
    s=0
    for i in x:
        if i.isdigit():
           st1=st1+ques*int(i)
           continue
        st1+=i
        p=p+1

    
    for i in y:
        if i.isdigit():
           st2=st2+ques*int(i)
           continue
        st2+=i
        q=q+1

    if(len(st1)==len(st2)):
        for i in range(len(st2)):
            if (st1[i]==ques or st2[i]==ques):
                continue
            else:
                if(st1[i]==st2[i]):
                    s=s+1
                    continue
                    
                else:
                    print("Strings are not same")
        
        if(s<=p or s<=q):
                print("Strings are same")


    else:
        print("strings are not same")
    


x=input("Enter String1:")
y=input("Enter String2:")
compare(x,y)
