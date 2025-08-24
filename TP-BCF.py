# -*- coding: utf-8 -*-
from burp import IBurpExtender, IMessageEditorTabFactory, IHttpListener, IMessageEditorTab, IExtensionStateListener, IBurpExtenderCallbacks

from java.lang import Runnable
from javax.swing import SwingUtilities, JMenu, JCheckBoxMenuItem, JMenuItem, JFileChooser, UIManager, JOptionPane
from java.awt import Frame, Desktop, Color, Font
from java.awt.event import ActionListener
from java.io import File

import os
# Define the directory for TP-BCF
TPBCF_DIR = os.path.join(os.path.expanduser("~"), "TPCS-ENV", "TP-BCF")
# Define the file paths for TARGETS, ENV
TARGETS_FILE = os.path.join(TPBCF_DIR, "TARGETS.json")
ENV_FILE = os.path.join(TPBCF_DIR, "environments.json")

# Create the TP-BCF directory if it does not exist
if not os.path.exists(TPBCF_DIR):
	os.makedirs(TPBCF_DIR)
	print("[TP-BCF] Created directory: " + TPBCF_DIR)

# Add the TP-BCF site-packages directory to the Python path
import site
if os.path.exists(os.path.join(os.getcwd(), "requirements.txt")):
	os.system("pip install -r \"{}\" --target \"{}\" --no-user".format(os.path.join(os.getcwd(), "requirements.txt"), os.path.join(TPBCF_DIR, "site-packages")))
site.addsitedir(os.path.join(TPBCF_DIR, "site-packages"))

import re
from datetime import datetime
import json_duplicate_keys as jdks
from collections import OrderedDict
from tp_http_request_response_parser import TP_HTTP_REQUEST_PARSER, TP_HTTP_RESPONSE_PARSER
from TP_Generator import Utils, MFA_Generator, Nonce_Generator, QR_Generator

from modules.Crypto.Symmetric.AESCipher import AESCipher
from modules.Crypto.Symmetric.DESCipher import DESCipher
from modules.Crypto.Asymmetric.RSACipher import RSACipher
from modules.Crypto.Hash.CRC32 import CRC32
from modules.Crypto.Hash.HMAC_MD5 import HMAC_MD5
from modules.Crypto.Hash.HMAC_SHA1 import HMAC_SHA1
from modules.Crypto.Hash.HMAC_SHA224 import HMAC_SHA224
from modules.Crypto.Hash.HMAC_SHA256 import HMAC_SHA256
from modules.Crypto.Hash.HMAC_SHA384 import HMAC_SHA384
from modules.Crypto.Hash.HMAC_SHA512 import HMAC_SHA512
from modules.Crypto.Hash.MD2 import MD2
from modules.Crypto.Hash.MD5 import MD5
from modules.Crypto.Hash.SHA1 import SHA1
from modules.Crypto.Hash.SHA224 import SHA224
from modules.Crypto.Hash.SHA256 import SHA256
from modules.Crypto.Hash.SHA384 import SHA384
from modules.Crypto.Hash.SHA512 import SHA512



EXTENSION_NAME = "TP-BCF"
EXTENSION_VERSION = "2025.8.24"
TARGET = "tpcybersec.com"
TEMP = dict()

# Initialize CipherTab and ProcessMessage dictionaries
CipherTab = {
	"EncryptRequest": [],
	"DecryptRequest": [],
	"EncryptResponse": [],
	"DecryptResponse": []
}
ProcessMessage = {
	"Request": [],
	"Response": []
}

# Check if the required files exist, if not create them
if not os.path.isfile(TARGETS_FILE):
	jdks.JSON_DUPLICATE_KEYS({}).dump(TARGETS_FILE)
	print("[TP-BCF] Created TARGETS file: " + TARGETS_FILE)

if not os.path.isfile(ENV_FILE):
	jdks.JSON_DUPLICATE_KEYS({}).dump(ENV_FILE)
	print("[TP-BCF] Created Environment Variables file: " + ENV_FILE)

# Load the TARGETS file and process each target
targets = jdks.load(TARGETS_FILE, ordered_dict=True, skipDuplicated=True) or jdks.JSON_DUPLICATE_KEYS({})
for target_name in targets.getObject():
	target_file = targets.get(target_name+"||path")["value"]
	if target_file != "JSON_DUPLICATE_KEYS_ERROR":
		print("[TP-BCF] " + target_file)
		if targets.get(target_name+"||enable")["value"] == True:
			JDKSObject = jdks.load(target_file, skipDuplicated=True, _isDebug_=True)
			if JDKSObject:
				if JDKSObject.get("CipherTab||EncryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
					CipherTab["EncryptRequest"] += JDKSObject.get("CipherTab||EncryptRequest")["value"]
				if JDKSObject.get("CipherTab||DecryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
					CipherTab["DecryptRequest"] += JDKSObject.get("CipherTab||DecryptRequest")["value"]
				if JDKSObject.get("CipherTab||EncryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
					CipherTab["EncryptResponse"] += JDKSObject.get("CipherTab||EncryptResponse")["value"]
				if JDKSObject.get("CipherTab||DecryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
					CipherTab["DecryptResponse"] += JDKSObject.get("CipherTab||DecryptResponse")["value"]

				if JDKSObject.get("ProcessMessage||Request")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
					ProcessMessage["Request"] += JDKSObject.get("ProcessMessage||Request")["value"]
				if JDKSObject.get("ProcessMessage||Response")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
					ProcessMessage["Response"] += JDKSObject.get("ProcessMessage||Response")["value"]
print("CipherTab", CipherTab)
print("ProcessMessage", ProcessMessage)

# Default environment variables
def default_envs():
	envs = OrderedDict()
	envs["defaultPublicKey"] = "-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuTwspB6ubxVDBIb7IL7sSinHDmZLk/7RYzOWzVmLZo7dzBKiOmAbvFMMGRXFZ/37eThQ7VP31qe6MCH7PhtuP+KKOFpfgQc3O9umo78Qut4NGuCYNiuRrRx2jv1KESS+zIxllelx/JmEbtrME3boMZJ7W/y/SL8dfhYuGZYuqrGOe2ZRwekWkxAUJlAlHT/keDU8qU3oGDgVIn6Ck5MW0o8yBoMsm7o1LfvAGdt5jdxATXy1pzIi3Tr/bLVVkOPmaYrmRQ1McQLSekGA0+hn/MSMTIKRBA4JtSLaQ7YPZQPqwlvYm56958Lr8FPcQ7dz3KXWRY5wG+KSf+3vWnRZ3QIDAQAB-----END PUBLIC KEY-----"
	envs["defaultPrivateKey"] = "-----BEGIN PRIVATE KEY-----MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5PCykHq5vFUMEhvsgvuxKKccOZkuT/tFjM5bNWYtmjt3MEqI6YBu8UwwZFcVn/ft5OFDtU/fWp7owIfs+G24/4oo4Wl+BBzc726ajvxC63g0a4Jg2K5GtHHaO/UoRJL7MjGWV6XH8mYRu2swTdugxkntb/L9Ivx1+Fi4Zli6qsY57ZlHB6RaTEBQmUCUdP+R4NTypTegYOBUifoKTkxbSjzIGgyybujUt+8AZ23mN3EBNfLWnMiLdOv9stVWQ4+ZpiuZFDUxxAtJ6QYDT6Gf8xIxMgpEEDgm1ItpDtg9lA+rCW9ibnr3nwuvwU9xDt3PcpdZFjnAb4pJ/7e9adFndAgMBAAECggEAAQJP5/D22EoQXGTz10DS/rBtkimCfeLkdxrf1myHct6SXLs5QQInBIabSUOyGJfsl8NzxWcwsW2meP6mZLc3iYeNYzMy0/wbE+tlY/z1dV8iSSQyEBF6sKu4BZ1hmuhNVcXqA8AKy+p2Kzhr5is+po56t4yP6jCIU5iBVchYprtggIeLUDAKIGterKEYxJt/N8pdJ0oGhx4cNxcRBDylqdm0HJphyP19BtBOsFtdT9cN6khNpsWGl7UirvlI8eoJxfkXzSgRLn0XoZhl1gDKAD9XCWnII9nzZyINUY1ICG2fISMMGGCNs9YmaY0wzMkhNvty8fPoWH+XrvNyomxIQQKBgQDiMQqPsRYZEw51CsGyyJFALHUfCxsLv6lXeFgCzBY74rksF4CrrNR1rcrvbMe06P54el+dtGevnpb+C1x/iFUkncGW6hNZii/dpKlxUvFTnYYWAITOiOJltDliFlXt7jCZEkGO9WcYRmTibve3pgjxB79MxEo4bJQCRSHTd6ZaLQKBgQDRpWUxaA5IdwuX7/pxG9ekFvxkJCpjDj14rkA832SLs1Zoq/d4D6/0WTp+c6wHL7fzU1DFbgCwB560ktlAvI77J6tapl1hps6RYh9H3bz+Hb6d6eFlhdyUKuTX1XXw6RcK3pYtYOltavl3bwAal/7TEKjrdS59qwx2BlsbQvQ8cQKBgQCHjjRyIQLJTC5h3mxvJNxHxVz7mcA/rkFidnDoXD8G7L1ku0EVoaJCVEFGc77LoMbAlTYwYSmyiiybW1u34pCEPTcDpoyqILLG9iPGEpsmLUVqci0lScvEf9nT+ubMjO77DYHUlyWN2sIjIbW7jfnV2XrAGvMQFaIuKhg3j4FWkQKBgQCYfp2QBae2EFnviBD864q9AjdOxHvMl9QhD2cMoFZrw+SLuOMGgyqzK6B/0LYGeDBvH2B2a+C2KqTHprW/ACllCWL8Sl1MpeBGIkCsrt9FXO+FwFVC2s8rO9RAJzZmKbaoImbM1VyWSaTyulwx+/PRJaIpu5A4uw4SX+cvelFcEQKBgHz2GicI/2cgYlRaeeR8tDSrfVNkhkF1qQZpC3GlTLMjmzZQzLXkjxvYRjNfSJaTZ9CMlaD1PFnqu7Uk9KhUwkClGnSsvFBO2MrRh6P32XS5eDVoP7jZ1pk5/dvuB1RSJqLT63FRaBi8XPSPeT/9po9lCfipK2tlNnggFMPZf3qQ-----END PRIVATE KEY-----"
	envs["defaultSecretKey"] = "C]$L)D}Sd<s!eRkW.hZT`MK9jQGN[4z~"
	envs["defaultIV"] = "X.4njY@(,RN&~f*W"
	envs["defaultSalt"] = "z#}k%>v'53^P<4Ky"
	envs["defaultPassword"] = "We4K=T!q@F#98zPw"
	return envs
print("[TP-BCF] Default Environment Variables:")
for k, v in default_envs().items():
	print(" - {} = {}".format(k, v))

print("[TP-BCF] Custom Environment Variables:")
for k, v in jdks.load(ENV_FILE, ordered_dict=True, skipDuplicated=True).getObject().items():
	print(" - {} = {}".format(k, v))



# Safe eval and exec functions to prevent code injection
def safe_eval(expr, local_vars=None):
	if local_vars is None:
		local_vars = {}
	local_vars["TEMP"] = TEMP

	restricted_globals = { "__builtins__": {} }
	allowed_classes = { "jdks": jdks, "re": re, "TP_HTTP_REQUEST_PARSER": TP_HTTP_REQUEST_PARSER, "TP_HTTP_RESPONSE_PARSER": TP_HTTP_RESPONSE_PARSER, "Utils": Utils, "MFA_Generator": MFA_Generator, "Nonce_Generator": Nonce_Generator, "QR_Generator": QR_Generator, "AESCipher": AESCipher, "DESCipher": DESCipher, "RSACipher": RSACipher, "CRC32": CRC32, "HMAC_MD5": HMAC_MD5, "HMAC_SHA1": HMAC_SHA1, "HMAC_SHA224": HMAC_SHA224, "HMAC_SHA256": HMAC_SHA256, "HMAC_SHA384": HMAC_SHA384, "HMAC_SHA512": HMAC_SHA512, "MD2": MD2, "MD5": MD5, "SHA1": SHA1, "SHA224": SHA224, "SHA256": SHA256, "SHA384": SHA384, "SHA512": SHA512 }
	restricted_globals.update(allowed_classes)

	return eval(expr, restricted_globals, local_vars)

def safe_exec(code, local_vars=None):
	if local_vars is None:
		local_vars = {}
	local_vars["TEMP"] = TEMP

	restricted_globals = { "__builtins__": {} }
	allowed_classes = { "jdks": jdks, "re": re, "TP_HTTP_REQUEST_PARSER": TP_HTTP_REQUEST_PARSER, "TP_HTTP_RESPONSE_PARSER": TP_HTTP_RESPONSE_PARSER, "Utils": Utils, "MFA_Generator": MFA_Generator, "Nonce_Generator": Nonce_Generator, "QR_Generator": QR_Generator, "AESCipher": AESCipher, "DESCipher": DESCipher, "RSACipher": RSACipher, "CRC32": CRC32, "HMAC_MD5": HMAC_MD5, "HMAC_SHA1": HMAC_SHA1, "HMAC_SHA224": HMAC_SHA224, "HMAC_SHA256": HMAC_SHA256, "HMAC_SHA384": HMAC_SHA384, "HMAC_SHA512": HMAC_SHA512, "MD2": MD2, "MD5": MD5, "SHA1": SHA1, "SHA224": SHA224, "SHA256": SHA256, "SHA384": SHA384, "SHA512": SHA512 }
	restricted_globals.update(allowed_classes)

	exec(code, restricted_globals, local_vars)



class MenuBar(Runnable, IExtensionStateListener):
	def __init__(self, callbacks):
		self.callbacks = callbacks
		self.callbacks.registerExtensionStateListener(self)
		self.menu_scanner_encReq_item = None
		self.menu_scanner_decRes_item = None
		self.menu_proxy_encReq_item = None
		self.menu_proxy_decRes_item = None
		self.menu_intruder_encReq_item = None
		self.menu_intruder_decRes_item = None
		self.menu_repeater_encReq_item = None
		self.menu_repeater_decRes_item = None
		self.menu_extender_encReq_item = None
		self.menu_extender_decRes_item = None
		self.menu_all_encReq_item = None
		self.menu_all_decRes_item = None
		self.menu_AutoRefresh_item = None
		self.selected_targets = set()
		self.menu_debug_mode_item = None


	def run(self):
		self.menu_button = JMenu(EXTENSION_NAME + " v" + EXTENSION_VERSION)

		# Encrypt Request
		self.menu_encReq = JMenu("Encrypt Request")
		self.menu_encReq.setOpaque(True)
		self.menu_encReq.setBackground(Color(36, 85, 145)) # steel blue
		self.menu_encReq.setForeground(Color.WHITE) # white
		self.menu_encReq.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_all_encReq_item = JCheckBoxMenuItem("All Tools")
		self.menu_all_encReq_item.setSelected(True)
		self.menu_all_encReq_item.setForeground(Color(0, 128, 255)) # deep sky blue
		self.menu_all_encReq_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_scanner_encReq_item = JCheckBoxMenuItem("Scanner")
		self.menu_scanner_encReq_item.setForeground(Color(0, 128, 255)) # deep sky blue
		self.menu_scanner_encReq_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_proxy_encReq_item = JCheckBoxMenuItem("Proxy")
		self.menu_proxy_encReq_item.setForeground(Color(0, 128, 255)) # deep sky blue
		self.menu_proxy_encReq_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_intruder_encReq_item = JCheckBoxMenuItem("Intruder")
		self.menu_intruder_encReq_item.setForeground(Color(0, 128, 255)) # deep sky blue
		self.menu_intruder_encReq_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_repeater_encReq_item = JCheckBoxMenuItem("Repeater")
		self.menu_repeater_encReq_item.setForeground(Color(0, 128, 255)) # deep sky blue
		self.menu_repeater_encReq_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_extender_encReq_item = JCheckBoxMenuItem("Extender")
		self.menu_extender_encReq_item.setForeground(Color(0, 128, 255)) # deep sky blue
		self.menu_extender_encReq_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_encReq.add(self.menu_all_encReq_item)
		self.menu_encReq.addSeparator()
		self.menu_encReq.add(self.menu_scanner_encReq_item)
		self.menu_encReq.addSeparator()
		self.menu_encReq.add(self.menu_proxy_encReq_item)
		self.menu_encReq.addSeparator()
		self.menu_encReq.add(self.menu_intruder_encReq_item)
		self.menu_encReq.addSeparator()
		self.menu_encReq.add(self.menu_repeater_encReq_item)
		self.menu_encReq.addSeparator()
		self.menu_encReq.add(self.menu_extender_encReq_item)

		encReq_items = [
			self.menu_scanner_encReq_item,
			self.menu_proxy_encReq_item,
			self.menu_intruder_encReq_item,
			self.menu_repeater_encReq_item,
			self.menu_extender_encReq_item
		]
		for tool in encReq_items: tool.setSelected(True)

		# Decrypt Response
		self.menu_decRes = JMenu("Decrypt Response")
		self.menu_decRes.setOpaque(True)
		self.menu_decRes.setBackground(Color(36, 85, 145)) # steel blue
		self.menu_decRes.setForeground(Color.WHITE) # white
		self.menu_decRes.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_all_decRes_item = JCheckBoxMenuItem("All Tools")
		self.menu_all_decRes_item.setSelected(True)
		self.menu_all_decRes_item.setForeground(Color(0, 128, 255)) # deep sky blue
		self.menu_all_decRes_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_scanner_decRes_item = JCheckBoxMenuItem("Scanner")
		self.menu_scanner_decRes_item.setForeground(Color(0, 128, 255))  # deep sky blue
		self.menu_scanner_decRes_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_proxy_decRes_item = JCheckBoxMenuItem("Proxy")
		self.menu_proxy_decRes_item.setForeground(Color(0, 128, 255))  # deep sky blue
		self.menu_proxy_decRes_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_intruder_decRes_item = JCheckBoxMenuItem("Intruder")
		self.menu_intruder_decRes_item.setForeground(Color(0, 128, 255))  # deep sky blue
		self.menu_intruder_decRes_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_repeater_decRes_item = JCheckBoxMenuItem("Repeater")
		self.menu_repeater_decRes_item.setForeground(Color(0, 128, 255))  # deep sky blue
		self.menu_repeater_decRes_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_extender_decRes_item = JCheckBoxMenuItem("Extender")
		self.menu_extender_decRes_item.setForeground(Color(0, 128, 255))  # deep sky blue
		self.menu_extender_decRes_item.setFont(Font("Monospaced", Font.BOLD, 12))

		self.menu_decRes.add(self.menu_all_decRes_item)
		self.menu_decRes.addSeparator()
		self.menu_decRes.add(self.menu_scanner_decRes_item)
		self.menu_decRes.addSeparator()
		self.menu_decRes.add(self.menu_proxy_decRes_item)
		self.menu_decRes.addSeparator()
		self.menu_decRes.add(self.menu_intruder_decRes_item)
		self.menu_decRes.addSeparator()
		self.menu_decRes.add(self.menu_repeater_decRes_item)
		self.menu_decRes.addSeparator()
		self.menu_decRes.add(self.menu_extender_decRes_item)

		decRes_items = [
			self.menu_scanner_decRes_item,
			self.menu_proxy_decRes_item,
			self.menu_intruder_decRes_item,
			self.menu_repeater_decRes_item,
			self.menu_extender_decRes_item
		]
		for tool in decRes_items: tool.setSelected(True)

		# Environment Variables
		self.menu_envs = JMenu("Environment Variables")
		self.menu_envs.setOpaque(True)
		self.menu_envs.setBackground(Color(85, 107, 47)) # dark olive green
		self.menu_envs.setForeground(Color.WHITE) # white
		self.menu_envs.setFont(Font("Monospaced", Font.BOLD, 12))
		self.load_env_vars()

		# TARGETS
		self.menu_targets = JMenu("TARGETS")
		self.menu_targets.setOpaque(True)
		self.menu_targets.setBackground(Color(70, 130, 180)) # steel blue
		self.menu_targets.setForeground(Color.WHITE) # white
		self.menu_targets.setFont(Font("Monospaced", Font.BOLD, 12))
		self.load_targets()

		# Auto Refresh TARGETS Config
		self.menu_AutoRefresh_item = JCheckBoxMenuItem("Auto Refresh TARGETS Config")
		self.menu_AutoRefresh_item.setSelected(True)
		self.menu_AutoRefresh_item.setForeground(Color(70, 130, 180)) # steel blue
		self.menu_AutoRefresh_item.setFont(Font("Monospaced", Font.BOLD, 12))

		# Enable Debug Mode
		self.menu_debug_mode_item = JCheckBoxMenuItem("DEBUG Mode")
		self.menu_debug_mode_item.setSelected(True)
		self.menu_debug_mode_item.setForeground(Color(255, 69, 0)) # red
		self.menu_debug_mode_item.setFont(Font("Monospaced", Font.BOLD, 12))

		# Add to root menu
		self.menu_button.addSeparator()
		self.menu_button.add(self.menu_encReq)
		self.menu_button.addSeparator()
		self.menu_button.add(self.menu_decRes)
		self.menu_button.addSeparator()
		self.menu_button.addSeparator()
		self.menu_button.add(self.menu_envs)
		self.menu_button.addSeparator()
		self.menu_button.addSeparator()
		self.menu_button.add(self.menu_targets)
		self.menu_button.addSeparator()
		self.menu_button.add(self.menu_AutoRefresh_item)
		self.menu_button.addSeparator()
		self.menu_button.addSeparator()
		self.menu_button.add(self.menu_debug_mode_item)
		self.menu_button.addSeparator()

		UIManager.put("CheckBoxMenuItem.doNotCloseOnMouseClick", True)
		UIManager.put("RadioButtonMenuItem.doNotCloseOnMouseClick", True)

		burp_jframe = self.get_burp_jframe()
		if burp_jframe:
			burp_jmenu_bar = burp_jframe.getJMenuBar()
			burp_jmenu_bar.add(self.menu_button)
			burp_jmenu_bar.repaint()

		# Action listeners
		self.menu_all_encReq_item.addActionListener(MenuBar.AllToolsListener(encReq_items))
		self.menu_all_decRes_item.addActionListener(MenuBar.AllToolsListener(decRes_items))

		for item in encReq_items:
			item.addActionListener(MenuBar.IndividualToolListener(self.menu_all_encReq_item, encReq_items))
		for item in decRes_items:
			item.addActionListener(MenuBar.IndividualToolListener(self.menu_all_decRes_item, decRes_items))


	def load_env_vars(self):
		self.menu_envs.removeAll()

		self.menu_envs.addSeparator()
		for key, value in default_envs().items():
			default_env = JMenu(key)
			default_env.setToolTipText(str(value))
			default_env.setOpaque(True)
			default_env.setBackground(Color(255, 228, 181)) # moccasin
			default_env.setFont(Font("Monospaced", Font.BOLD, 12))

			self.menu_envs.add(default_env)
			self.menu_envs.addSeparator()

		envs = jdks.load(ENV_FILE, ordered_dict=True, skipDuplicated=True) or jdks.JSON_DUPLICATE_KEYS({})
		for key, value in envs.getObject().items():
			parent_menu = JMenu(key)
			parent_menu.setToolTipText(str(value))
			parent_menu.setOpaque(True)
			parent_menu.setBackground(Color(224, 255, 255)) # light cyan
			parent_menu.setFont(Font("Monospaced", Font.BOLD, 12))

			edit_item = JMenuItem("Edit")
			edit_item.setOpaque(True)
			edit_item.setBackground(Color(204, 229, 255)) # light blue
			edit_item.setFont(Font("Monospaced", Font.BOLD, 12))
			edit_item.addActionListener(lambda event, k=key: self.edit_env_var(k))
			parent_menu.add(edit_item)
			parent_menu.addSeparator()

			remove_item = JMenuItem("Remove")
			remove_item.setOpaque(True)
			remove_item.setBackground(Color(255, 204, 204)) # light red
			remove_item.setFont(Font("Monospaced", Font.BOLD, 12))
			remove_item.addActionListener(lambda event, k=key: self.remove_env_var(k))
			parent_menu.add(remove_item)

			self.menu_envs.add(parent_menu)
			self.menu_envs.addSeparator()
		self.menu_envs.addSeparator()
		envs.dump(ENV_FILE, indent=4)

		add_item = JMenuItem("( + ) Add New Variable...")
		add_item.setOpaque(True)
		add_item.setBackground(Color(204, 255, 204)) # light green
		add_item.setFont(Font("Monospaced", Font.BOLD, 12))
		add_item.addActionListener(self.add_env_var)
		self.menu_envs.add(add_item)
		self.menu_envs.addSeparator()


	def add_env_var(self, event):
		key = JOptionPane.showInputDialog(None, "Enter Variable Name:", "New Name", JOptionPane.PLAIN_MESSAGE)
		if not key: return
		value = JOptionPane.showInputDialog(None, "Enter Variable Value:", "New Value", JOptionPane.PLAIN_MESSAGE)
		if value is None: return
		envs = jdks.load(ENV_FILE, ordered_dict=True, skipDuplicated=True) or jdks.JSON_DUPLICATE_KEYS({})
		envs.set(key, value)
		print("[TP-BCF] Added New Variable: {} = {}".format(key, value))
		envs.dump(ENV_FILE, indent=4)
		self.load_env_vars()


	def edit_env_var(self, key):
		envs = jdks.load(ENV_FILE, ordered_dict=True, skipDuplicated=True)
		if envs and envs.get(key)["value"] != "JSON_DUPLICATE_KEYS_ERROR":
			value = JOptionPane.showInputDialog(None, "Edit Variable Value:", envs.get(key)["value"])
			if value is None: return
			envs.update(key, value)
			print("[TP-BCF] Edited Variable: {} = {}".format(key, value))
			envs.dump(ENV_FILE, indent=4)
			self.load_env_vars()


	def remove_env_var(self, key):
		if JOptionPane.showConfirmDialog(None, "Are you sure to remove the environment variable: {}?".format(key), "Confirm", JOptionPane.YES_NO_OPTION) != JOptionPane.YES_OPTION:
			return
		envs = jdks.load(ENV_FILE, ordered_dict=True, skipDuplicated=True)
		if envs:
			envs.delete(key)
			print("[TP-BCF] Deleted Variable: {}".format(key))
			envs.dump(ENV_FILE, indent=4)
			self.load_env_vars()


	def load_targets(self):
		self.menu_targets.removeAll()
		self.menu_targets.addSeparator()
		self.selected_targets.clear()
		targets = jdks.load(TARGETS_FILE, ordered_dict=True, skipDuplicated=True) or jdks.JSON_DUPLICATE_KEYS({})

		for target_name in targets.getObject():
			target_path = targets.get(target_name+"||path")["value"]
			if target_path != "JSON_DUPLICATE_KEYS_ERROR":
				target_enable = False if targets.get(target_name+"||enable")["value"] != True else True
				targets.update(target_name+"||enable", target_enable, allow_new_key=True)
				if target_enable:
					self.selected_targets.add(target_path)

				parent_menu = JMenu(target_name)
				parent_menu.setOpaque(True)
				parent_menu.setBackground(Color(240, 240, 240)) # light gray
				parent_menu.setFont(Font("Monospaced", Font.BOLD, 12))
				checkbox_item = JCheckBoxMenuItem("Enable")
				checkbox_item.setSelected(target_enable)
				checkbox_item.setForeground(Color(0, 128, 0)) # green
				checkbox_item.setFont(Font("Monospaced", Font.BOLD, 12))
				checkbox_item.addActionListener(MenuBar.TargetCheckListener(target_name, target_path, self))
				parent_menu.add(checkbox_item)
				parent_menu.addSeparator()

				edit_item = JMenuItem("Edit")
				edit_item.setOpaque(True)
				edit_item.setBackground(Color(204, 229, 255)) # light blue
				edit_item.setFont(Font("Monospaced", Font.BOLD, 12))
				edit_item.addActionListener(lambda event, n=target_name: self.edit_target(n))
				parent_menu.add(edit_item)
				parent_menu.addSeparator()

				remove_item = JMenuItem("Remove")
				remove_item.setOpaque(True)
				remove_item.setBackground(Color(255, 204, 204)) # light red
				remove_item.setFont(Font("Monospaced", Font.BOLD, 12))
				remove_item.addActionListener(lambda event, n=target_name: self.remove_target(n))
				parent_menu.add(remove_item)

				
				self.menu_targets.add(parent_menu)
				self.menu_targets.addSeparator()
				self.menu_targets.addSeparator()
		targets.dump(TARGETS_FILE, indent=4)

		add_item = JMenuItem("( + ) Add New Target...")
		add_item.setOpaque(True)
		add_item.setBackground(Color(204, 255, 204)) # light green
		add_item.setFont(Font("Monospaced", Font.BOLD, 12))
		add_item.addActionListener(self.add_target)
		self.menu_targets.add(add_item)
		self.menu_targets.addSeparator()


	def add_target(self, event):
		chooser = JFileChooser()
		if chooser.showOpenDialog(None) == JFileChooser.APPROVE_OPTION:
			file_path = chooser.getSelectedFile().getAbsolutePath()
			target_name = JOptionPane.showInputDialog(None, "Enter Target Name:", "New Target", JOptionPane.PLAIN_MESSAGE)
			if target_name:
				targets = jdks.load(TARGETS_FILE, ordered_dict=True, skipDuplicated=True) or jdks.JSON_DUPLICATE_KEYS({})
				targets.set(target_name, {"path": file_path, "enable": True})
				print("[TP-BCF] Added New Target: {}".format(target_name))
				targets.dump(TARGETS_FILE, indent=4)
				self.load_targets()


	def edit_target(self, target_name):
		targets = jdks.load(TARGETS_FILE, skipDuplicated=True)
		if targets:
			try:
				path = targets.get(target_name+"||path")["value"]
				file_obj = File(path)
				if not file_obj.exists():
					print("[TP-BCF] Target file does not exist: " + path)
					return

				if Desktop.isDesktopSupported():
					desktop = Desktop.getDesktop()
					desktop.open(file_obj)
				else:
					print("[TP-BCF] Desktop open not supported on this system.")

			except Exception as e:
				print("[TP-BCF] Error opening file: " + str(e))


	def remove_target(self, target_name):
		if JOptionPane.showConfirmDialog(None, "Are you sure to remove the target: {}?".format(target_name), "Confirm", JOptionPane.YES_NO_OPTION) != JOptionPane.YES_OPTION:
			return

		targets = jdks.load(TARGETS_FILE, ordered_dict=True, skipDuplicated=True)
		if targets:
			targets.delete(target_name)
			print("[TP-BCF] Deleted Target: {}".format(target_name))
			targets.dump(TARGETS_FILE, indent=4)
			self.load_targets()


	def get_burp_jframe(self):
		for frame in Frame.getFrames():
			if frame.isVisible() and frame.getTitle().startswith("Burp Suite"):
				return frame
		return None


	def extensionUnloaded(self):
		try:
			jMenuBar = self.get_burp_jframe().getJMenuBar()
			jMenuBar.remove(self.menu_button)
			jMenuBar.repaint()
		except:
			pass


	class AllToolsListener(ActionListener):
		def __init__(self, checkboxes): self.checkboxes = checkboxes
		def actionPerformed(self, event):
			state = event.getSource().isSelected()
			for cb in self.checkboxes: cb.setSelected(state)


	class IndividualToolListener(ActionListener):
		def __init__(self, all_checkbox, checkboxes): self.all_checkbox, self.checkboxes = all_checkbox, checkboxes
		def actionPerformed(self, event):
			all_selected = all(cb.isSelected() for cb in self.checkboxes)
			self.all_checkbox.setSelected(all_selected)


	class TargetCheckListener(ActionListener):
		def __init__(self, target_name, target_path, menu_bar): self.target_name, self.target_path, self.menu_bar = target_name, target_path, menu_bar
		def actionPerformed(self, event):
			targets = jdks.load(TARGETS_FILE, ordered_dict=True, skipDuplicated=True) or jdks.JSON_DUPLICATE_KEYS({})

			if event.getSource().isSelected():
				self.menu_bar.selected_targets.add(self.target_path)
				targets.update(self.target_name, {"path":self.target_path, "enable":True})
			else:
				self.menu_bar.selected_targets.discard(self.target_path)
				targets.update(self.target_name, {"path":self.target_path, "enable":False})

			targets.dump(TARGETS_FILE, indent=4)



class BurpExtender(IBurpExtender, IMessageEditorTabFactory, IHttpListener):
	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks

		self._helpers = callbacks.getHelpers()

		self.config_menu = MenuBar(self._callbacks)

		SwingUtilities.invokeLater(self.config_menu)

		callbacks.setExtensionName(EXTENSION_NAME + " v" + EXTENSION_VERSION)

		callbacks.registerMessageEditorTabFactory(self)

		callbacks.registerHttpListener(self)
	

	def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
		global ProcessMessage

		target = messageInfo.getHttpService().getHost() + ":" + str(messageInfo.getHttpService().getPort())
		url = str(messageInfo.getHttpService().getProtocol()) + "//" + target + self._helpers.analyzeRequest(messageInfo.getRequest()).getHeaders()[0].split(" ")[1]

		if messageIsRequest:
			if (self.config_menu.menu_all_encReq_item.getState() and toolFlag in [IBurpExtenderCallbacks.TOOL_SCANNER, IBurpExtenderCallbacks.TOOL_PROXY, IBurpExtenderCallbacks.TOOL_INTRUDER, IBurpExtenderCallbacks.TOOL_REPEATER, IBurpExtenderCallbacks.TOOL_EXTENDER]) \
			or (self.config_menu.menu_scanner_encReq_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_SCANNER) \
			or (self.config_menu.menu_proxy_encReq_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_PROXY) \
			or (self.config_menu.menu_intruder_encReq_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_INTRUDER) \
			or (self.config_menu.menu_repeater_encReq_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_REPEATER) \
			or (self.config_menu.menu_extender_encReq_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_EXTENDER):
				oriRequest = messageInfo.getRequest()
				newRequest = self._helpers.bytesToString(oriRequest)

				try:
					envs = jdks.load(ENV_FILE, skipDuplicated=True)
					if not envs:
						envs = jdks.JSON_DUPLICATE_KEYS({})
					envs = envs.getObject()
					envs.update(default_envs())

					if self.config_menu.menu_AutoRefresh_item.getState():
						ProcessMessage["Request"] =  []
						ProcessMessage["Response"] =  []
						CipherTab["EncryptRequest"] =  []
						CipherTab["DecryptRequest"] =  []
						CipherTab["EncryptResponse"] =  []
						CipherTab["DecryptResponse"] =  []

						for target_file in self.config_menu.selected_targets:
							if self.config_menu.menu_debug_mode_item.getState():
								print("[TP-BCF] " + target_file)
							JDKSObject = jdks.load(target_file, skipDuplicated=True, _isDebug_=True)
							if JDKSObject:
								if JDKSObject.get("ProcessMessage||Request")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									ProcessMessage["Request"] += JDKSObject.get("ProcessMessage||Request")["value"]
								
								if JDKSObject.get("ProcessMessage||Response")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									ProcessMessage["Response"] += JDKSObject.get("ProcessMessage||Response")["value"]

								if JDKSObject.get("CipherTab||EncryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["EncryptRequest"] += JDKSObject.get("CipherTab||EncryptRequest")["value"]

								if JDKSObject.get("CipherTab||DecryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["DecryptRequest"] += JDKSObject.get("CipherTab||DecryptRequest")["value"]

								if JDKSObject.get("CipherTab||EncryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["EncryptResponse"] += JDKSObject.get("CipherTab||EncryptResponse")["value"]

								if JDKSObject.get("CipherTab||DecryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["DecryptResponse"] += JDKSObject.get("CipherTab||DecryptResponse")["value"]

						if self.config_menu.menu_debug_mode_item.getState():
							print("ProcessMessage", ProcessMessage)
							print("CipherTab", CipherTab)


					for i in range(len(ProcessMessage["Request"])):
						match = True
						for pattern in ProcessMessage["Request"][i]["PATTERN"]:
							if not re.search(pattern, newRequest):
								match = False
								break

						if not re.search(ProcessMessage["Request"][i]["TARGET"], target): match = False

						if match:
							if self.config_menu.menu_debug_mode_item.getState():
								print("-"*128)
								print("["+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] [TP-BCF] Request (processHttpMessage): "+url)

							RequestParser = TP_HTTP_REQUEST_PARSER(newRequest, ordered_dict=True)
							O = list()

							local_vars = {
								"envs": envs,
								"RequestParser": RequestParser,
								"O": O
							}

							for j in range(len(ProcessMessage["Request"][i]["DATA"])):
								O.append("")

								if len(ProcessMessage["Request"][i]["DATA"][j]["CONDITION"]) == 0 or eval(ProcessMessage["Request"][i]["DATA"][j]["CONDITION"]):
									for output in ProcessMessage["Request"][i]["DATA"][j]["OUTPUT"]:
										LOOPVAR = output["LOOPVAR"]
										CONDITION = output["CONDITION"]
										if len(LOOPVAR) > 0:
											for LOOPDATA in safe_eval(LOOPVAR, local_vars=local_vars):
												if len(CONDITION) == 0 or safe_eval(CONDITION, local_vars=local_vars):
													local_vars["LOOPDATA"] = LOOPDATA
													if output["exec_func"]:
														safe_exec(output["ExprStmt"], local_vars=local_vars)
													else:
														O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)
														break
										else:
											if output["exec_func"]:
												safe_exec(output["ExprStmt"], local_vars=local_vars)
											else:
												O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)

								if self.config_menu.menu_debug_mode_item.getState():
									print("- O["+str(j)+"]: {}".format(repr(O[j])))

							RequestParser.request_headers.delete("X-TPBCF-ENABLED", case_insensitive=True)
							newRequest = RequestParser.unparse(update_content_length=True)
							break

					newRequest = self._helpers.stringToBytes(newRequest)
					messageInfo.setRequest(newRequest)
				except Exception as e:
					if self.config_menu.menu_debug_mode_item.getState():
						print("[TP-BCF] processHttpMessage - Request:", e)
					messageInfo.setRequest(oriRequest)
		else:
			if (self.config_menu.menu_all_decRes_item.getState() and toolFlag in [IBurpExtenderCallbacks.TOOL_SCANNER, IBurpExtenderCallbacks.TOOL_PROXY, IBurpExtenderCallbacks.TOOL_INTRUDER, IBurpExtenderCallbacks.TOOL_REPEATER, IBurpExtenderCallbacks.TOOL_EXTENDER]) \
			or (self.config_menu.menu_scanner_decRes_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_SCANNER) \
			or (self.config_menu.menu_proxy_decRes_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_PROXY) \
			or (self.config_menu.menu_intruder_decRes_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_INTRUDER) \
			or (self.config_menu.menu_repeater_decRes_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_REPEATER) \
			or (self.config_menu.menu_extender_decRes_item.getState() and toolFlag == IBurpExtenderCallbacks.TOOL_EXTENDER):
				oriResponse = messageInfo.getResponse()
				newResponse = self._helpers.bytesToString(oriResponse)

				try:
					envs = jdks.load(ENV_FILE, skipDuplicated=True)
					if not envs:
						envs = jdks.JSON_DUPLICATE_KEYS({})
					envs = envs.getObject()
					envs.update(default_envs())

					if self.config_menu.menu_AutoRefresh_item.getState():
						ProcessMessage["Request"] =  []
						ProcessMessage["Response"] =  []
						CipherTab["EncryptRequest"] =  []
						CipherTab["DecryptRequest"] =  []
						CipherTab["EncryptResponse"] =  []
						CipherTab["DecryptResponse"] =  []

						for target_file in self.config_menu.selected_targets:
							if self.config_menu.menu_debug_mode_item.getState():
								print("[TP-BCF] " + target_file)
							JDKSObject = jdks.load(target_file, skipDuplicated=True, _isDebug_=True)
							if JDKSObject:
								if JDKSObject.get("ProcessMessage||Request")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									ProcessMessage["Request"] += JDKSObject.get("ProcessMessage||Request")["value"]

								if JDKSObject.get("ProcessMessage||Response")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									ProcessMessage["Response"] += JDKSObject.get("ProcessMessage||Response")["value"]

								if JDKSObject.get("CipherTab||EncryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["EncryptRequest"] += JDKSObject.get("CipherTab||EncryptRequest")["value"]

								if JDKSObject.get("CipherTab||DecryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["DecryptRequest"] += JDKSObject.get("CipherTab||DecryptRequest")["value"]

								if JDKSObject.get("CipherTab||EncryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["EncryptResponse"] += JDKSObject.get("CipherTab||EncryptResponse")["value"]

								if JDKSObject.get("CipherTab||DecryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
									CipherTab["DecryptResponse"] += JDKSObject.get("CipherTab||DecryptResponse")["value"]
	
						if self.config_menu.menu_debug_mode_item.getState():
							print("ProcessMessage", ProcessMessage)
							print("CipherTab", CipherTab)


					for i in range(len(ProcessMessage["Response"])):
						match = True
						for pattern in ProcessMessage["Response"][i]["PATTERN"]:
							if not re.search(pattern, newResponse):
								match = False
								break

						if not re.search(ProcessMessage["Response"][i]["TARGET"], target): match = False

						if match:
							if self.config_menu.menu_debug_mode_item.getState():
								print("-"*128)
								print("["+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] [TP-BCF] Response (processHttpMessage): "+url)

							ResponseParser = TP_HTTP_RESPONSE_PARSER(newResponse, ordered_dict=True)
							O = list()

							local_vars = {
								"envs": envs,
								"ResponseParser": ResponseParser,
								"O": O
							}

							for j in range(len(ProcessMessage["Response"][i]["DATA"])):
								O.append("")

								if len(ProcessMessage["Response"][i]["DATA"][j]["CONDITION"]) == 0 or eval(ProcessMessage["Response"][i]["DATA"][j]["CONDITION"]):
									for output in ProcessMessage["Response"][i]["DATA"][j]["OUTPUT"]:
										LOOPVAR = output["LOOPVAR"]
										CONDITION = output["CONDITION"]
										if len(LOOPVAR) > 0:
											for LOOPDATA in safe_eval(LOOPVAR, local_vars=local_vars):
												if len(CONDITION) == 0 or safe_eval(CONDITION, local_vars=local_vars):
													local_vars["LOOPDATA"] = LOOPDATA
													if output["exec_func"]:
														safe_exec(output["ExprStmt"], local_vars=local_vars)
													else:
														O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)
														break
										else:
											if output["exec_func"]:
												safe_exec(output["ExprStmt"], local_vars=local_vars)
											else:
												O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)

								if self.config_menu.menu_debug_mode_item.getState():
									print("- O["+str(j)+"]: {}".format(repr(O[j])))

							newResponse = ResponseParser.unparse(update_content_length=True)
							break

					newResponse = self._helpers.stringToBytes(newResponse)
					messageInfo.setResponse(newResponse)
				except Exception as e:
					if self.config_menu.menu_debug_mode_item.getState():
						print("[TP-BCF] processHttpMessage - Response:", e)
					messageInfo.setResponse(oriResponse)


	def createNewInstance(self, controller, editable):
		return CipherMessageEditorTab(self, controller, editable)



class CipherMessageEditorTab(IMessageEditorTab):
	def __init__(self, extender, controller, editable):
		self._txtInput = extender._callbacks.createMessageEditor(controller, editable)
		self._extender = extender
		self.editable = editable


	def getUiComponent(self):
		return self._txtInput.getComponent()


	def getTabCaption(self):
		return EXTENSION_NAME + " v" + EXTENSION_VERSION


	def isEnabled(self, content, isRequest):
		global TARGET, CipherTab

		match = False
		if content:
			if self._extender.config_menu.menu_AutoRefresh_item.getState():
				ProcessMessage["Request"] =  []
				ProcessMessage["Response"] =  []
				CipherTab["EncryptRequest"] =  []
				CipherTab["DecryptRequest"] =  []
				CipherTab["EncryptResponse"] =  []
				CipherTab["DecryptResponse"] =  []

				for target_file in self._extender.config_menu.selected_targets:
					if self._extender.config_menu.menu_debug_mode_item.getState():
						print("[TP-BCF] " + target_file)
					JDKSObject = jdks.load(target_file, skipDuplicated=True, _isDebug_=True)
					if JDKSObject:
						if JDKSObject.get("ProcessMessage||Request")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
							ProcessMessage["Request"] += JDKSObject.get("ProcessMessage||Request")["value"]

						if JDKSObject.get("ProcessMessage||Response")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
							ProcessMessage["Response"] += JDKSObject.get("ProcessMessage||Response")["value"]

						if JDKSObject.get("CipherTab||EncryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
							CipherTab["EncryptRequest"] += JDKSObject.get("CipherTab||EncryptRequest")["value"]

						if JDKSObject.get("CipherTab||DecryptRequest")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
							CipherTab["DecryptRequest"] += JDKSObject.get("CipherTab||DecryptRequest")["value"]

						if JDKSObject.get("CipherTab||EncryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
							CipherTab["EncryptResponse"] += JDKSObject.get("CipherTab||EncryptResponse")["value"]

						if JDKSObject.get("CipherTab||DecryptResponse")["value"] != "JSON_DUPLICATE_KEYS_ERROR":
							CipherTab["DecryptResponse"] += JDKSObject.get("CipherTab||DecryptResponse")["value"]

				if self._extender.config_menu.menu_debug_mode_item.getState():
					print("ProcessMessage", ProcessMessage)
					print("CipherTab", CipherTab)

			if isRequest:
				newContent = self._extender._helpers.bytesToString(content)
				RequestParser = TP_HTTP_REQUEST_PARSER(newContent, ordered_dict=True)

				Host = RequestParser.request_headers.get("Host", case_insensitive=True)["value"]
				if Host != "JSON_DUPLICATE_KEYS_ERROR": TARGET = Host

				if RequestParser.request_headers.get("X-TPBCF-ENABLED", case_insensitive=True)["value"] != "JSON_DUPLICATE_KEYS_ERROR": return False

				DecryptRequest = CipherTab["DecryptRequest"]
				for i in range(len(DecryptRequest)):
					match = True
					for pattern in DecryptRequest[i]["PATTERN"]:
						if not re.search(pattern, newContent):
							match = False
							break

					if not re.search(DecryptRequest[i]["TARGET"], TARGET): match = False

					if match: break
				return match
			else:
				newContent = self._extender._helpers.bytesToString(content)
				ResponseParser = TP_HTTP_RESPONSE_PARSER(newContent, ordered_dict=True)

				if ResponseParser.response_headers.get("X-TPBCF-ENABLED", case_insensitive=True)["value"] != "JSON_DUPLICATE_KEYS_ERROR": return False

				DecryptResponse = CipherTab["DecryptResponse"]
				for i in range(len(DecryptResponse)):
					match = True
					for pattern in DecryptResponse[i]["PATTERN"]:
						if not re.search(pattern, newContent):
							match = False
							break

					if not re.search(DecryptResponse[i]["TARGET"], TARGET): match = False

					if match: break
				return match

		return match


	def setMessage(self, content, isRequest):
		self._txtInput.setMessage("", isRequest)
		self._isRequest = isRequest

		if content:
			envs = jdks.load(ENV_FILE, skipDuplicated=True)
			if not envs:
				envs = jdks.JSON_DUPLICATE_KEYS({})
			envs = envs.getObject()
			envs.update(default_envs())


			if isRequest:
				try:
					newContent = self._extender._helpers.bytesToString(content)
					DecryptRequest = CipherTab["DecryptRequest"]

					for i in range(len(DecryptRequest)):
						match = True
						for pattern in DecryptRequest[i]["PATTERN"]:
							if not re.search(pattern, newContent):
								match = False
								break

						if not re.search(DecryptRequest[i]["TARGET"], TARGET): match = False

						if match:
							if self._extender.config_menu.menu_debug_mode_item.getState():
								print("-"*128)
								print("["+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] [TP-BCF] Request (DecryptRequestTab)")

							RequestParser = TP_HTTP_REQUEST_PARSER(newContent, ordered_dict=True)
							O = list()

							local_vars = {
								"envs": envs,
								"RequestParser": RequestParser,
								"O": O
							}

							for j in range(len(DecryptRequest[i]["DATA"])):
								O.append("")

								if len(DecryptRequest[i]["DATA"][j]["CONDITION"]) == 0 or eval(DecryptRequest[i]["DATA"][j]["CONDITION"]):
									for output in DecryptRequest[i]["DATA"][j]["OUTPUT"]:
										LOOPVAR = output["LOOPVAR"]
										CONDITION = output["CONDITION"]
										if len(LOOPVAR) > 0:
											for LOOPDATA in safe_eval(LOOPVAR, local_vars=local_vars):
												if len(CONDITION) == 0 or safe_eval(CONDITION, local_vars=local_vars):
													local_vars["LOOPDATA"] = LOOPDATA
													if output["exec_func"]:
														safe_exec(output["ExprStmt"], local_vars=local_vars)
													else:
														O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)
														break
										else:
											if output["exec_func"]:
												safe_exec(output["ExprStmt"], local_vars=local_vars)
											else:
												O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)

								if self._extender.config_menu.menu_debug_mode_item.getState():
									print("- O["+str(j)+"]: {}".format(repr(O[j])))

							RequestParser.request_headers.update("X-TPBCF-ENABLED", True, case_insensitive=True, allow_new_key=True)
							newContent = RequestParser.unparse(update_content_length=True)
							break

					newContent = self._extender._helpers.stringToBytes(newContent)
					self._txtInput.setMessage(newContent, isRequest)
				except Exception as e:
					if self._extender.config_menu.menu_debug_mode_item.getState():
						print("[TP-BCF] CipherMessageEditorTab - DecryptRequest:", e)
			else:
				try:
					newContent = self._extender._helpers.bytesToString(content)
					DecryptResponse = CipherTab["DecryptResponse"]

					for i in range(len(DecryptResponse)):
						match = True
						for pattern in DecryptResponse[i]["PATTERN"]:
							if not re.search(pattern, newContent):
								match = False
								break

						if not re.search(DecryptResponse[i]["TARGET"], TARGET): match = False

						if match:
							if self._extender.config_menu.menu_debug_mode_item.getState():
								print("-"*128)
								print("["+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] [TP-BCF] Response (DecryptResponseTab)")

							ResponseParser = TP_HTTP_RESPONSE_PARSER(newContent, ordered_dict=True)
							O = list()

							local_vars = {
								"envs": envs,
								"ResponseParser": ResponseParser,
								"O": O
							}

							for j in range(len(DecryptResponse[i]["DATA"])):
								O.append("")

								if len(DecryptResponse[i]["DATA"][j]["CONDITION"]) == 0 or eval(DecryptResponse[i]["DATA"][j]["CONDITION"]):
									for output in DecryptResponse[i]["DATA"][j]["OUTPUT"]:
										LOOPVAR = output["LOOPVAR"]
										CONDITION = output["CONDITION"]
										if len(LOOPVAR) > 0:
											for LOOPDATA in safe_eval(LOOPVAR, local_vars=local_vars):
												if len(CONDITION) == 0 or safe_eval(CONDITION, local_vars=local_vars):
													local_vars["LOOPDATA"] = LOOPDATA
													if output["exec_func"]:
														safe_exec(output["ExprStmt"], local_vars=local_vars)
													else:
														O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)
														break
										else:
											if output["exec_func"]:
												safe_exec(output["ExprStmt"], local_vars=local_vars)
											else:
												O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)

								if self._extender.config_menu.menu_debug_mode_item.getState():
									print("- O["+str(j)+"]: {}".format(repr(O[j])))

							ResponseParser.response_headers.update("X-TPBCF-ENABLED", True, case_insensitive=True, allow_new_key=True)
							newContent = ResponseParser.unparse(update_content_length=True)
							break

					newContent = self._extender._helpers.stringToBytes(newContent)
					self._txtInput.setMessage(newContent, isRequest)
				except Exception as e:
					if self._extender.config_menu.menu_debug_mode_item.getState():
						print("[TP-BCF] CipherMessageEditorTab - DecryptResponse:", e)


	def getMessage(self):
		content = self._txtInput.getMessage()
		if self.editable and content:
			envs = jdks.load(ENV_FILE, skipDuplicated=True)
			if not envs:
				envs = jdks.JSON_DUPLICATE_KEYS({})
			envs = envs.getObject().update(default_envs())


			if self._isRequest:
				newContent = self._extender._helpers.bytesToString(content)
				EncryptRequest = CipherTab["EncryptRequest"]

				for i in range(len(EncryptRequest)):
					match = True
					for pattern in EncryptRequest[i]["PATTERN"]:
						if not re.search(pattern, newContent):
							match = False
							break

					if not re.search(EncryptRequest[i]["TARGET"], TARGET): match = False

					if match:
						if self._extender.config_menu.menu_debug_mode_item.getState():
							print("-"*128)
							print("["+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] [TP-BCF] Request (EncryptRequestTab)")

						RequestParser = TP_HTTP_REQUEST_PARSER(newContent, ordered_dict=True)
						O = list()

						local_vars = {
							"envs": envs,
							"RequestParser": RequestParser,
							"O": O
						}

						for j in range(len(EncryptRequest[i]["DATA"])):
							O.append("")

							if len(EncryptRequest[i]["DATA"][j]["CONDITION"]) == 0 or eval(EncryptRequest[i]["DATA"][j]["CONDITION"]):
								for output in EncryptRequest[i]["DATA"][j]["OUTPUT"]:
									LOOPVAR = output["LOOPVAR"]
									CONDITION = output["CONDITION"]
									if len(LOOPVAR) > 0:
										for LOOPDATA in safe_eval(LOOPVAR, local_vars=local_vars):
											if len(CONDITION) == 0 or safe_eval(CONDITION, local_vars=local_vars):
												local_vars["LOOPDATA"] = LOOPDATA
												if output["exec_func"]:
													safe_exec(output["ExprStmt"], local_vars=local_vars)
												else:
													O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)
													break
									else:
										if output["exec_func"]:
											safe_exec(output["ExprStmt"], local_vars=local_vars)
										else:
											O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)

							if self._extender.config_menu.menu_debug_mode_item.getState():
								print("- O["+str(j)+"]: {}".format(repr(O[j])))

						RequestParser.request_headers.delete("X-TPBCF-ENABLED", case_insensitive=True)
						newContent = RequestParser.unparse(update_content_length=True)
						break

				newContent = self._extender._helpers.stringToBytes(newContent)
				return newContent
			else:
				newContent = self._extender._helpers.bytesToString(content)
				EncryptResponse = CipherTab["EncryptResponse"]

				for i in range(len(EncryptResponse)):
					match = True
					for pattern in EncryptResponse[i]["PATTERN"]:
						if not re.search(pattern, newContent):
							match = False
							break

					if not re.search(EncryptResponse[i]["TARGET"], TARGET): match = False

					if match:
						if self._extender.config_menu.menu_debug_mode_item.getState():
							print("-"*128)
							print("["+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] [TP-BCF] Response (EncryptResponseTab)")

						ResponseParser = TP_HTTP_RESPONSE_PARSER(newContent, ordered_dict=True)
						O = list()

						local_vars = {
							"envs": envs,
							"ResponseParser": ResponseParser,
							"O": O
						}

						for j in range(len(EncryptResponse[i]["DATA"])):
							O.append("")

							if len(EncryptResponse[i]["DATA"][j]["CONDITION"]) == 0 or eval(EncryptResponse[i]["DATA"][j]["CONDITION"]):
								for output in EncryptResponse[i]["DATA"][j]["OUTPUT"]:
									LOOPVAR = output["LOOPVAR"]
									CONDITION = output["CONDITION"]
									if len(LOOPVAR) > 0:
										for LOOPDATA in safe_eval(LOOPVAR, local_vars=local_vars):
											if len(CONDITION) == 0 or safe_eval(CONDITION, local_vars=local_vars):
												local_vars["LOOPDATA"] = LOOPDATA
												if output["exec_func"]:
													safe_exec(output["ExprStmt"], local_vars=local_vars)
												else:
													O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)
													break
									else:
										if output["exec_func"]:
											safe_exec(output["ExprStmt"], local_vars=local_vars)
										else:
											O[j] = safe_eval(output["ExprStmt"], local_vars=local_vars)

							if self._extender.config_menu.menu_debug_mode_item.getState():
								print("- O["+str(j)+"]: {}".format(repr(O[j])))

						ResponseParser.response_headers.delete("X-TPBCF-ENABLED", case_insensitive=True)
						newContent = ResponseParser.unparse(update_content_length=True)
						break

				newContent = self._extender._helpers.stringToBytes(newContent)
				return newContent


	def isModified(self):
		return self.editable


	def getSelectedData(self):
		return self._txtInput.getSelectedData()