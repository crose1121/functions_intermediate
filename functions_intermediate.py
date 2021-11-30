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