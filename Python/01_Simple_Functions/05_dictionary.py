string = 'Hi, DSAL is here and practicing Python for fun.'
counter = dict()
for letter in string:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

for this_one in list(counter.keys()):
    print('%s appeared %s items' %(this_one, counter[this_one]))



"""
This code performs a frequency analysis of characters in a given string.
It iterates over each character, counts its occurrences using a dictionary,
and then prints the frequency of each character in the string.
"""