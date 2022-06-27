#from dataclasses import replace


char_map = {    'සු': 'su',
                'ජා': 'ja',
                ' ': ' ',
                'තා': 'tha',
                'ව': 'wa',
                'ර්': 'r',
                'ර්': 'r',
                'න': 'na',
                'ල': 'la',
                'තා': 'tha',
                'ජී': 'jee',
                'වා': 'va',
                'න': 'na',
                'න්': 'n',
                'ද': 'da',
                'ධ': 'dha',
                'ණ': 'na',
                'උ': 'u',
                'ප': 'pa',
                'ත': 'tha',
                'හා': 'haa',
                'ධා': 'dha',
                'නා': 'naa',
                'ස': 'sa',
                'හෝ': 'ho',
                'නි': 'ni',
                'ල': 'la',
                'බා': 'ba',
                'ඇ': 'ae',
                'ත': 'tha',
                'අ': 'a',
                'ඉ': 'i',
                'ඊ': 'ee',
                'එ': 'ae',
                'ඔ': 'o',
                'ක': 'ka',
                'ග': 'ga',
                'න': 'na',
                'ත': 'tha',
                'ද': 'dha',
                'ඩ': 'da',
                'න': 'na',
                'ත': 'tha',
                'ප': 'pa',
                'බ': 'ba',
                'ම': 'ma',
                'ය': 'ya',
                'ර': 'ra',
                'ල': 'la',
                'ව': 'wa',
                'ශ': 'sha',
                'ස': 'sa',
                'හ': 'ha',
                'ල': 'la',
                'ෆ': 'fa',
                'ස්': 's'}

replaced_text = ''

intext = input('type :')

     
for letter in intext:
    try:
        replaced_text += char_map[letter]
    except KeyError: 
            replaced_text += letter
                
            print (replaced_text )
    