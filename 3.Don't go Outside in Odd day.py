size = int(input("Enter the range :"))
lst = []
for i in range(10):
    value = int(input("enter the element: "))
    lst.append(value)
    print(lst)
odd = 0
even = 0
for i in lst:
        if not i % 2:
            even+=1
        else:
            odd+=1
    	     
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)