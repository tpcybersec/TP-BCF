import javax.crypto.Cipher as Cipher
import javax.crypto.spec.SecretKeySpec as SecretKeySpec
import javax.crypto.spec.IvParameterSpec as IvParameterSpec

import base64

class DESCipher:
	"""
	- algorithm: str // "DES/ECB/NoPadding", "DES/CBC/PKCS5Padding"
	- provider: str
	"""
	def __init__(self, algorithm, provider=None):
		self.algorithm = algorithm
		self.provider = provider
		self.mode = algorithm.split("/")[1]


	"""
	- PlainText: str
	- SECRET_KEY: str // length of SECRET_KEY: 8
	- IV: str // length of IV: 8 for CBC, CFB, OFB, GCM
	- Return value: base64 encode
	"""
	def encrypt(self, PlainText, SECRET_KEY, IV=None):
		if self.provider != None:
			instance = Cipher.getInstance(self.algorithm, self.provider)
		else:
			instance = Cipher.getInstance(self.algorithm)

		if self.mode == "ECB":
			instance.init(Cipher.ENCRYPT_MODE, SecretKeySpec(SECRET_KEY, "DES"))
		else:
			instance.init(Cipher.ENCRYPT_MODE, SecretKeySpec(SECRET_KEY, "DES"), IvParameterSpec(IV))

		CipherText = instance.doFinal(PlainText)
		return base64.b64encode(CipherText)


	"""
	- CipherText: base64 encode
	- SECRET_KEY: str // length of SECRET_KEY: 8
	- IV: str // length of IV: 8 for CBC, CFB, OFB, GCM
	- Return value: str
	"""
	def decrypt(self, CipherText, SECRET_KEY, IV=None):
		if self.provider != None:
			instance = Cipher.getInstance(self.algorithm, self.provider)
		else:
			instance = Cipher.getInstance(self.algorithm)

		if self.mode == "ECB":
			instance.init(Cipher.DECRYPT_MODE, SecretKeySpec(SECRET_KEY, "DES"))
		else:
			instance.init(Cipher.DECRYPT_MODE, SecretKeySpec(SECRET_KEY, "DES"), IvParameterSpec(IV))

		PlainText = instance.doFinal(base64.b64decode(CipherText))
		return  PlainText.tostring()