# Strings
word = "amazing"

# slicing
print(word[0:5])

# length of the string
str = "aina"
print(len(str))

# returns true if string ends with "na"
print(str.endswith("na"))

# counts the total number of occurences of any char (case sensitive)
print(str.count("a"))

# capitalize the first char of a string
str = "harry"
cap_string = str.capitalize()
print(cap_string)

# find the index of the string we are looking for
index = str.find("rr")
print(index)

# replacing chars
str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string)

# escape sequence chars
print("this is the new line \n", " this is the tab \t", "this is single quote \'")

name = input("Enter Your Name: ")
print("Good afternoon", name)

print("Dear ", name,",", "\nYou are selected!", "\nmay 18th, 2025")

# detecting double spaces in a string
str = "joe  likes food"
index = str.find("  ")
print(index)

# replacing string with double space to just one space
replace = str.replace("  ", " ")
print(replace)