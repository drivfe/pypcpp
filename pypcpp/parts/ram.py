from pypcpp.parts.common import Part

class RAM(Part):
    _arg = '--ram'
    _fetch = 'memory'
    
    @staticmethod
    def generateFields():
        from collections import OrderedDict
        
        fields = OrderedDict()
        fields['ram'] = 1
        fields['speed'] = 2
        #fields['type'] = 3
        fields['modules'] = 5
        #fields['size'] = 6
        fields['price/gb'] = 7
        fields['price'] = 10
        
        return fields