# ! ------> common funcions for  list

l1 = [6, 7, 8, 9, 0]
# print(len(l1))

print(max(l1))
# print(min(l1))

l1 = [6, 8, 9, "p", "u"]
print(max(l1)) # ---> eeror coz its a combination pf list and string
print(max(l1)) # ---> eeror coz its a combination pf list and string

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# print(min(l1)) # -5

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
# print(l1.index(9))

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count() --> how many num of tims an element is repeated
# print(l1.count(6))

#! some function which is specifically used for list

# Toadd element inside list
# ? insert() --> to add elementa at specific index position
l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1.insert(2, "cars")
print(l1)# ? to delete element from list
l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# pop() --> last element will be deleted
l1.pop()
print(l1)


pop(index_value) --> used to delete element at specific index
l1.pop(4) is index value
print(l1)

# remove(element) --> used to delete element directly
# l1.remove(8.89)
# print(l1)


#* clear() --> to complete delete all element in list
# l1.clear
# print(l1)

# del -> to delete the list
# del l1 # or del(l1)
# print(l1)

# ? ---> join 2 lists


l1 = [9, 0, 8]
l2 = ["p", "o", "t", 34]
print(l1+l2)
#* deep copy --> used to copy the list with nested list
import copy
l1 = [8, 9, 0,[5, 6],[3, 2, 1]]
print(l1[-1][1]) --> to index nested list

l2 = copy.deepcopy(l1)
l1[-1].append(890)
print(l1)
print(l2)
# ? sort --> arrange elements in list in ascending or descending order
l1 = [9, 7, 45, 0, -6, 5, 12]
l1.sort() # to arrange in ascending order
print(l1)


l1.sort
(reverse=True) # to sort in  descending order
print(l1)


l1 = ['z', 'i', '0', 'p', 9]
.sort()
print(l1) # --> error

list constructor
list() --> to conver other collction datatype to list
l3 = ((8, 9, 0))
print(list(l3))

l4 = (8, 9)
print(list(l4))

# ! ---> nested list
l1 = [8, 9, [0, 8, 7,], ["p", "o", "y"], [8, "t"]]
# print9l1[-2][1]) # --> 0

print(l1[1:4])
print(l1[1:-1])

# ? to delete "t" from l1
(l1[-1].remove('t'))
print(l1)

# ? combine these ["p", "o", 'y'], [8, 't'] lists in l1 to ["p", "o", 'y',8, 't']



