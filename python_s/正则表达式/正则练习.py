import re
a="////"
r=re.match(r"^/{1}(.+).html","//indexsfdsf.html")
print(r.group())
print(r.group(1))
