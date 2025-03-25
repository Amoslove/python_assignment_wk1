#my week 2 python assgnment 
#question one, creat an empty list called my_list
my_list = []

#question 2 Apppend the following eleemts 10,20,30,40
my_list.extend([10,20,30,40,])

#quedtion 3 insert the value 15 at the second position
my_list.insert(1, 15)

#question 4 extend my_list with another list [50,60,70]
my_list.extend([50,60,70])

# question 5 emove the last element from the my_list
my_list.pop()

#qustion 6 sort my_list in ascending order
my_list.sort()

#question 7 find and print the index of the value 30
index_30 = my_list.index(30)
print(f"index of 30: {index_30}")

print("final my_list:", my_list)