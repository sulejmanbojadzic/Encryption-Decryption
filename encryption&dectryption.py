import random
print("Only alphanumeric characters and spaces can be used ! ")
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"0","1","2","3","4","5","6","7","8","9"," "]
enclnum=19
spacerandom=random.randint(19,36)
EorD=input("Do you want to encrypt or dectrypt message?\nE is for encrypt and D for decrypt : ").upper()
def Encryption(message):
    codelist=[]
    for i in message:
        encl0=str(letters.index(i)+enclnum)
        encl1=str(letters.index(i)+enclnum-26)
        encl2=str(letters.index(" ")+spacerandom)
        if letters.index(i)<52:
            enccheck=str(i).isupper()
            if enccheck:
                encl1+="x"
                codelist.append(encl1)
            else:
                encl0+="f"
                codelist.append(encl0)
        elif letters.index(i)==62:
            if random.randint(1,2)==1:
                encl2+="f"
                codelist.append(encl2)
            else:
                encl2+="x"
                codelist.append(encl2)
        else:
            if int(letters.index(i))%2==0:
                encl0+="y"
                codelist.append(encl0)
            else:
                encl0+="a"
                codelist.append(encl0)
    code=""
    for j in codelist:
        code+=j
    return code

def Decryption(messagecode): 
    codeletterlist=[]
    slicedcode=[]
    enccode=[]
    b=""
    n=""
    indx=[]
    crackedcode=""
    minilist=[]
    m=0
    c=0
    h=""
    q=0

    encx=len(messagecode)/3
    for i in messagecode:
        j=0
        j+=1
        codeletterlist.append(i)
        messagecode=str(messagecode).replace(str(i),"",1)
        if j%3==0:
            break
    for n in range(len(codeletterlist)):
        c+=1
        minilist.append(codeletterlist[m])
        if c%3==0:
            for x in minilist:
                b+=x
            slicedcode.append(b)
            minilist.clear()
            b=""
        m+=1
    for i in slicedcode:
        n=str(i)
        q=int(n.replace(n[-1],""))
        if q>80:
            indx.append(62)
        elif n[-1]=="x":
            h=n.replace(n[-1],"")
            indx.append(int(h)+26-19)
        else:
            h=n.replace(n[-1],"")
            indx.append(int(h)-19)
            
    for m in indx:
                enccode.append(letters[m])

    for cl in enccode:
        crackedcode+=cl

    return crackedcode
    
        
if EorD=="E":
    input=input("Input your message : ")
    input=input.replace(".","")
    input=input.replace(",","")
    input=input.replace("}","")
    input=input.replace("/","")
    input=input.replace('"',"")
    input=input.replace("(","")
    input=input.replace(")","")
    input=input.replace("[","")
    input=input.replace("]","")
    input=input.replace("!","")
    input=input.replace("?","")
    message=input.replace("{","")
    encr1=Encryption(message)
    print(encr1)

elif EorD=="D":
    input1=input("Input encrypted code,\nEncrypted code can only be from this source : ")
    inpu1t=input1.replace(".","")
    input1=input1.replace(",","")
    input1=input1.replace("}","")
    input1=input1.replace("/","")
    input1=input1.replace('"',"")
    input1=input1.replace("(","")
    input1=input1.replace(")","")
    input1=input1.replace("[","")
    input1=input1.replace("]","")
    input1=input1.replace("!","")
    input1=input1.replace("?","")
    messagecode=input1.replace("{","")
    decr1=Decryption(messagecode)
    print(decr1)



