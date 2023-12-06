district = {'Emon': 'Momisingh', 'Tarek': 'Chittagong', 'Zubayer': 'Munsigong', 'Arafat': 'Brammanbaria',
            'Sojib':'Tangail'}

district.update({'Emon': 'Mymensingh'})
print(district)
district.update({'Kawser': 'Sherpur'})
print(district)

district2 = {'Mubarak': 'Noakhali', 'Sadik': 'Dhaka'}

district.update(district2)

print(district)