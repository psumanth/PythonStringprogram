def expand_input_string(p1,st,z):
    for i in p1:
        if i.isdigit():
            st=st+int(i)*ques
            continue
        st=st+i
        z=z+1
    return
        
def comparing_strings(st1,st2,s):
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
    return

st1=""
st2=""
ques="?"
p=0
q=0
s=0
x=input("Enter string1:")
y=input("Enter string2:")
expand_input_string(x,st1,p)
expand_input_string(y,st2,q)
comparing_strings(st1,st2,s)