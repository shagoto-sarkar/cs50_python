#Collection of unique values just like sets in math
#udorderd

#create an empthy set
s = set()

#add values to a set
s.add("shagoto")
s.add("osman")
s.add("himu")
s.add("oni")
s.add(11)
s.add("osman") #doest add duplicate values

#remove a element
s.remove(11)

print(s)
print(f"Total item: {len(s)}") #gives the number of iitem in a set