from Crypto.Cipher import AES
#this is for creating string vector
import random
import base64
import sys # this is for process exit

maxlength = 16
minlength = 4
mode = AES.MODE_CBC # strongest crypto

message = "There is nothing either good or bad, but thinking makes it so."
password = input("please input your password\n({min} letters min, {max} letters max) > ".format(min=minlength,max=maxlength))

if len(password) > maxlength:
  print("must be less than {0} letters".format(maxlength))
  sys.exit(0)
elif len(password) < minlength:
  print("must be longer than {0} letters".format(minlength))
  sys.exit(0)

#creates randomized letters
def createHash(weight):
  clues = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567891234567890"
  #the return value is randomized string of X letters == "aF3329CdkF..."
  return ''.join(random.SystemRandom().choice(clues) for _ in range(weight))

myhash = createHash(maxlength)  #initial hash

#set the text to X letters when it's shorter
#this is a drawback of CBC cryptographic method.
#CBC always need to be set up at fixed length of characters
#the length must be 16 * X
def mkpad(s, size):
  s = s.encode("utf-8")
  pad = b' ' * (size - len(s) % size)
  return s + pad

def encrypt(password,data):
  #adjust the size of text
  password = mkpad(password,maxlength)
  data = mkpad(data,maxlength)

  password = password[:maxlength]
  #encrypt
  aes = AES.new(password,mode,myhash) #it creates initial AES key with custom hash
  data_cipher = aes.encrypt(data)
  return base64.b64encode(data_cipher).decode("utf-8")

def decrypt(password,encdata):
  #adjust the size of text
  password = mkpad(password,16)
  password = password[:16]

  aes = AES.new(password,mode,myhash) #it creates initial AES key with custom hash
  #decrypt
  encdata = base64.b64decode(encdata)
  data = aes.decrypt(encdata)
  return data.decode("utf-8")

enc = encrypt(password,message)
dec = decrypt(password,enc)

print("encrypted: ",enc)
print("decrypted: ",dec)