from collections import Counter
def is_isogram(string):
    if string == '':
        return True
    chr_allowed = (' ', '-')

    for word in string.lower():
        if word not in chr_allowed and string.lower().count(word) > 1:
            return False
        else:
            continue
    return True
