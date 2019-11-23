from . import sf
msg = "ZmxhZ3tXZWxjb21lIHRvIDNDVEYhfQ%3D%3D"
#key = "12345678"  #key值可传可不传
des1 = sf.MyDESCrypt()
#加密
#cipherTxt = des1.encrypt(msg)  #返回值为bytes型
#print(cipherTxt)
#解密
decTxt = des1.decrypt(msg);  #返回值为str型
print(decTxt)