# For loops - Exercise Party invitation
# You're having a party and want to invite your friends you want the print-out invitations for each friend using for loops
# The names are in two lists, 'names' and 'names1' You also need to add two extra names to the list using an input
# box, when you run the code Printout one invitation to each friend per line
# Names should be properly capitalized Example of printout John Gicasa! You are invited to tho panty on satardoy ric Idle!
# Yon are invited to the party on absurdity Hint: you may need two (for) loops to solve this exercise.


names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

msg = 'You are invited to my party! on Friday'
names.extend(names1)

for index in range(2):
    names.append(input('Enter a friends name: '))

for friend in names:
    print(f'Hey {friend.title()}! {msg}')
