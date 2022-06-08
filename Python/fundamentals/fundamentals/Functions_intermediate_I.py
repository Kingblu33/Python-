x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["lastname"] = "Brayant"
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'][0] = "Andres"
print (sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print (z)

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for plz in some_list:
        print(plz)
    return some_list

iterateDictionary(students)

def iterateDictionary2(Key_name, somelist):
    for k in somelist:
        print (k[Key_name])
    return k[Key_name]

iterateDictionary2('first_name',students)
iterateDictionary2('last_name', students)

dojo = {
        'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict['locations']),"Locations")
    for location in some_dict['locations']:
        print(location)

    print(len(some_dict['instructors']), "Instructors")

    for name in some_dict['instructors']:

        print(name)

printInfo(dojo)
