#Distanse converter using input and output

name = input('Enter name: ')
distance_km = float(input('Enter Display is KM: '))
distance_mile = distance_km/1.609

print(f'Hi {name.upper()} your distance is {distance_km} km or {round(distance_mile,2)} miles')
