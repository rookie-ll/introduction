'''<video preload="metadata" conrtols="true" src="blob:https://v.youku.com/f0808daa-5759-4410-bce9-5f29718e239c" style="width: 100%; height: 100%; background-color: rgb(0, 0, 0);"></video>'''
import requests

r=requests.get("https://v.youku.com/0b88ec18000010ac5d8c12d70000bf90")
with open("hello.mp4","wb") as pp:
    for chunk in r.iter_content():
        if chunk:
            pp.write(chunk)

import pywifi