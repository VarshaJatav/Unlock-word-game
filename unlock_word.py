import random
l1=["hair","clock","bag","school","water","food","blanket","page","book","pen","pencil","app","hand","flower","car","bike","home"]
l2=["It is somewhat which you can never count? ","This is somewhat which never stops? ","This is the adda of your things when you are on a trip or to college/schhol? ","This is somewhat which is mainly known for education and you don't like when you have, but miss it afterwards? ","This is somewhat which is solid,liquid and gas and can never be washed? ","This is what you have everyday and it is so essential for our living? ","This is somewhat you like when it is winter but you hate it in summer? ","This is somewhat which is 2d and has a lot of use? ","This is somewhat which so knowledgable and is said as friends of human? ","This is somewhat which is powerful than a sword? ","This is somewhat which becomes shorter and shorter day by day with its age? ","This is somewhat which everyone use and is software in our phone? ","It is somewhat which everyone have two and is connected with our body?  ","It is somewhat which have colours and smell ?","This is a vehicle? ","It is a vehicle? ","It is a place where you get sukooon? "]
str1=random.choice(l1)
for i in l1:
    if str1==i:
        abc=l1.index(i)
# str2=str1
l1=[]
for i in str1:
    l1.append("*")
attempt=len(str1)
print("\n\n\n\n","".join(l1))
print("\n\nHINT:   ",l2[abc],"\n\n\n")
for i in range(0,attempt*2):
    print("Attempt:  ",i+1)
    x=input("Enter a letter:  ")
    y=x[0]
    if y in str1:
        for j in range(attempt):
            if y==str1[j]:
                l1[j]=str1[j]           
    str12="".join(l1)
    print(str12)
    if str1==str12:
        break
if str1==str12:
    print("\n\n\n\t\t\t*Congo, You won*\n\n\n")
else:
    print("\n\n\n\n\n\t\tBetter luck next time\n\n\n")