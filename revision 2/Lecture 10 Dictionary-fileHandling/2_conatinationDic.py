# 2. Write a Python script to concatenate the following dictionaries to create a new one.

carDict = {"brand": "Ford", "model": "Mustang", "year": 1964}

dealerDict = {'Dhaka': 'Hasan', 'Sylhet': 'Karim', 'Cumilla': 'Rahima'}
carDict.update(dealerDict)

print(carDict)