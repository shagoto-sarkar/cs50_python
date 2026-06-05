#Lists are sequence of mutable value
#Items are not unique
#can add and remove Items

names= ["shagoto","oni","himu","osman","noman"] #To create a list

#print(names[0]) #to view first item
#print(names[-1]) #to view last item

names.append("oni") #To add a new name in list
names.insert(3,"istiak") #To add name at a specific index
names.remove("oni") #To remove item "x"
names.sort() #To sort a list
names.reverse() #to reverse the list

length = len(names) #to find the number of items in a list
freq_oni = int(names.count("oni")) #.count(x) for frequency of a item x

for friend in names: print(friend) #to go through the list and print all names

print(f"There are {len(names)} names in the list.") 
print(f"The last name of the list is {names[-1]}")
print(f"The name oni apears {freq_oni} time in the list")