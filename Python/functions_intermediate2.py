def update_values(x=[], students=[], sports_directory={}, z=[]):
    """
    Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    Change the last_name of the first student from 'Jordan' to 'Bryant'
    In the sports_directory, change 'Messi' to 'Andres'
    Change the value 20 in z to 30
    """
    # For x
    if len(x) > 0:
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j] == 10:
                    x[i][j] = 15

    # For students
    if len(students) > 0:
        for i in range(len(students)):
            if students[i]['last_name'] == 'Jordan':
                students[i]['last_name'] = "Bryant"

    # For sports directory
    if len(sports_directory) > 0:
        for key, values in sports_directory.items():
            for i in range(len(values)):
                if sports_directory[key][i] == 'Messi':
                    sports_directory[key][i] = 'Andres'

    # For z
    if len(z) > 0:
        for i in range(len(z)):
            for key, value in z[i].items():
                if value == 20:
                    z[i][key] = 30


x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}


]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


update_values(x=x, students=students, sports_directory=sports_directory, z=z)
print("x:", x)
print("students:", students)
print("sports_directory:", sports_directory)
print("Z:", z)

print("================")
print("iterate dictionary 1")


def iterateDictionary1(some_list):
    """
    given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
    """
    for vals in some_list:
        count = len(vals)
        for key, value in vals.items():
            endchar = ', '
            if count == 1:
                endchar = '\n'
            print(f"{key} - {value}", end=endchar)
            count -= 1


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary1(students)


def interateDictionary2(key_name, some_list):
    """
    given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
    """
    for vals in some_list:
        print(vals[key_name])


print("===================")
print("iterate dictionary 2 - first name")
interateDictionary2('first_name', students)
print("===================")
print("iterate dictionary 2 - last name")
interateDictionary2('last_name', students)

print("===================")
print("iterate dictionary with list")


def printInfo(some_dict):
    for key, value in some_dict.items():
        print("{0} {1}".format(len(value), key.upper()))
        for val in value:
            print(val)
        print()


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
