python = {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'Biccus Diccus': 45}
# membership
if 'Arthur' in holy_grail:
    print('Arthur is found')
else:
    print('Arthur is not found')

# concatenating two lists
# method 1 update()
python.update(holy_grail)
print(python)

# method 2 comprehension

for group in (python, holy_grail, life_of_brian): python.update(group)
print(python.items())

# method 3 unpacking
print({**python, **holy_grail, **life_of_brian})
