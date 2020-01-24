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
    if word == 'th':
        count = count + 1
    elif word == '':
        return count
    def helper_function(word, count):
        if 'th' in word:
            count = count + 1
    helper_function(word, count)
    return count

print(count_th('ththth'))
