# Update Values in Dictionaries and Lists

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 

def change_x():
    x[1][0] = 15
    return x

print(change_x())

# Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def change_name():
    students[0]['last_name'] = 'Bryant'
    return students

change_name()
print(students)


# In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def change_sports():
    sports_directory['soccer'][0] = 'Andres'
    return sports_directory

change_sports()
print(sports_directory)

# Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]

def change_z():
    z[0]['y'] = 30
    return z

change_z()
print(z)


# Iterate Through a List of Dictionaries

# Create a function iterate_cictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'Jake', 'last_name' : 'Smith', 'middle_name': 'Jack'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def iterate_dictionary(students):
#     for student in students:
#             print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

# iterate_dictionary(students)

#ALTERNATIVELY:

def iterate_dictionary(students):
    for x in range(len(students)):
        row = ""
        for key,value in students[x].items():
            row += f"{key} - {value} "
        print(row)

iterate_dictionary(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# Get Values From a List of Dictionaries


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'Jake', 'last_name' : 'Smith', 'middle_name': 'Jack'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

def iterateDictionary2(key, students):
    for x in range(len(students)):
        row = ""
        for value in students[x][key]:
            row+= value
        print(row)

iterateDictionary2('first_name',students)

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key, students):
    for x in range(len(students)):
        row = ""
        for value in students[x][key]:
            row+= value
        print(row)

iterateDictionary2('last_name',students)

# Iterate Through a Dictionary with List Values

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, print the name of each key along with the size of its list, and then print the associated values within each key's list. For example:

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

#This last one literally took me hours to figure out lol.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        num_locations = len(some_dict[key])
        print(f"\nThere are {num_locations} {key}\n")
        for value in some_dict[key]:
            print(value)
        

printInfo(dojo)




