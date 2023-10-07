# Create a list of characters using list comprehension
char_list = [char for char in "linuxhint"]
print(char_list)

# Define a tuple of websites
websites = ("google.com", "yahoo.com", "ask.com", "bing.com")

# Create a list from tuple using list comprehension
site_list = [site for site in websites]
print(site_list)


text = "Learn Python Programming"

# Slice using one parameter
sliceObj = slice(5)
print(text[sliceObj])

# Slice using two parameter
sliceObj = slice(6, 12)
print(text[sliceObj])

# Slice using three parameter
sliceObj = slice(6, 25, 5)
print(text[sliceObj])