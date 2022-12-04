#Program to illustrate startswith and endswith methods
#print("This program checks whether the given string starts with 'Python' and ends with 'programming'")
str = input("str: ")
if (str.startswith('Python') and str.endswith('programming')):
	print("valid")
else:
	print("invalid")
print("character with min val:", min(str))
print("character with max val:", max(str))


#Program to find the number of times a substring appears in a given string
str = input("str1: " )
sstr = input("str2: ")
print("count:", str.count(sstr))

