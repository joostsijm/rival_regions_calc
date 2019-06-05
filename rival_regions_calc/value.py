"""Value parser inherited from int"""


class Value(int):
    """A value parser"""

    def __new__(cls, value):
        if isinstance(value, str):
            value = value.replace('t', '000000000000')
            value = value.replace('k', '000')
            value = value.replace('.', '')
            value = int(value)
        return super(Value, cls).__new__(cls, value)

    def __repr__(self):
        str_format = '{:,}'.format(self)
        new_str = ''
        for i in range(len(str_format), 0, -4):
            if str_format[i-4:i] == ',000':
                new_str = 'k' + new_str
            else:
                new_str = str_format[:i] + new_str
                break

        new_str = new_str.replace('kkkk', 't')
        new_str = new_str.replace(',', '.')
        return new_str

    def __str__(self):
        return self.__repr__()
