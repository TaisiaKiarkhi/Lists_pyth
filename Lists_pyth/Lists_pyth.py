

names = ["Alice", "Eric", "Alan", "Paul", "Willy", "Tom"]
random_data = [2, "potato", False]

print(names) #prints the whole list with all the name inside it
print(names[1]) #prints the second name inside the list
print(names[-1]) #starts indexis from the end of the list (prints the last name in our case)
print(names[-3])
print(names[1:]) #prints all the names starting with the name at index 1
print(names[2:5]) #prints names from index 2 to 4 (5 is nt inlcuded)

names[1] = "Stephan" #the second name will be updated to Stephan
names.append(str("Sally")) # adds a value to the list, similar to push_back in c++
names.extend(random_data) #extends the list (merges two lists togethes)
names.insert(2, "Milly") #inserts a value into the given index, the other values will be shifted
print(names)
names.remove("potato")
print(names)
names.pop() #similar to c++, pop the last variable from the list

names.clear() #removes all of the variables
names.append(2)
names.append(2)
names.append(2)

print(names.index(2)) #print the index where the given variable is placed
print(names.count(2)) #count how many times a variable appears inside the list

names.sort() #sorts the list in ascending order
names.reverse() #sorts nut in the reverse order

names_2 = names.copy()
print(names_2)