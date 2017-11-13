class sth(object):
    def __init__(self,xixi):
        self.a = xixi
    def __enter__(self):
        print u'haha jinlail'
        return self.a
    def __exit__(self, type, value, traceback):
        print u'haha chulail'

with sth('xixi_name') as s:
    print s
