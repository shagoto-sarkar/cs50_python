#Collection of key-value pairs
#Uses key to look up the value

#Define a dictionary
book = {"a":"apple","b":"ball","c":"cat"}

#add value to a dictionary
book["d"] = "dog"

print(book) #print the dictionary
print(book["c"]) #prints the value using asociated key like "cat" for "c"
for i in book:print(i) #prints the keys using for loop
for i in book: print(book[i]) #Prints the values using for loop