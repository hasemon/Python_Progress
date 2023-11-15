movie = {
    'title': 'Life of Brain',
    'year': 1979,
    'cast': ['Michel', 'Eric', 'Terry', 'George']
}
movie.update({
    'title': 'Life of Brain',
    'budget': 35000,
    'rating': 8
})

for key, value in movie.items():
    print(key, value)
