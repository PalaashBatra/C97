myList1 = [10, 20, 30, 40, 50] 
myList2 = [56, 42, 79, 42, 85, 96, 23]
if 120 not in myList1:
    print("120 is not present")
if 30 in myList1:
    print("30 is present")

print(max(myList1))
print(myList1+myList2)
print(myList2.count(42))
print(myList2[2:7])
myList1.append(60)
print(myList1)
myList2.insert(5,17)
print(myList2)
myList2.pop(3)
print(myList2)
myList1.reverse()
print(myList1)
myList1.clear()
print(myList1)