'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, index = 1):
    if len(word) == 0:
        return 0

    count = 0

    if word[index - 1] == "t" and word[index] == "h":
        count += 1

    if len(word) > index + 1:
        count += count_th(word, index + 1)
    
    return count
