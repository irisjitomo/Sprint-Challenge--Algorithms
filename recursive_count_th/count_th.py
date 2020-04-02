'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    # word_list = (list(word))
     # splits string into list of letters
    # TBC
    # Base case that if string equals 'th' return 
    # break 'word' into array of letters to see how many 'th' there are
    if len(word) <= 1:
        return count
    elif word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])

print(count_th('ththth'))
