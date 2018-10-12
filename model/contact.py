from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, all_phones_from_homepage=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.all_phones_from_homepage = all_phones_from_homepage
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and \
               (self.id == other.id or self.id is None or other.id is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
