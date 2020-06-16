from collections import Counter
def is_isogram(string):
    chr_allowed = (' ', '-')
    key_set = set()
    count = Counter(string.lower())

    if not count.keys():
        return True

    for val in count.keys():
        if val not in chr_allowed :
            key_set.add(count[val])
    return len(key_set) == 1