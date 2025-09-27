#Strings
#A string is a series of characters
#anything inside the single or double qoutes around is a string

name = "fahad hossain babor"
print(name.title()) #Fahad Hossain Babor
print(name.upper()) #FAHAD HOSSAIN BABOR
print(name.lower()) #fahad hossain babor
#the lower method is useful for storing data

#using variable in Strings
first_name = "ada"
last_name ='lovelace'
#f strings -> f stands format 
full_name = f"{first_name} {last_name}"
print(full_name) #ada lovelace
print(f"Hello , {full_name.title()}") #Hello , Ada Lovelace


#Escape characters -> '\t' and '\n'
print("Python")
print('\t Python') #         Python

print('Languages:\nPython\nC\nJavascript')
# Languages:
# Python
# C
# Javascript


print('Languages:\n\tPython\n\tC\n\tJavascript')
# Languages:
#         Python
#         C
#         Javascript

#Stripping White space
lang = '  Python  '
print(lang.strip())  #Python
print(lang.rstrip()) #  Python
print(lang.lstrip()) #Python  




