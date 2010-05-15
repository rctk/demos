import sys

if sys.version_info[0] == 3:    
    ## python 3
    def highlight(source):
        """ no pygments for python 3 """
        return '<pre>%s</pre>' % source.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
else:
    from pygments import highlight as hl
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter

    def highlight(source):
        return hl(source, PythonLexer(), HtmlFormatter(noclasses=True))
