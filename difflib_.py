import sys
import difflib
from difflib import HtmlDiff

file1 = open(sys.argv[1]).read()
file2 = open(sys.argv[2]).read()

delta = difflib.Differ().compare(file1.splitlines(), file2.splitlines())
print("\n".join(delta))

delta_html = HtmlDiff().make_file(file1.splitlines(), file2.splitlines())
with open("delta.html","w") as f:
    f.write(delta_html)
