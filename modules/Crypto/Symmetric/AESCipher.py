import javax.crypto.Cipher as Cipher
import javax.crypto.spec.SecretKeySpec as SecretKeySpec
import javax.crypto.spec.IvParameterSpec as IvParameterSpec
import javax.crypto.spec.GCMParameterSpec as GCMParameterSpec

import base64

class AESCipher:
	"""
	- algorithm: str
	- provider: str
	"""
	def __init__(self, algorithm, provider=None):
		self.algorithm = algorithm
		self.provider = provider
		self.mode = algorithm.split("/")[1]


	"""
	- PlainText: str
	- SECRET_KEY: str // length of SECRET_KEY: 16, 24, 32
	- IV: str // length of IV: 16 for CBC, CFB, OFB, GCM
	- GCM_Tag: int // 128
	- Return value: base64 encode
	"""
	def encrypt(self, PlainText, SECRET_KEY, IV=None, GCM_Tag=128):
		if self.provider != None:
			instance = Cipher.getInstance(self.algorithm, self.provider)
		else:
			instance = Cipher.getInstance(self.algorithm)

		if self.mode == "ECB":
			instance.init(Cipher.ENCRYPT_MODE, SecretKeySpec(SECRET_KEY, "AES"))
		elif self.mode == "GCM":
			instance.init(Cipher.ENCRYPT_MODE, SecretKeySpec(SECRET_KEY, "AES"), GCMParameterSpec(GCM_Tag, IV))
		else:
			instance.init(Cipher.ENCRYPT_MODE, SecretKeySpec(SECRET_KEY, "AES"), IvParameterSpec(IV))

		CipherText = instance.doFinal(PlainText)
		return base64.b64encode(CipherText)


	"""
	- CipherText: base64 encode
	- SECRET_KEY: str // length of SECRET_KEY: 16, 24, 32
	- IV: str // length of IV: 16 for CBC, CFB, OFB, GCM
	- GCM_Tag: int // 128
	- Return value: str
	"""
	def decrypt(self, CipherText, SECRET_KEY, IV=None, GCM_Tag=128):
		if self.provider != None:
			instance = Cipher.getInstance(self.algorithm, self.provider)
		else:
			instance = Cipher.getInstance(self.algorithm)

		if self.mode == "ECB":
			instance.init(Cipher.DECRYPT_MODE, SecretKeySpec(SECRET_KEY, "AES"))
		elif self.mode == "GCM":
			instance.init(Cipher.DECRYPT_MODE, SecretKeySpec(SECRET_KEY, "AES"), GCMParameterSpec(GCM_Tag, IV))
		else:
			instance.init(Cipher.DECRYPT_MODE, SecretKeySpec(SECRET_KEY, "AES"), IvParameterSpec(IV))

		PlainText = instance.doFinal(base64.b64decode(CipherText))
		return  PlainText.tostring()