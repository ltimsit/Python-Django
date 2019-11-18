class Elem():
    def __init__(self, tag='div', attr={}, content='', tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = ''
        if type(content) == list:
            self.content +='\n'
            for cont in content:
                    self.content += '   '+str(cont)+'\n'
        else:
            if isinstance(content, Elem):
                self.content = '\n  '+str(content)+'\n'
            elif type(content) == str:
                self.content = content
        self.tag_type = tag_type

    def __str__(self):
        attrib = ''
        if isinstance(self.attr, dict):
            for key, value in self.attr.items():
                attrib += " %s='%s'" % (key, str(value))
                # print(attrib, 'coucou')
        balise_o = '<'+self.tag+attrib+'>'
        balise_c = '</'+self.tag+'>'
        return balise_o+self.content+('' ,balise_c)[self.tag_type == 'double']

    def add_content(self, new_content):
        self.content += new_content

class Text(str):
    def __str__(self):
        result = super().__str__()
        data_to_replace = ['<', '>', '"', '\n']
        replace_with = ['&lt;', '&gt;', '&quot;', '\n<br />\n']
        for inp, out in zip(data_to_replace, replace_with):
            result = result.replace(inp, out)
        # print(result)
        return result

if __name__=='__main__':
    import test

    test.test_text()
    tst = str(Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double'))
    tst = str(Elem(content=[Text('foo'), Text('bar'), Elem()]))
    print(tst, '\n', '<div>\n  foo\n  bar\n \
 <div></div>\n</div>')
    # assert tst == '<body>\n  <div></div>\n</body>'
    # print(tst, '\n','<body>\n  <div></div>\n</body>')
    test.test_elem_basics()
    # tst = Elem('banane', {'patate': 2}, 'je suis une\n fougere', 'simple')
    # print(tst)
    # tst = str(Elem(tag='body', attr={}, content=Elem(), tag_type='double'))
    # print(tst)
    # tst = str(Elem(content=[Text('foo'), Text('bar'), Elem()]))
    # print(tst
