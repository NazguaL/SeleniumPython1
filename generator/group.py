import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.group import Group


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = str(a)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

constant = [
        Group(name="name1", header="header1", footer="footer1"),
        Group(name="name2", header="header2", footer="footer2")
]

testdata = [Group(name=random_string("name", 5), header=random_string("header", 20), footer=random_string("footer", 20))
         for i in range(n)]

groups_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(groups_file, "w") as file:
    jsonpickle.set_encoder_options("json", indent=4)
    # file.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=4))
    file.write(jsonpickle.encode(testdata))