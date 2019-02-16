a=input("Enter the text to be encrypted:")
a=a.lower()
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
temp=[]
temp1=[]
for i in a:
    temp1.append(i)

for i in a:
    temp.append((letters.index(i)+1))
    
cipher=[]
for i in temp:
    cipher.append(letters[i])
for i in cipher:
    print(i,end="")
    


