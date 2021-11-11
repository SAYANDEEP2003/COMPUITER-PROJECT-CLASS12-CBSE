v,c=0,0
st=input("enter a string: ")
for letter in st:
    if letter.isalpha():
        if letter.lower()=='a' or  letter.lower()=='e' or letter.lower()=='i' or letter.lower()=='o' or letter.lower()=='u':
            v+=1
        else:
            c+=1
print("the no. of vowels are: ",v)
print("the no. of consonents are: ",c)
