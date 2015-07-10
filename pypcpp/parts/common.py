from collections import OrderedDict

class Part:
    def __init__(self):
        self.fields = OrderedDict()
    
    @classmethod
    def name(cls):
        return cls.__name__
    
    @classmethod
    def isName(cls, name):
        return name == cls.name()
    
    def __repr__(self):
        ret = []
        for k, v in self.fields.items():
            ret.append(v)
        
        return ' '.join(ret)
    
    def __str__(self):
        return repr(self)
        
    def beautifyFields(self):
        pass
        