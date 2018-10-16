import random
import string
from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
        Group(name="name1", header="header1", footer="footer1"),
        Group(name="name2", header="header2", footer="footer2")
]
"""
# [Group(name="", header="", footer="")] + \
testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 5)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
    ] + [Group(name=random_string("name", 5), header=random_string("header", 20), footer=random_string("footer", 20))
         for i in range(3)]
"""