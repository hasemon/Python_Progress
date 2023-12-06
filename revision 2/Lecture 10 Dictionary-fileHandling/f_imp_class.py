district = {'Emon': 'Momisingh', 'Tarek': 'Chittagong', 'Zubayer': 'Munsigong', 'Arafat': 'Brammanbaria',
            'Sojib': 'Tangail'}


copyDistrict = district.copy()
district.get('Emon')
print(district.get('Emon'))
print(district.items())
print(district.keys())
print(district.values())
print(district.pop('Tarek'))
print(district.popitem())
print(district)
district.update({'Emon': 'Mymensingh'})
district.update({'Pappu': 'Barisal'})
print(district)
district.update(copyDistrict)

print(district)