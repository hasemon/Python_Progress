movie = {
    'title': 'Life of Pi',
    'year': 1999,
    'cast': ['Jon', 'Erik', 'Micheal', 'Terry']
}

print(movie, 'original dictionary')
print(movie['title'])
print(movie.get('cast'))
print(movie.get('budget', 'budget is not declared'))
movie['title'] = 'Mission Impossible'
print(movie.get('title'))
movie['budget'] = 100000
print(movie)

movie.update({
    'title': 'Hacksaw ridge',
    'year': 2000
})
print(movie)
# deleting
del movie['year']
print(movie)
# popping
cast = movie.pop('cast')
print(cast)
# length
print(len(movie))
# printing keys
print(movie.keys())
# printing values
print(movie.values())
# printing items
print(movie.items())
# looping through
for key, value in movie.items():
    print(key, value)
