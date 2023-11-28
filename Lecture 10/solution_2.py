# 2. Write a Python script to concatenate the following dictionaries to create a new one.

python = {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'icons': 45}

# method 1 concatenation update
python.update(holy_grail)
python.update(life_of_brian)
print(python)

# method 2 concatenation comprehension
for group in (python, holy_grail, life_of_brian):
    python.update(group)
print(python)

# method 3 concatenation unpacking
print({**python, **holy_grail, **life_of_brian})
