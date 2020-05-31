'''def sound(number):
    lst = []
    for f in factors:
        if number % f == 0:
            lst.append(divisible[f])
    return lst

def convert(number):
    s = sound(number)
    if len(s) == 0:
        return str(number)
    else:
        return ''.join(s)

divisible = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
factors = (3, 5, 7)'''


def convert(number: int) -> str:
    result = ''
    result += "Pling" if number % 3 == 0 else ""
    result += "Plang" if number % 5 == 0 else ""
    result += "Plong" if number % 7 == 0 else ""

    return result or str(number)

print(convert(84))