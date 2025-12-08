# 1. append() :- add to end of the list

lst = [1, 2, 3]
lst.append(4)
print(lst)

# 2. insert() → add an item at a specific position 

lst = [10, 20, 30]
lst.insert(1, 15)   # index 1 पर 15 जोड़ेगा
print(lst)

# 3. remove() → a value needs to be removed 

lst = [10, 20, 30, 20]
lst.remove(20)      # पहला 20 हटेगा
print(lst)

# 4. pop() :- removes an item from an index 

lst = [10, 20, 30]
lst.pop(1)          # index 1 हटेगा
print(lst)

# 5. sorts ():- shorts the list in ascending and descending order 

nums = [5, 2, 9, 1]
nums.sort()
print("Ascending =", nums)

nums.sort(reverse=True)
print("Descending =", nums)

# 6. reverse() :- reverse it the order

lst = [1, 2, 3, 4]
lst.reverse()
print(lst)

# 7. count() :- who knows how to count the value

lst = [10, 20, 20, 30]
print(lst.count(20))

# 8. index():- index the value is distributed (batna)

lst = [10, 20, 30]
print(lst.index(20))

# 9. extend appends one list to another list (ak dusre list ko jorta hai)

a = [1, 2, 3]
b = [4, 5]

a.extend(b)
print(a)
