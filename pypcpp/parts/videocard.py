from pypcpp.parts.common import Part

class VideoCard(Part):
    _arg = '--videocard'
    _fetch = 'video-card'
    
    def beautifyFields(self):
        #Only brand name of the Videocard
        self.fields['videocard'] = self.fields['videocard'].split(' ')[0]
        
        #Remove 'Radeon' and 'Geforce' from chipset
        self.fields['chipset'] = self.fields['chipset'].replace('Radeon ', '').replace('GeForce ', '')
        
        #Remove 'black edition' from series (string too long)
        self.fields['series'] = self.fields['series'].replace('Black Edition ', '')
    
    @staticmethod
    def generateFields():
        from collections import OrderedDict
        
        fields = OrderedDict()
        fields['videocard'] = 1
        fields['series'] = 2
        fields['chipset'] = 3
        fields['memory'] = 4
        fields['coreclock'] = 5
        fields['price'] = 8
        
        return fields