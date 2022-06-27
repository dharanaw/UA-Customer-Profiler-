characters_map ={
{               'ට':'ta',
                'සු':'su',
                'ජා':'ja',
                'තා':'tha',
                'වී':'wee',
                'ර':'ra',
                'සිං':'sin'
                'හ:''ha', 
                'ක':'ka',
                'ර':'ra',
                ' ':' ',
                'කු':'ku',
                'ස':'sa',
                }

}


text = ('රක සක හතා')


for letter in text:
    try:
        text = text.replace(letter,characters_map[letter])
    except KeyError: 
        pass # if a letter is not recognized it will just let it as is

    replaced_text = ''
for letter in text:
    try:
        replaced_text += characters_map[letter]
    except KeyError: 
        replaced_text += letter