import sys
import chilkat


key = crypt = chilkat.CkCrypt2()
success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()


def encrypt3DES(key, text):
   """algoritmo"""
   crypt = chilkat.CkCrypt2()
   crypt.put_CryptAlgorithm("3des")    
   crypt.put_CipherMode("cbc")
   crypt.put_KeyLength(192)
   crypt.put_PaddingScheme(0)
   crypt.put_EncodingMode("hex")
   ivHex = "0001020304050607"
   crypt.SetEncodedIV(ivHex,"hex")
   """algoritmo"""
   keyHex = key
   crypt.SetEncodedKey(keyHex,"hex")
   plain = crypt.encryptStringENC(text)
   return plain

def decrypt3DES(key,text):
   """algoritmo"""
   crypt = chilkat.CkCrypt2()
   crypt.put_CryptAlgorithm("3des")    
   crypt.put_CipherMode("cbc")
   crypt.put_KeyLength(192)
   crypt.put_PaddingScheme(0)
   crypt.put_EncodingMode("hex")
   ivHex = "0001020304050607"
   crypt.SetEncodedIV(ivHex,"hex")
   """algoritmo"""
   keyHex = key
   crypt.SetEncodedKey(keyHex,"hex")
   plain = crypt.decryptStringENC(text)
   return plain