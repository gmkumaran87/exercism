def distance(strand_a, strand_b):
    hamming_distance = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Kindly enter the same DNA strands')
    else:
        return sum(x != y for x,y in zip(list(strand_a), list(strand_b)))