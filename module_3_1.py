calls = 0

def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    a =len(string)
    b = string.upper()
    c = string.lower()
    return (a,b,c)
def is_contains (string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        a = False
        if string.lower() == list_to_search[i].lower():
            a = True
    return a

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'uRBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)