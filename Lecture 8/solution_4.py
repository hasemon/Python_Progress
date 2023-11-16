# 4. Write a Python script that takes input from the user and displays that input back in upper and lower cases based
# on selection.

def caseChange(inputStr, selection):
    if selection == 'uppercase':
        return f'Uppercase: {inputStr.upper()}'
    elif selection == 'lowercase':
        return f'Lowercase : {inputStr.lower()}'
    else:
        return 'Selection invalid'


inStr = input('Enter a string: ')
inSelection = input('Enter a selection: ')

result = caseChange(inStr, inSelection)
print(result)
