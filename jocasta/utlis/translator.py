from urllib.request import urlopen


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return None


class translate(object):
    """docstring for translate."""
    def __init__(self, *arg):
        super(translate, self).__init__()
        self.arg = arg
        
    @classmethod
    def tr(cls, text:str, out_lang:str = 'en', in_lang:str = 'auto') -> bool:
        url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={in_lang}&tl={out_lang}&dt=t&q={text}'
        result = urlopen(url)
        data = result.read().decode('utf-8')
        cls.text = find_between(data,'[[["','"')
        return cls.text is not None
        
        
    @property
    def text(self):
        return self.text
