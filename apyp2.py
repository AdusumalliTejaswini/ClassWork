names=['Arun','Varun','Kent','Eat','Pot','Net','Peak','Peacock','Zebra','Nato','Toe','Poke','Knife','Peot','Venus','Ant']
letters=['A','K','E','O','T','P','N']
for name in names:
    c=0
    l=list(set(name.upper()))
    for letter in l:
        if letter in letters:
            c+=1
        if c==len(name):
            print(name)