# TODO Still nothing have been done make a function that hash the input and return the hashed version of that input
class Hash:
    def __init__(self, hashable):
        self.hashable = hashable
        self.prop = -1

    def hashnumber(self):
        return self.hashable * 2

    def propfunc(self):
        self.prop += 1
