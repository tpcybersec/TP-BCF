import javax.crypto.KeyAgreement as KeyAgreement
import java.security.KeyFactory as KeyFactory
import java.security.spec.X509EncodedKeySpec as X509EncodedKeySpec
import java.security.spec.PKCS8EncodedKeySpec as PKCS8EncodedKeySpec

import base64

class KeyExchange:
	"""
	- algorithm: str
	 + "ECDH" curves: P-256 (secp256r1), P-384 (secp384r1), P-521 (secp521r1)
	 + "DH"
	 + "X25519"
	 + "X448"
	"""
	def __init__(self, algorithm):
		self.algorithm = algorithm


	"""
	- PublicKey: str
	- Return value: PublicKey object
	"""
	def ECPublicKey(self, PublicKey):
		if self.algorithm == "ECDH":
			KeyFactoryInstance = KeyFactory.getInstance("EC")
		else:
			KeyFactoryInstance = KeyFactory.getInstance(self.algorithm)

		return KeyFactoryInstance.generatePublic(X509EncodedKeySpec(base64.b64decode(PublicKey.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "").replace("\r", "").replace("\n", ""))))


	"""
	- PrivateKey: str
	- Return value: PrivateKey object
	"""
	def ECPrivateKey(self, PrivateKey):
		if self.algorithm == "ECDH":
			KeyFactoryInstance = KeyFactory.getInstance("EC")
		else:
			KeyFactoryInstance = KeyFactory.getInstance(self.algorithm)

		return KeyFactoryInstance.generatePrivate(PKCS8EncodedKeySpec(base64.b64decode(PrivateKey.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "").replace("\r", "").replace("\n", ""))))


	"""
	- serverPublicKey: str
	- clientPrivateKey: str
	- Return value: str (Base64-encoded)
	"""
	def getSharedSecret(self, serverPublicKey, clientPrivateKey):
		keyAgreement = KeyAgreement.getInstance(self.algorithm)

		keyAgreement.init(self.ECPrivateKey(clientPrivateKey))

		keyAgreement.doPhase(self.ECPublicKey(serverPublicKey), True)

		sharedSecret = keyAgreement.generateSecret()
		return base64.b64encode(sharedSecret)