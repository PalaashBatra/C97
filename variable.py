myname="Palaash Batra"
myage=13
print(myname,myage)
print(type(myage))

friendlist=["Moksh","Manan","Vansh"]
print(friendlist[2])

pocket=int(input("Enter the amount of Pocket Money you get: "))
if(pocket<500):
    print("You don't have enough money")
elif(500<pocket<1000):
    print("You have enough money")
else:
    print("You are RICH")

for friend in friendlist:
    print(friend)

