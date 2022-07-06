
class sin_str(str):
    @property
    def __phonetics(self) -> dict:
        return {'සිංහ':'singhe',
                'ධා':'dha',
                'ණ':'na',
                'තා':'tha',
                'ජා':'ja',
                'සු':'su',
                'වී':'wee',
                'ස්':'s',
                'ර්':'r',
                'හ':'ha',
                'ර':'ra',
                'ෆ':'fa',
                'ව':'wa',
                'ම':'ma',
                'න':'na',
                ' ':' '
               }
    
    
    @property
    def transliteration(self) -> str:
        p,t = self.__phonetics, self [:]
        for k,v in p.items(): t=t.replace(k, v)
        return t
        #return ''.join(p.get(c, None) or c for c in self)


while(True):
    text=input('type :')
    text = sin_str(text)
    print(text.transliteration) 