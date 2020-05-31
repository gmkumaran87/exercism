def two_fer(name=''):
    if len(name) == 0:
        return f'One for you, one for me.'
    else:
        return f'One for {name}, one for me.'

print(two_fer('Muthu'))