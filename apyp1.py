s=input("Enter a string:")
vowels=['a','e','i','o','u']
c=0
for i in str(vowels):
    if i in s.lower():
        c+=1
if c==5:
    print("String contains all vowels")
else:
    print("String doesnot contains all vowels")