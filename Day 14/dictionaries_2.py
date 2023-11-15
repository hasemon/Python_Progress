python = {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'Biccus Diccus': 45}

# membership test

print('arthur' in holy_grail)
if 'arthur' not in python:
    print('He\'s not here')

# adding lists
# Method 1: with update method better for fewer dictionaries
people = {}
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)
# Method 2: with for loop better for more dictionaries
people_1 = {}

for groups in (python, holy_grail, life_of_brian): people_1.update(groups)
print(people_1)

# Method 3: Unpacking

people_2 = {**python, **holy_grail, **life_of_brian}
print(sorted(people_2.items()))
