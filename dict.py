
class sin_str(str):
    @property
    def __phonetics(self) -> dict:
        return {'අ':'a',
                'ඉ':'i',
                'ඊ':'ee',
                'එ':'ae',
                'ඔ':'o',
                'ක':'ka',
                'ග':'ga',
                'න':'na',
                'ත':'tha',
                'ද':'dha',
                'ඩ':'da',
                'න':'na',
                'ත':'tha',
                'ප':'pa',
                'බ':'ba',
                'ම':'ma',
                'ය':'ya',
                'ර':'ra',
                'ල':'la',
                'ව':'wa',
                'ශ':'sha',
                'ස':'sa',
                'හ':'ha',
                'ල':'la',
                'ෆ':'fa',
                'කු':'ku',
                'ක්':'k',
                'කා':'kaa',
                'කි':'ki',
                'කී':'kee',
                'ගු':'gu',
                'ටේ':'te',
                ' ':' '
               }
    
    
    @property
    def transliteration(self) -> str:
        p = self.__phonetics
        return ''.join(p.get(c, None) or c for c in self)


while(True):
    text=input('type :')
    text = sin_str(text)
    print(text.transliteration) 