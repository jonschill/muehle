# coding: utf8
def enum (**named_values):
    return type('Enum', (), named_values)
