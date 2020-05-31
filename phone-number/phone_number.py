class PhoneNumber:
    def __init__(self, number):
        self.number = number
        print(self.phone_no(number))

    def phone_no(self, number):
        new_str = ''
        for no in self.number:
            if no.isdigit():
                new_str += no
        if new_str[0] == '1':
            new_str = new_str[1:]
        if len(new_str) != 10:
            raise ValueError

        return f'Phone number is {new_str}'

#number = PhoneNumber("122345067890").number



