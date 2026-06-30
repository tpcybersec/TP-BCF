import java.security.Signature as Signature
import java.security.KeyFactory as KeyFactory
import java.security.spec.X509EncodedKeySpec as X509EncodedKeySpec
import java.security.spec.PKCS8EncodedKeySpec as PKCS8EncodedKeySpec

import base64

class ECDSACipher:
	"""
	- algorithm: str
	"""
	def __init__(self, algorithm):
		self.algorithm = algorithm


	"""
	- PublicKey: str
	- Return value: PublicKey object
	"""
	def ECPublicKey(self, PublicKey):
		return KeyFactory.getInstance("EC").generatePublic(X509EncodedKeySpec(base64.b64decode(PublicKey.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "").replace("\r", "").replace("\n", ""))))


	"""
	- PrivateKey: str
	- Return value: PrivateKey object
	"""
	def ECPrivateKey(self, PrivateKey):
		return KeyFactory.getInstance("EC").generatePrivate(PKCS8EncodedKeySpec(base64.b64decode(PrivateKey.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "").replace("\r", "").replace("\n", ""))))


	"""
	- message: str
	- PrivateKey: str
	- Return value: str (Base64-encoded)
	"""
	def signature(self, message, PrivateKey):
		sign = Signature.getInstance(self.algorithm)

		sign.initSign(self.ECPrivateKey(PrivateKey))
		sign.update(message)
		return base64.b64encode(sign.sign())


	"""
	- message: str
	- signedData: str
	- PublicKey: str
	- Return value: boolean
	"""
	def verify(self, message, signedData, PublicKey):
		sign = Signature.getInstance(self.algorithm)

		sign.initVerify(self.ECPublicKey(PublicKey))
		sign.update(message)
		return sign.verify(signedData)