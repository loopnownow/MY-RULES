import sys
from html.parser import HTMLParser
VOID={"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack=[]
        self.err=[]
    def handle_starttag(self,tag,attrs):
        if tag not in VOID: self.stack.append((tag,self.getpos()))
    def handle_endtag(self,tag):
        if tag in VOID: return
        if not self.stack: self.err.append(f"extra </{tag}> at {self.getpos()}"); return
        t,pos=self.stack.pop()
        if t!=tag:
            self.err.append(f"mismatch </{tag}> at {self.getpos()} closes <{t}> from {pos}")
for f in sys.argv[1:]:
    p=P(); p.feed(open(f,encoding="utf-8").read())
    left=[x for x in p.stack]
    print(f, "ERRORS" if (p.err or left) else "OK", p.err[:3], [x[0] for x in left][:5])
