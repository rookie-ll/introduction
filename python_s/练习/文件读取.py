with open("hello.txt","r",encoding="utf8") as pp:
    files=pp.read()
    print(files)

with open("hello1.txt,","w",encoding="utf8") as pp:
    file=pp.write("hello")
