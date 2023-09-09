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
    def tr(self,text:str,out_lang:str = 'en',in_lang:str = 'auto') -> bool:
        url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}'.format(in_lang, out_lang, text)
        result = urlopen(url)
        data = result.read().decode('utf-8')
        self.text = find_between(data,'[[["','"')
        if  self.text is None: return False
        else:
            return True
        
        
    @property
    def text(self):
        return self.text
