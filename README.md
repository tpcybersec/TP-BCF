<div align="center">
	<img src="https://raw.githubusercontent.com/TPCyberSec/TP-BCF/refs/heads/main/assets/TP-BCF.png" height=200>
	<h1>TP-BCF (Burp Cipher Framework)</h1>
	<i>A framework for intercepting HTTP Requests/ Responses and creating a Cipher tab to perform Encryption/ Decryption based on predefined configurations</i>
	<br><br>
	<a href="https://github.com/TPCyberSec/TP-BCF/releases/"><img src="https://img.shields.io/github/release/TPCyberSec/TP-BCF" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/downloads/TPCyberSec/TP-BCF/total" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/stars/TPCyberSec/TP-BCF" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/forks/TPCyberSec/TP-BCF" height=30></a>
	<a href="https://github.com/TPCyberSec/TP-BCF/issues?q=is%3Aopen+is%3Aissue"><img src="https://img.shields.io/github/issues/TPCyberSec/TP-BCF" height=30></a>
	<a href="https://github.com/TPCyberSec/TP-BCF/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/TPCyberSec/TP-BCF" height=30></a>
</div>

---
# ✨ Features
- Intercepts and rewrites HTTP Request/ Response messages based on predefined configurations
- Cipher Tab for manual Encryption/ Decryption operations
- Supports built-in symmetric, asymmetric, hash-based cryptography and Common utilities
- Easily extendable via JSON configuration files

---
# 🛠️ Installation
#### Requirements:
- Burp Suite Professional or Community
- Jython Standalone JAR (for Python-based extensions). You can download it from: https://www.jython.org/download
- `python` version 3 must be installed and added to the `PATH`

#### Steps to Install:
1. Clone the repository
```console
git clone https://github.com/TPCyberSec/TP-BCF.git --branch <Branch/Tag>
```
2. Open **Burp Suite**
3. Go to **Extender** → **Options** tab
4. Under **Python Environment**, click **Select file...** and choose the downloaded `jython-standalone-<version>.jar`
5. Switch to the `Extensions` tab
6. Click `Add`
- In the `Extension type`, select: `Python`
- In the `Extension file`, choose the `TP-BCF.py` file from the cloned repository
7. Click `Next` to load the extension

Once loaded successfully, you should see a new `TP-BCF` menu tab on the top menu bar of Burp Suite

---
# 🧩 Built-in Variables and Modules/ Functions
## Built-in Variables
### ([TP_HTTP_REQUEST_PARSER](https://github.com/TPCyberSec/TP-HTTP-Request-Response-Parser#tp_http_request_parser)) RequestParser
_Provides properties to access details of the current HTTP Request. Use these attributes to extract method, path, headers, cookies, body, etc. for analysis, condition checking, or data processing in your rules_
- `RequestParser.request_method`: HTTP method (GET, POST, etc.)
- `RequestParser.request_paths`: Request path parts as JSON_Duplicate_Keys object
- `RequestParser.request_queryParams`: Query parameters as JSON_Duplicate_Keys object
- `RequestParser.request_fragment`: URL fragment
- `RequestParser.request_httpVersion`: HTTP version
- `RequestParser.request_headers`: Request headers as JSON_Duplicate_Keys object
- `RequestParser.request_cookies`: Request cookies as JSON_Duplicate_Keys object
- `RequestParser.request_body`: Request body (string or parsed object) as JSON_Duplicate_Keys object

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### ([TP_HTTP_RESPONSE_PARSER](https://github.com/TPCyberSec/TP-HTTP-Request-Response-Parser#tp_http_response_parser)) ResponseParser
_Provides properties to access details of the current HTTP Response. Use these attributes to extract status code, headers, cookies, body, etc. for analysis, transformation, or validation in your rules_
- `ResponseParser.response_httpVersion`: HTTP version
- `ResponseParser.response_statusCode`: Status code
- `ResponseParser.response_statusText`: Status text
- `ResponseParser.response_headers`: Response headers as JSON_Duplicate_Keys object
- `ResponseParser.response_cookies`: Response cookies as JSON_Duplicate_Keys object
- `ResponseParser.response_body`: Response body as JSON_Duplicate_Keys object

**Usage scope in the configuration file:**
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### (dict) envs
_A dictionary containing default environment variables such as keys, IV, salt, and password. Use these for cryptographic operations or as parameters in your rules. You can add new custom environment variables through the MenuBar "**Environment Variables > ( + ) Add New Variable...**"._
```
# Default environment variables
envs['defaultRSA2048PublicKey']
envs['defaultRSA2048PrivateKey']
envs['defaultEC256r1PublicKey']
envs['defaultEC256r1PrivateKey']
envs['defaultSecretKey']
envs['defaultIV']
envs['defaultSalt']
envs['defaultPassword']

# Custom Environment Variables:
env['your-custom-variable']
...
```

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### TEMP
_A temporary dictionary for storing intermediate values or results during rule execution_

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### fromTool
_Define the tool name from which the request was sent. It is used in the Request/ Response configuration of HttpMessage. The value of fromTool can be: Scanner, Proxy, Intruder, Repeater, Extender_

**Usage scope in the configuration file:**
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`

---
### O
_A list for storing temporary results of expressions or calculations in each processing step. Only used within the Index of the current DATA and cannot be shared with the Index of another DATA_

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### LOOPDATA
_A variable used in loops, holding the current item being iterated in a rule. Only used within the Index of the current OUTPUT and cannot be shared with the Index of another OUTPUT_

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
## Built-in Modules/ Functions
### [TP_HTTP_REQUEST_PARSER](https://github.com/TPCyberSec/TP-HTTP-Request-Response-Parser#tp_http_request_parser) module
_Module for parsing and manipulating HTTP request data_

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### [TP_HTTP_RESPONSE_PARSER](https://github.com/TPCyberSec/TP-HTTP-Request-Response-Parser#tp_http_response_parser) module
_Module for parsing and manipulating HTTP response data_

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### [jdks](https://github.com/TPCyberSec/json-duplicate-keys) library
_Flatten/ Unflatten and Load(s)/ Dump(s) JSON File/ Object with Duplicate Keys_

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### re library
_Python's built-in regular expression library_

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### Utils module
**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
#### Utils.timestamp(length :int) -> int
```
Utils.timestamp(10)
# OUTPUT: 1732726800
```

---
#### Utils.uuid(version :int) -> str
```
Utils.uuid(4)
# OUTPUT: 'e0db37ce-3296-4253-a3ca-be43bc80073b'
```

---
#### Utils.RandomNumber(min :int, max :int) -> int
```
Utils.RandomNumber(0, 1000)
# OUTPUT: 465
```

---
#### Utils.RandomString(length :int, charsets :str=None) -> str
```
Utils.RandomString(10)
# OUTPUT: 'Wz<:1<.YSC'
```

---
#### Utils.toUTF8_Overlong(message: str, numBytes: int=2) -> byte
```
Utils.toUTF8_Overlong('TPCyberSec', numBytes=2)
# OUTPUT: b'\xc1\x94\xc1\x90\xc1\x83\xc1\xb9\xc1\xa2\xc1\xa5\xc1\xb2\xc1\x93\xc1\xa5\xc1\xa3'
```

---
#### Utils.toUTF16(message: str, type: str="LE") -> byte
```
Utils.toUTF16('TPCyberSec')
# OUTPUT: b'T\x00P\x00C\x00y\x00b\x00e\x00r\x00S\x00e\x00c\x00'
```

---
#### Utils.toUTF32(message: str, type: str="LE") -> byte
```
Utils.toUTF32('TPCyberSec')
# OUTPUT: b'T\x00\x00\x00P\x00\x00\x00C\x00\x00\x00y\x00\x00\x00b\x00\x00\x00e\x00\x00\x00r\x00\x00\x00S\x00\x00\x00e\x00\x00\x00c\x00\x00\x00'
```

---
#### Utils.Str2Hex(message :str) -> str
```
Utils.Str2Hex('TPCyberSec')
# OUTPUT: '54504379626572536563'
```

---
#### Utils.Hex2Str(message :str) -> str
```
Utils.Hex2Str('54504379626572536563')
# OUTPUT: 'TPCyberSec'
```

---
#### Utils.base64Encode(message :str) -> str
```
Utils.base64Encode('TPCyberSec')
# OUTPUT: 'VFBDeWJlclNlYw=='
```

---
#### Utils.base64Decode(message :str) -> str
```
Utils.base64Decode('VFBDeWJlclNlYw==')
# OUTPUT: 'TPCyberSec'
```

---
#### Utils.base64UrlEncode(message :str) -> str
```
Utils.base64UrlEncode('TPCyberSec')
# OUTPUT: 'VFBDeWJlclNlYw'
```

---
#### Utils.base64UrlDecode(message :str) -> str
```
Utils.base64UrlDecode('VFBDeWJlclNlYw')
# OUTPUT: 'TPCyberSec'
```

---
#### Utils.UrlEncode(message :str) -> str
```
Utils.UrlEncode('TP Cyber Security')
# OUTPUT: 'TP%20Cyber%20Security'
```

---
#### Utils.UrlDecode(message :str) -> str
```
Utils.UrlDecode('TP%20Cyber%20Security')
# OUTPUT: 'TP Cyber Security'
```

---
#### Utils.HTMLEncode(message: str, type: str="hex", padding: int=0) -> str
```
Utils.HTMLEncode('TPCyberSec')
# OUTPUT: '&#x54;&#x50;&#x43;&#x79;&#x62;&#x65;&#x72;&#x53;&#x65;&#x63;'

Utils.HTMLEncode('TPCyberSec', type="dec")
# OUTPUT: '&#84;&#80;&#67;&#121;&#98;&#101;&#114;&#83;&#101;&#99;'
```

---
#### Utils.XML2JSON(message: str, ordered_dict: bool=False) -> dict
```
xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>'''

Utils.XML2JSON(xml_string)
# OUTPUT: {'note': {'to': {'#text': 'Tove'}, 'from': {'#text': 'Jani'}, 'heading': {'#text': 'Reminder'}, 'body': {'#text': "Don't forget me this weekend!"}}}
```

---
#### Utils.JSON2XML(message: dict) -> str
```
json_object = {'note': {'to': {'#text': 'Tove'}, 'from': {'#text': 'Jani'}, 'heading': {'#text': 'Reminder'}, 'body': {'#text': "Don't forget me this weekend!"}}}
Utils.JSON2XML(json_object)
# OUTPUT: <?xml version="1.0" encoding="UTF-8"?><note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don&apos;t forget me this weekend!</body></note>
```

---
### MFA_Generator
**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
#### MFA_Generator.TOTP(secretKey: str, digits=6: int, period=30: int) -> str
_Generating the TOTP code_
```
MFA_Generator.TOTP("JBSWY3DPEHPK3PXP")
# OUTPUT: '862642'
```

---
#### MFA_Generator.HOTP(secretKey: str, counter: int, digits=6: int) -> str
_Generating the HOTP code_
```
MFA_Generator.HOTP("JBSWY3DPEHPK3PXP", 1)
# OUTPUT: '996554'
```

---
### Nonce_Generator
**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
#### Nonce_Generator.WordPress_Nonce(nonce_action: str, WORDPRESS_NONCE_KEY: str, WORDPRESS_NONCE_SALT: str, user_id=0: int, wordpress_logged_in_COOKIE="": str, DAY_IN_SECONDS=24*60*60: int) -> str
_Generating the WordPress Nonce_
```
action = "wp-rest"
NONCE_KEY = "Y9(H0]_u8BA:^or^<^4>AM@EkgnAm`{Mpsq*H!Z-?8 OHe6ITmPY6kQSai)y3w{}"
NONCE_SALT = "xV&%-Ji<,`Clp+|bqt9<c%JrGpq!EiMy///`z0+<D1F<E%H14mha9Csm<TH;~TfH"

Nonce_Generator.WordPress_Nonce(nonce_action=action, WORDPRESS_NONCE_KEY=NONCE_KEY, WORDPRESS_NONCE_SALT=NONCE_SALT)
# OUTPUT: `ac06630f78`
```

---
### QR_Generator
_(Un)parsing QR Code: VietQR (TAG 38), MoMo (TAG 38), VNPAYQR (TAG 26), KHQR\_Individual (TAG 29), KHQR\_Corporate (TAG 30), ThaiQR\_CREDIT\_TRANSFER (TAG 29), ThaiQR\_BILL\_PAYMENT (TAG 30)_
```
QR_String = "00020101021230340009nbcb@devb01090000001230204DEVB520459995303840540115802KH5912Coffee Klang6010Phnom Penh62300314Coffe Klang0010708A60086679917001316418876882756304CE7C"

QRObj = QR_Generator.initQR("KHQR_Corporate").parse(QR_String)
QRObj.dumps()
# OUTPUT: {"PayloadFormatIndicator": "01", "PointOfInitiationMethod": "12", "MerchantAccountInformation": {"BakongAccountID": "nbcb@devb", "MerchantID": "000000123", "AcquiringBank": "DEVB"}, "MerchantCategoryCode": "5999", "TransactionCurrency": "840", "TransactionAmount": "1", "CountryCode": "KH", "MerchantName": "Coffee Klang", "MerchantCity": "Phnom Penh", "AdditionalDataFieldTemplate": {"StoreLabel": "Coffe Klang001", "TerminalLabel": "A6008667"}, "CRC": "CE7C", "Timestamp": {"timestamp": "1641887688275"}}

QRObj.update("TransactionAmount", "1000")
QR_Generator.initQR("KHQR_Corporate").unparse(QRObj)
# OUTPUT: '00020101021230340009nbcb@devb01090000001230204DEVB520459995303840540410005802KH5912Coffee Klang6010Phnom Penh62300314Coffe Klang0010708A600866799170013164188768827563043ECD'
```

**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
### Crypto.Symmetric modules
**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
#### AESCipher(algorithm :str, provider :str=None).encrypt(PlainText :str, SECRET_KEY :str, IV :str=None, GCM_Tag :int=128) -> str
```
AESCipher('AES/ECB/NoPadding').encrypt('TPCyberSec      ', 'TPCSTPCSTPCSTPCS')
# OUTPUT: 'BE1cSAcGFP7A3U6KWBgN+A=='

AESCipher('AES/ECB/PKCS5Padding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS')
# OUTPUT: 'b0QZKUuy5xDkhnVjw6cIng=='

AESCipher('AES/CBC/NoPadding').encrypt('TPCyberSec      ', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'qw0WmEyafuONfm62t7NjVg=='

AESCipher('AES/CBC/PKCS5Padding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'WOEIZNG6H+sATfvrjmAWcQ=='

AESCipher('AES/CFB/NoPadding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'dOZDp/9KqFmRtA=='

AESCipher('AES/CFB/PKCS5Padding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'dOZDp/9KqFmRtBfquij1vQ=='

AESCipher('AES/OFB/NoPadding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'dOZDp/9KqFmRtA=='

AESCipher('AES/OFB/PKCS5Padding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'dOZDp/9KqFmRtBfquij1vQ=='

AESCipher('AES/GCM/NoPadding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'e1I2J7qTmKUFsyElw7Y+jQkbAbuyhv4gimI='

AESCipher('AES/CTR/NoPadding').encrypt('TPCyberSec', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'dOZDp/9KqFmRtA=='
```

---
#### AESCipher(algorithm :str, provider :str=None).decrypt(CipherText :str, SECRET_KEY :str, IV :str=None, GCM_Tag :int=128) -> str
```
AESCipher('AES/ECB/NoPadding').decrypt('\x04M\\H\x07\x06\x14\xfe\xc0\xddN\x8aX\x18\r\xf8', 'TPCSTPCSTPCSTPCS')
# OUTPUT: 'TPCyberSec      '

AESCipher('AES/ECB/NoPadding').decrypt('oD\x19)K\xb2\xe7\x10\xe4\x86uc\xc3\xa7\x08\x9e', 'TPCSTPCSTPCSTPCS')
# OUTPUT: 'TPCyberSec\x06\x06\x06\x06\x06\x06'

AESCipher('AES/CBC/NoPadding').decrypt('\xab\r\x16\x98L\x9a~\xe3\x8d~n\xb6\xb7\xb3cV', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec      '

AESCipher('AES/CBC/PKCS5Padding').decrypt('X\xe1\x08d\xd1\xba\x1f\xeb\x00M\xfb\xeb\x8e`\x16q', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec'

AESCipher('AES/CFB/NoPadding').decrypt('t\xe6C\xa7\xffJ\xa8Y\x91\xb4', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec'

AESCipher('AES/CFB/PKCS5Padding').decrypt('t\xe6C\xa7\xffJ\xa8Y\x91\xb4\x17\xea\xba(\xf5\xbd', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec'

AESCipher('AES/OFB/NoPadding').decrypt('t\xe6C\xa7\xffJ\xa8Y\x91\xb4', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec'

AESCipher('AES/OFB/PKCS5Padding').decrypt('t\xe6C\xa7\xffJ\xa8Y\x91\xb4\x17\xea\xba(\xf5\xbd', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec'

AESCipher('AES/GCM/NoPadding').decrypt("{R6'\xba\x93\x98\xa5\x05\xb3!%\xc3\xb6>\x8d\t\x1b\x01\xbb\xb2\x86\xfe \x8ab", 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec'

AESCipher('AES/CTR/NoPadding').decrypt('t\xe6C\xa7\xffJ\xa8Y\x91\xb4', 'TPCSTPCSTPCSTPCS', '0123456789012345')
# OUTPUT: 'TPCyberSec'
```

---
#### DESCipher(algorithm :str, provider :str=None).encrypt(PlainText :str, SECRET_KEY :str, IV :str=None) -> str
```
DESCipher('DES/ECB/NoPadding').encrypt('TPCyberSec      ', 'TPCSTPCS', '01234567')
# OUTPUT: 'RHtVWhhDa8yAECpwfwl/OQ=='
```

---
#### DESCipher(algorithm :str, provider :str=None).decrypt(CipherText :str, SECRET_KEY :str, IV :str=None) -> str
```
DESCipher('DES/ECB/NoPadding').decrypt('D{UZ\x18Ck\xcc\x80\x10*p\x7f\t\x7f9', 'TPCSTPCS', '01234567')
# OUTPUT: 'TPCyberSec      '
```

---
### Crypto.Asymmetric modules
**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
#### RSACipher(algorithm :str, provider :str=None).encrypt(PlainText :str, PublicKey :str=None, PrivateKey :str=None) -> str
```
PublicKey = '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuTwspB6ubxVDBIb7IL7sSinHDmZLk/7RYzOWzVmLZo7dzBKiOmAbvFMMGRXFZ/37eThQ7VP31qe6MCH7PhtuP+KKOFpfgQc3O9umo78Qut4NGuCYNiuRrRx2jv1KESS+zIxllelx/JmEbtrME3boMZJ7W/y/SL8dfhYuGZYuqrGOe2ZRwekWkxAUJlAlHT/keDU8qU3oGDgVIn6Ck5MW0o8yBoMsm7o1LfvAGdt5jdxATXy1pzIi3Tr/bLVVkOPmaYrmRQ1McQLSekGA0+hn/MSMTIKRBA4JtSLaQ7YPZQPqwlvYm56958Lr8FPcQ7dz3KXWRY5wG+KSf+3vWnRZ3QIDAQAB-----END PUBLIC KEY-----'
PrivateKey = '-----BEGIN PRIVATE KEY-----MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5PCykHq5vFUMEhvsgvuxKKccOZkuT/tFjM5bNWYtmjt3MEqI6YBu8UwwZFcVn/ft5OFDtU/fWp7owIfs+G24/4oo4Wl+BBzc726ajvxC63g0a4Jg2K5GtHHaO/UoRJL7MjGWV6XH8mYRu2swTdugxkntb/L9Ivx1+Fi4Zli6qsY57ZlHB6RaTEBQmUCUdP+R4NTypTegYOBUifoKTkxbSjzIGgyybujUt+8AZ23mN3EBNfLWnMiLdOv9stVWQ4+ZpiuZFDUxxAtJ6QYDT6Gf8xIxMgpEEDgm1ItpDtg9lA+rCW9ibnr3nwuvwU9xDt3PcpdZFjnAb4pJ/7e9adFndAgMBAAECggEAAQJP5/D22EoQXGTz10DS/rBtkimCfeLkdxrf1myHct6SXLs5QQInBIabSUOyGJfsl8NzxWcwsW2meP6mZLc3iYeNYzMy0/wbE+tlY/z1dV8iSSQyEBF6sKu4BZ1hmuhNVcXqA8AKy+p2Kzhr5is+po56t4yP6jCIU5iBVchYprtggIeLUDAKIGterKEYxJt/N8pdJ0oGhx4cNxcRBDylqdm0HJphyP19BtBOsFtdT9cN6khNpsWGl7UirvlI8eoJxfkXzSgRLn0XoZhl1gDKAD9XCWnII9nzZyINUY1ICG2fISMMGGCNs9YmaY0wzMkhNvty8fPoWH+XrvNyomxIQQKBgQDiMQqPsRYZEw51CsGyyJFALHUfCxsLv6lXeFgCzBY74rksF4CrrNR1rcrvbMe06P54el+dtGevnpb+C1x/iFUkncGW6hNZii/dpKlxUvFTnYYWAITOiOJltDliFlXt7jCZEkGO9WcYRmTibve3pgjxB79MxEo4bJQCRSHTd6ZaLQKBgQDRpWUxaA5IdwuX7/pxG9ekFvxkJCpjDj14rkA832SLs1Zoq/d4D6/0WTp+c6wHL7fzU1DFbgCwB560ktlAvI77J6tapl1hps6RYh9H3bz+Hb6d6eFlhdyUKuTX1XXw6RcK3pYtYOltavl3bwAal/7TEKjrdS59qwx2BlsbQvQ8cQKBgQCHjjRyIQLJTC5h3mxvJNxHxVz7mcA/rkFidnDoXD8G7L1ku0EVoaJCVEFGc77LoMbAlTYwYSmyiiybW1u34pCEPTcDpoyqILLG9iPGEpsmLUVqci0lScvEf9nT+ubMjO77DYHUlyWN2sIjIbW7jfnV2XrAGvMQFaIuKhg3j4FWkQKBgQCYfp2QBae2EFnviBD864q9AjdOxHvMl9QhD2cMoFZrw+SLuOMGgyqzK6B/0LYGeDBvH2B2a+C2KqTHprW/ACllCWL8Sl1MpeBGIkCsrt9FXO+FwFVC2s8rO9RAJzZmKbaoImbM1VyWSaTyulwx+/PRJaIpu5A4uw4SX+cvelFcEQKBgHz2GicI/2cgYlRaeeR8tDSrfVNkhkF1qQZpC3GlTLMjmzZQzLXkjxvYRjNfSJaTZ9CMlaD1PFnqu7Uk9KhUwkClGnSsvFBO2MrRh6P32XS5eDVoP7jZ1pk5/dvuB1RSJqLT63FRaBi8XPSPeT/9po9lCfipK2tlNnggFMPZf3qQ-----END PRIVATE KEY-----'

RSACipher('RSA/ECB/PKCS1Padding').encrypt('TPCyberSec', PublicKey=PublicKey)
# OUTPUT: 'AN3W2xqBkr87cl5lgw11HSgRXFJMoBlsNtXvRZHEGezrQVZrI6vp5lJdt0ZrAvwRqKYmw5jQHP1t55aCtT0erTNDbax++DThL64LfVYHmjwnC+/hEyv9S4S0W5UZd/8RAqP0LBWXYe5jp5fQu0TlUlrfBlhXy5ngs2Exmiz/5ggvb9dmVVs/IsXy8h2nNFC5JMqixX9w9wrvU3tzkjuP9PwIpPAAraH+SNavV8WbhuDMfmV5YVQABr5G5H0UW1pyAHk+hUhnE++nN6TAgxaP+nNu9fheBEku15oCF8sN4VpnqZonynau4I43QfWnLDByZLaEbqFc4Qh2cDKaojHYpg=='

RSACipher('RSA/ECB/PKCS1Padding').encrypt('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'QHxZIo5hRnsMnmhZJalYEGR7Aa7IHTtJ/D4ZsRaIVgYnUwHDGFMvXKAPva/+9xqqkjdKMrLHTB/C8kCxoBE/9iP7F7FAfgd7hcnu4mL3fbdVYgcvUyOPJwFxSSSRl5twiqGv/MXns9jsG+0qm+W4BxRnZu8a4JufdIEZ/8Qmt6NB0je9lT4+/tqAdbiwuYT+0MIGTo4MsGsTkbmMy957C72FQa1v2NQYaSsFSQegpgRdFD4VSfI0aNJrQs28a/j4bFrtwz2VtIqW+bWtPib/woj2FTaWgH72HpoTnxwPbtwuonJKiLXzMSiCorwUpe0TA+jZ2sAVHpDkftbu+8IajA=='

RSACipher('RSA/ECB/NoPadding').encrypt('TPCyberSec', PublicKey=PublicKey)
# OUTPUT: 'f48TeHLdtxuaH0EvozopEciNK0E5hsHAFqVeVSO1mc+KHEBNUvSzJAnvOVz2YRgXtdCIrcGjK9wUOThWzgE947t13mlHspvncJTrmm+CLX0tJMY8EGVZR8312soiNS8oOKBG4GmrVsKuAo46KTyDtL0SPeupr8VeUhtXdR+YtA252PJSrDWDM9iak027yL+OIqGjY8vZbDG9Str2bgKjuJZEYMQqZ31tXpRPrgObEzp2z1NidDBINgA3BQXI4k59wtKJben8jkz0i8gww2mAOXYRpvoIwgQXhQJKHsb5cmfgHNsiMQicS+bZwCAT+ETypiVCVUe0EYWvKE7h+mtd0A=='

RSACipher('RSA/ECB/NoPadding').encrypt('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'Dmo2o4HZhuX3EhsaxOaoLH86olhmfmsLpIAW4SXQcNqnhZOOzpP4TCLW4cllo4Y3h6oAA7tJ7ZpFYzFiS4NObllTSPse8fnftyK9UzQdxl/9FkCxSZHGPQEP5ln6fAdnWg5XmPpsF1qA+brBUzTcP2YKEv6dw/r19SyO8wEpa/jBglv64MurX9wY1BhTE7glm5OiIJU90Jh9q91aacNZ8+Q8hAcec4/gX7uArDD1rjfLqcjr84pZab3RLNKN0/xiAhQ+BVJKLs/cw66yTscSSAQHq7Pc5jwBCT59Y4GpbQz9fbT5wgk90ZnUROQT9PdGSckgivshaqzTJG+VD6GD7Q=='

RSACipher('RSA/ECB/OAEPPadding').encrypt('TPCyberSec', PublicKey=PublicKey, OAEPHashAlg='SHA-256', MGFHashAlg='MGF1')
# OUTPUT: 'jewX//32JWMcVFi19BvTpyuLS+/5yb1CURbH+s8WTuF1aINwIkVurmWxqAAGTJil8UVJUxjnnNvvRfVhJHXEe6hqscrlUfrZDe0L7vmh5fxEKWFC3X0EF6QY8Lua0B7TiKecBVbXIif7sFAcmoGOJ3kE4cuZdtQvm1qCMR5mdoyRBslLmnFZREl5F8RaIA72kFRBQgV+icH/kAttnCOUhXSc6nX+fauR92Zoknm9GUY4r/Y1oCpGqUDTr12r6fOuVYN6w7m7XwBkqPtAtSt8CSR9i0IYDQdrJsbZk8OcCXo+csdEMQciy+86cAQC1MJfl7hl1unaTTiCzv8f++6hbQ=='

RSACipher('RSA/ECB/OAEPWithSHA-1AndMGF1Padding').encrypt('TPCyberSec', PublicKey=PublicKey, OAEPHashAlg='SHA-1', MGFHashAlg='MGF1')
# OUTPUT: 'SwWgRSLqShe4nRgFjEzpNNMfn0eEOorhYp3Azq55agAvCRx7q3GrK0XVr2UnkugF6AQkNx1vwb34m68pe1HzUIu4PH6wdXf921Hw2tgCvlT6SWWwbEGJmHH4UetfUMPKQPLvN3hGSfuvvjRb3VCfH/muEwGSKArpQMm+88pDtsI6Uxl/pnmWwgeHzf0/JiR3ZIl8Tbob42O4C9L5BhLHMxNZtUMpDQWndOLkCs4inI5qu6LBsRqYCZI/ijD8ofz5EbwuOSeuhVK++prD83/UrSXIj+91ynSjllXL19VWvEdFkUuSuzmMnAWwmMI+QP69C4/qPmImrr6Glf5OpTCA+w=='

RSACipher('RSA/ECB/OAEPWithSHA-224AndMGF1Padding').encrypt('TPCyberSec', PublicKey=PublicKey, OAEPHashAlg='SHA-224', MGFHashAlg='MGF1')
# OUTPUT: 'aAfEayGfAeOmRLXHYBXpxEClVBLCESzcsD2RuuCUhT5V9qRcoJlnkvW25u1pYJy+nrbTXKiQVwsuUfdw28n/+TkIg39t4hWcG5qPMnQeX5OQMRY15uaiAV8xjT8deWh3vhjOk7GZj4q1P7dTxc+3dJYY3yFLFV/DUNGs9NlBJBio2fXAWIlGli3ioMoTuvEKhgnS9hbJDnNRsrxvRYr8m6GPDzsPJG4j8Io2Kvd34Qg4u7wmu8elZxwZQck2vmTCjaoHFs18zmtdqbS/r5Jbl3rN3D9z4Lw2KCW8ZNuGfadPn92hGio/wNTt6Tnuht3gz7C1mJjyG6bWDhSB6X4l/Q=='

RSACipher('RSA/ECB/OAEPWithSHA-256AndMGF1Padding').encrypt('TPCyberSec', PublicKey=PublicKey, OAEPHashAlg='SHA-256', MGFHashAlg='MGF1')
# OUTPUT: 'om6R2Cd2t/mtvQDBpj/mgoJuzzEkUHFMNnwI0gUqicwsPhVUWDFiBJgYaeOJREZiQ1EvVZP1/ip0z21k1/frqPb5BgRUiR4+yXw3E9owgSKYlR+SU5lIECvH1DaewKYmWk+p+piDJpadw17+cTXXOXERxVbq+DwkQ458KVUrvPychf8OtkfJhoX7fcVk2JkCLfXymmf3VYFlllWJr2nvS+9nrVBoxuuo1/HsjM3Po2opzDyFwFStKJigVk9FC3owIUmd7jbzjVz8OE1YBaDnShZTx2t0E0Bw9kptokkCWCKlgn0Ji9sCkG2CXZBHG57lN+u1/X0ySAXx7m9uO6rerg=='

RSACipher('RSA/ECB/OAEPWithSHA-384AndMGF1Padding').encrypt('TPCyberSec', PublicKey=PublicKey, OAEPHashAlg='SHA-384', MGFHashAlg='MGF1')
# OUTPUT: 'EkwPpaDUWiEQ11YcG3bRswShj50YkArvijqF+GnJkjuB40YmK+zjU2Qxh8PCIZozNIqtOe8qDVt0uc3RJHzgTpAUhjEbla/8shoh4xnaqAOgPqATcZ2Ne9t//Qea3146+yWI47Fs1J1HbMbSVdE+WCncE5hYjnBLqYLzYPulPX7gcn39JQLB0I5YcVKzhK4dsrhls+I75fnHdknpb0eHVAt0Q5JYd5x8yq4DwcAxDiXHr5qKx7MCqp+omTRyHIwXkFetMD9UAU6b0dHUTLPhojxqrTJKKFvSkxSoLcZZjYFltb9eALTlkwYXXRORXB12Nmbk9BYK4ldq3EpSGdjIuA=='

RSACipher('RSA/ECB/OAEPWithSHA-512AndMGF1Padding').encrypt('TPCyberSec', PublicKey=PublicKey, OAEPHashAlg='SHA-512', MGFHashAlg='MGF1')
# OUTPUT: 'W7Tmo8GU9z2xK3mgZC4twRxDEEi1NfmCdbgeJkGi7X/kIGTyaQVGqoPMS4/81yiwzoMiyA9mGm4ccjzjfYt+PBGGQ3OZdw8yHY/EvRBEsIoS6ZvvHFcjFsttrsGektKlN6KSG0NZVeHsUSyzeZ2875srVdjmaiqeJcwATgjSmqpZDSjHK6fy6TbqHrZDp/lCcTMgFp5dYMYEDu7dqL56GtDsog197B5O3seiBLldrSJtloAs2/NzOB3gxKkQlPc4wsfSm8HTxC2Ei0ls4xq3vDt2h1JJ27DVOcDZsEB+Z9JlenbZjyhBt2Al5Mi+iRIXty/d+UUM+bBcE8gbDTmXcg=='
```

---
#### RSACipher(algorithm :str, provider :str=None).decrypt(CipherText :str, PrivateKey :str=None, PublicKey :str=None) -> str
```
PublicKey = '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuTwspB6ubxVDBIb7IL7sSinHDmZLk/7RYzOWzVmLZo7dzBKiOmAbvFMMGRXFZ/37eThQ7VP31qe6MCH7PhtuP+KKOFpfgQc3O9umo78Qut4NGuCYNiuRrRx2jv1KESS+zIxllelx/JmEbtrME3boMZJ7W/y/SL8dfhYuGZYuqrGOe2ZRwekWkxAUJlAlHT/keDU8qU3oGDgVIn6Ck5MW0o8yBoMsm7o1LfvAGdt5jdxATXy1pzIi3Tr/bLVVkOPmaYrmRQ1McQLSekGA0+hn/MSMTIKRBA4JtSLaQ7YPZQPqwlvYm56958Lr8FPcQ7dz3KXWRY5wG+KSf+3vWnRZ3QIDAQAB-----END PUBLIC KEY-----'
PrivateKey = '-----BEGIN PRIVATE KEY-----MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5PCykHq5vFUMEhvsgvuxKKccOZkuT/tFjM5bNWYtmjt3MEqI6YBu8UwwZFcVn/ft5OFDtU/fWp7owIfs+G24/4oo4Wl+BBzc726ajvxC63g0a4Jg2K5GtHHaO/UoRJL7MjGWV6XH8mYRu2swTdugxkntb/L9Ivx1+Fi4Zli6qsY57ZlHB6RaTEBQmUCUdP+R4NTypTegYOBUifoKTkxbSjzIGgyybujUt+8AZ23mN3EBNfLWnMiLdOv9stVWQ4+ZpiuZFDUxxAtJ6QYDT6Gf8xIxMgpEEDgm1ItpDtg9lA+rCW9ibnr3nwuvwU9xDt3PcpdZFjnAb4pJ/7e9adFndAgMBAAECggEAAQJP5/D22EoQXGTz10DS/rBtkimCfeLkdxrf1myHct6SXLs5QQInBIabSUOyGJfsl8NzxWcwsW2meP6mZLc3iYeNYzMy0/wbE+tlY/z1dV8iSSQyEBF6sKu4BZ1hmuhNVcXqA8AKy+p2Kzhr5is+po56t4yP6jCIU5iBVchYprtggIeLUDAKIGterKEYxJt/N8pdJ0oGhx4cNxcRBDylqdm0HJphyP19BtBOsFtdT9cN6khNpsWGl7UirvlI8eoJxfkXzSgRLn0XoZhl1gDKAD9XCWnII9nzZyINUY1ICG2fISMMGGCNs9YmaY0wzMkhNvty8fPoWH+XrvNyomxIQQKBgQDiMQqPsRYZEw51CsGyyJFALHUfCxsLv6lXeFgCzBY74rksF4CrrNR1rcrvbMe06P54el+dtGevnpb+C1x/iFUkncGW6hNZii/dpKlxUvFTnYYWAITOiOJltDliFlXt7jCZEkGO9WcYRmTibve3pgjxB79MxEo4bJQCRSHTd6ZaLQKBgQDRpWUxaA5IdwuX7/pxG9ekFvxkJCpjDj14rkA832SLs1Zoq/d4D6/0WTp+c6wHL7fzU1DFbgCwB560ktlAvI77J6tapl1hps6RYh9H3bz+Hb6d6eFlhdyUKuTX1XXw6RcK3pYtYOltavl3bwAal/7TEKjrdS59qwx2BlsbQvQ8cQKBgQCHjjRyIQLJTC5h3mxvJNxHxVz7mcA/rkFidnDoXD8G7L1ku0EVoaJCVEFGc77LoMbAlTYwYSmyiiybW1u34pCEPTcDpoyqILLG9iPGEpsmLUVqci0lScvEf9nT+ubMjO77DYHUlyWN2sIjIbW7jfnV2XrAGvMQFaIuKhg3j4FWkQKBgQCYfp2QBae2EFnviBD864q9AjdOxHvMl9QhD2cMoFZrw+SLuOMGgyqzK6B/0LYGeDBvH2B2a+C2KqTHprW/ACllCWL8Sl1MpeBGIkCsrt9FXO+FwFVC2s8rO9RAJzZmKbaoImbM1VyWSaTyulwx+/PRJaIpu5A4uw4SX+cvelFcEQKBgHz2GicI/2cgYlRaeeR8tDSrfVNkhkF1qQZpC3GlTLMjmzZQzLXkjxvYRjNfSJaTZ9CMlaD1PFnqu7Uk9KhUwkClGnSsvFBO2MrRh6P32XS5eDVoP7jZ1pk5/dvuB1RSJqLT63FRaBi8XPSPeT/9po9lCfipK2tlNnggFMPZf3qQ-----END PRIVATE KEY-----'

RSACipher('RSA/ECB/PKCS1Padding').decrypt('\xb4\xb1\xbe\xaaS\xec\xba\xaa.\x18lUt\xb3`\x0b\xc7\x8b>\xe6\x0fVE\x82\t\xa6\xd7o8\xc5\xfauUv\xb1\x8d\xfa6C!\xf3\x93Rv\x9db\t\xdf\x1a\xb1%E!|\x00\xef\x08\x0c\xc2\xb1W:\x0c\x97k\xd28\xddZ\xe8\x18h\x7f\xed\x98h?;\xb3\x0e\xd6\x83\x11\xa7\t\xf0d\x7f]\xd5\xd3&\x98\x9b\x8f+\xbc\x9b{"6\xdd\xcc\xec\xfc1\xceR\xb3\xfa\xcaW\x03\x8f\x0f\x98\xe9\xeb\xad\x1b\x16a\x1b\\\x84\xd0\xe7! 8L\xba\xb08T\xb7\x87\xbd\xb4G\xad\t\xa6\xb6J\xfd\xef6Z\xbc4+[\xe3\xb7\xef_\xe4\xc25A*\x16a\x92\x10\xe9i2B !\xae_}\x1f\x05\x80W\xefS\x85\xe6]\x1f \x962J3\x1f\xdc\x91\xa7\xd5A{\x11\xa9\xef!\xd8=\x8e\xf29\x93\xed\xa7-\x93o\xff\x1bB\xb0\xd8\'u\x13\x1e=\x98\x14\x99\xcb\xcf\xf2\x18y+4\x00/L\xcc\xf9\xf6\\\x02\xe5\x87\xc1\xee\xd8\xd8\xcb\xb8`|z\x0c\x05\xa5Hx', PrivateKey=PrivateKey)
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/PKCS1Padding').decrypt('@|Y"\x8eaF{\x0c\x9ehY%\xa9X\x10d{\x01\xae\xc8\x1d;I\xfc>\x19\xb1\x16\x88V\x06\'S\x01\xc3\x18S/\\\xa0\x0f\xbd\xaf\xfe\xf7\x1a\xaa\x927J2\xb2\xc7L\x1f\xc2\xf2@\xb1\xa0\x11?\xf6#\xfb\x17\xb1@~\x07{\x85\xc9\xee\xe2b\xf7}\xb7Ub\x07/S#\x8f\'\x01qI$\x91\x97\x9bp\x8a\xa1\xaf\xfc\xc5\xe7\xb3\xd8\xec\x1b\xed*\x9b\xe5\xb8\x07\x14gf\xef\x1a\xe0\x9b\x9ft\x81\x19\xff\xc4&\xb7\xa3A\xd27\xbd\x95>>\xfe\xda\x80u\xb8\xb0\xb9\x84\xfe\xd0\xc2\x06N\x8e\x0c\xb0k\x13\x91\xb9\x8c\xcb\xde{\x0b\xbd\x85A\xado\xd8\xd4\x18i+\x05I\x07\xa0\xa6\x04]\x14>\x15I\xf24h\xd2kB\xcd\xbck\xf8\xf8lZ\xed\xc3=\x95\xb4\x8a\x96\xf9\xb5\xad>&\xff\xc2\x88\xf6\x156\x96\x80~\xf6\x1e\x9a\x13\x9f\x1c\x0fn\xdc.\xa2rJ\x88\xb5\xf31(\x82\xa2\xbc\x14\xa5\xed\x13\x03\xe8\xd9\xda\xc0\x15\x1e\x90\xe4~\xd6\xee\xfb\xc2\x1a\x8c', PublicKey=PublicKey)
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/NoPadding').decrypt('\x7f\x8f\x13xr\xdd\xb7\x1b\x9a\x1fA/\xa3:)\x11\xc8\x8d+A9\x86\xc1\xc0\x16\xa5^U#\xb5\x99\xcf\x8a\x1c@MR\xf4\xb3$\t\xef9\\\xf6a\x18\x17\xb5\xd0\x88\xad\xc1\xa3+\xdc\x1498V\xce\x01=\xe3\xbbu\xdeiG\xb2\x9b\xe7p\x94\xeb\x9ao\x82-}-$\xc6<\x10eYG\xcd\xf5\xda\xca"5/(8\xa0F\xe0i\xabV\xc2\xae\x02\x8e:)<\x83\xb4\xbd\x12=\xeb\xa9\xaf\xc5^R\x1bWu\x1f\x98\xb4\r\xb9\xd8\xf2R\xac5\x833\xd8\x9a\x93M\xbb\xc8\xbf\x8e"\xa1\xa3c\xcb\xd9l1\xbdJ\xda\xf6n\x02\xa3\xb8\x96D`\xc4*g}m^\x94O\xae\x03\x9b\x13:v\xcfSbt0H6\x007\x05\x05\xc8\xe2N}\xc2\xd2\x89m\xe9\xfc\x8eL\xf4\x8b\xc80\xc3i\x809v\x11\xa6\xfa\x08\xc2\x04\x17\x85\x02J\x1e\xc6\xf9rg\xe0\x1c\xdb"1\x08\x9cK\xe6\xd9\xc0 \x13\xf8D\xf2\xa6%BUG\xb4\x11\x85\xaf(N\xe1\xfak]\xd0', PrivateKey=PrivateKey)
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/NoPadding').decrypt('\x0ej6\xa3\x81\xd9\x86\xe5\xf7\x12\x1b\x1a\xc4\xe6\xa8,\x7f:\xa2Xf~k\x0b\xa4\x80\x16\xe1%\xd0p\xda\xa7\x85\x93\x8e\xce\x93\xf8L"\xd6\xe1\xc9e\xa3\x867\x87\xaa\x00\x03\xbbI\xed\x9aEc1bK\x83NnYSH\xfb\x1e\xf1\xf9\xdf\xb7"\xbdS4\x1d\xc6_\xfd\x16@\xb1I\x91\xc6=\x01\x0f\xe6Y\xfa|\x07gZ\x0eW\x98\xfal\x17Z\x80\xf9\xba\xc1S4\xdc?f\n\x12\xfe\x9d\xc3\xfa\xf5\xf5,\x8e\xf3\x01)k\xf8\xc1\x82[\xfa\xe0\xcb\xab_\xdc\x18\xd4\x18S\x13\xb8%\x9b\x93\xa2 \x95=\xd0\x98}\xab\xddZi\xc3Y\xf3\xe4<\x84\x07\x1es\x8f\xe0_\xbb\x80\xac0\xf5\xae7\xcb\xa9\xc8\xeb\xf3\x8aYi\xbd\xd1,\xd2\x8d\xd3\xfcb\x02\x14>\x05RJ.\xcf\xdc\xc3\xae\xb2N\xc7\x12H\x04\x07\xab\xb3\xdc\xe6<\x01\t>}c\x81\xa9m\x0c\xfd}\xb4\xf9\xc2\t=\xd1\x99\xd4D\xe4\x13\xf4\xf7FI\xc9 \x8a\xfb!j\xac\xd3$o\x95\x0f\xa1\x83\xed', PublicKey=PublicKey)
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/OAEPPadding').decrypt('T\x87C\x0e\xf4\xde\xf1\x0e \x1b\xaa\xe8&\xf6\xdf\x0f\x9eUhW\xb5_\x10D\xa00\xba\xb0]\xe0\'\x18\x92!%Q\xa7\x17\xb1\xd3\xd8b\xcco6V\x83z\xffA\xe5T\xfbG\xa5o}\\\xffe\xdc\x1f5P\xc5\x1c\xa8\xfa\xf1e"\xbf\xd4\xd7r\xc3\x9a^*\xe7\x12hw\xca\xb7CE\xe7\xf3\x8533\xbe\xdd\x9eL[K,\xc0\x93\xc9\x03\x0e\xcf\xa7\xae\x01\x19P\x8e\x0e\xcfE=\x8d\xc8\xad\xc8\x0e\xcf\xc4&.L\x1el\xfb\xddi\x13\xe7\xc2\x1b5\x94/\x91d>}I\xc4\x0cFv\xc2\xd1\xa8\x80u\x16\xfc\x81\xc1H\x87\xd28\xf9\xb6\'\x17\xc7\x92$\x87\xfbh\x875\x17\xd6\xda\xdf\x0b\xc8\x94l\x8c\xaa\xad\xdf\xd7\x14Z\x82\xb5\xd6\x8f\xb0\xdc},\\\xc6\x15\xac\xcd\x12\xa5\xeb\xbb]\xad\xbeW>\xe3\xfa\xf6\r\xdd\x1c\xd2\xf2x\xcdN\xb6\x14\x07W\xb4n\xfc\xcd\x04Dv}\xd1\x05\xe5\n|\x89\xbc\x9c\xb7Yv\xa0\xa7\xed\xa78k\xa78K\xa2@ly0', PrivateKey=PrivateKey, OAEPHashAlg='SHA-256', MGFHashAlg='MGF1')
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/OAEPWithSHA-1AndMGF1Padding').decrypt('K\x05\xa0E"\xeaJ\x17\xb8\x9d\x18\x05\x8cL\xe94\xd3\x1f\x9fG\x84:\x8a\xe1b\x9d\xc0\xce\xaeyj\x00/\t\x1c{\xabq\xab+E\xd5\xafe\'\x92\xe8\x05\xe8\x04$7\x1do\xc1\xbd\xf8\x9b\xaf){Q\xf3P\x8b\xb8<~\xb0uw\xfd\xdbQ\xf0\xda\xd8\x02\xbeT\xfaIe\xb0lA\x89\x98q\xf8Q\xeb_P\xc3\xca@\xf2\xef7xFI\xfb\xaf\xbe4[\xddP\x9f\x1f\xf9\xae\x13\x01\x92(\n\xe9@\xc9\xbe\xf3\xcaC\xb6\xc2:S\x19\x7f\xa6y\x96\xc2\x07\x87\xcd\xfd?&$wd\x89|M\xba\x1b\xe3c\xb8\x0b\xd2\xf9\x06\x12\xc73\x13Y\xb5C)\r\x05\xa7t\xe2\xe4\n\xce"\x9c\x8ej\xbb\xa2\xc1\xb1\x1a\x98\t\x92?\x8a0\xfc\xa1\xfc\xf9\x11\xbc.9\'\xae\x85R\xbe\xfa\x9a\xc3\xf3\x7f\xd4\xad%\xc8\x8f\xefu\xcat\xa3\x96U\xcb\xd7\xd5V\xbcGE\x91K\x92\xbb9\x8c\x9c\x05\xb0\x98\xc2>@\xfe\xbd\x0b\x8f\xea>b&\xae\xbe\x86\x95\xfeN\xa50\x80\xfb', PrivateKey=PrivateKey, OAEPHashAlg='SHA-1', MGFHashAlg='MGF1')
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/OAEPWithSHA-224AndMGF1Padding').decrypt('h\x07\xc4k!\x9f\x01\xe3\xa6D\xb5\xc7`\x15\xe9\xc4@\xa5T\x12\xc2\x11,\xdc\xb0=\x91\xba\xe0\x94\x85>U\xf6\xa4\\\xa0\x99g\x92\xf5\xb6\xe6\xedi`\x9c\xbe\x9e\xb6\xd3\\\xa8\x90W\x0b.Q\xf7p\xdb\xc9\xff\xf99\x08\x83\x7fm\xe2\x15\x9c\x1b\x9a\x8f2t\x1e_\x93\x901\x165\xe6\xe6\xa2\x01_1\x8d?\x1dyhw\xbe\x18\xce\x93\xb1\x99\x8f\x8a\xb5?\xb7S\xc5\xcf\xb7t\x96\x18\xdf!K\x15_\xc3P\xd1\xac\xf4\xd9A$\x18\xa8\xd9\xf5\xc0X\x89F\x96-\xe2\xa0\xca\x13\xba\xf1\n\x86\t\xd2\xf6\x16\xc9\x0esQ\xb2\xbcoE\x8a\xfc\x9b\xa1\x8f\x0f;\x0f$n#\xf0\x8a6*\xf7w\xe1\x088\xbb\xbc&\xbb\xc7\xa5g\x1c\x19A\xc96\xbed\xc2\x8d\xaa\x07\x16\xcd|\xcek]\xa9\xb4\xbf\xaf\x92[\x97z\xcd\xdc?s\xe0\xbc6(%\xbcd\xdb\x86}\xa7O\x9f\xdd\xa1\x1a*?\xc0\xd4\xed\xe99\xee\x86\xdd\xe0\xcf\xb0\xb5\x98\x98\xf2\x1b\xa6\xd6\x0e\x14\x81\xe9~%\xfd', PrivateKey=PrivateKey, OAEPHashAlg='SHA-224', MGFHashAlg='MGF1')
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/OAEPWithSHA-256AndMGF1Padding').decrypt('\xa2n\x91\xd8\'v\xb7\xf9\xad\xbd\x00\xc1\xa6?\xe6\x82\x82n\xcf1$PqL6|\x08\xd2\x05*\x89\xcc,>\x15TX1b\x04\x98\x18i\xe3\x89DFbCQ/U\x93\xf5\xfe*t\xcfmd\xd7\xf7\xeb\xa8\xf6\xf9\x06\x04T\x89\x1e>\xc9|7\x13\xda0\x81"\x98\x95\x1f\x92S\x99H\x10+\xc7\xd46\x9e\xc0\xa6&ZO\xa9\xfa\x98\x83&\x96\x9d\xc3^\xfeq5\xd79q\x11\xc5V\xea\xf8<$C\x8e|)U+\xbc\xfc\x9c\x85\xff\x0e\xb6G\xc9\x86\x85\xfb}\xc5d\xd8\x99\x02-\xf5\xf2\x9ag\xf7U\x81e\x96U\x89\xafi\xefK\xefg\xadPh\xc6\xeb\xa8\xd7\xf1\xec\x8c\xcd\xcf\xa3j)\xcc<\x85\xc0T\xad(\x98\xa0VOE\x0bz0!I\x9d\xee6\xf3\x8d\\\xfc8MX\x05\xa0\xe7J\x16S\xc7kt\x13@p\xf6Jm\xa2I\x02X"\xa5\x82}\t\x8b\xdb\x02\x90m\x82]\x90G\x1b\x9e\xe57\xeb\xb5\xfd}2H\x05\xf1\xeeon;\xaa\xde\xae', PrivateKey=PrivateKey, OAEPHashAlg='SHA-256', MGFHashAlg='MGF1')
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/OAEPWithSHA-384AndMGF1Padding').decrypt('\x12L\x0f\xa5\xa0\xd4Z!\x10\xd7V\x1c\x1bv\xd1\xb3\x04\xa1\x8f\x9d\x18\x90\n\xef\x8a:\x85\xf8i\xc9\x92;\x81\xe3F&+\xec\xe3Sd1\x87\xc3\xc2!\x9a34\x8a\xad9\xef*\r[t\xb9\xcd\xd1$|\xe0N\x90\x14\x861\x1b\x95\xaf\xfc\xb2\x1a!\xe3\x19\xda\xa8\x03\xa0>\xa0\x13q\x9d\x8d{\xdb\x7f\xfd\x07\x9a\xdf^:\xfb%\x88\xe3\xb1l\xd4\x9dGl\xc6\xd2U\xd1>X)\xdc\x13\x98X\x8epK\xa9\x82\xf3`\xfb\xa5=~\xe0r}\xfd%\x02\xc1\xd0\x8eXqR\xb3\x84\xae\x1d\xb2\xb8e\xb3\xe2;\xe5\xf9\xc7vI\xe9oG\x87T\x0btC\x92Xw\x9c|\xca\xae\x03\xc1\xc01\x0e%\xc7\xaf\x9a\x8a\xc7\xb3\x02\xaa\x9f\xa8\x994r\x1c\x8c\x17\x90W\xad0?T\x01N\x9b\xd1\xd1\xd4L\xb3\xe1\xa2<j\xad2J([\xd2\x93\x14\xa8-\xc6Y\x8d\x81e\xb5\xbf^\x00\xb4\xe5\x93\x06\x17]\x13\x91\\\x1dv6f\xe4\xf4\x16\n\xe2Wj\xdcJR\x19\xd8\xc8\xb8', PrivateKey=PrivateKey, OAEPHashAlg='SHA-384', MGFHashAlg='MGF1')
# OUTPUT: 'TPCyberSec'

RSACipher('RSA/ECB/OAEPWithSHA-512AndMGF1Padding').decrypt('[\xb4\xe6\xa3\xc1\x94\xf7=\xb1+y\xa0d.-\xc1\x1cC\x10H\xb55\xf9\x82u\xb8\x1e&A\xa2\xed\x7f\xe4 d\xf2i\x05F\xaa\x83\xccK\x8f\xfc\xd7(\xb0\xce\x83"\xc8\x0ff\x1an\x1cr<\xe3}\x8b~<\x11\x86Cs\x99w\x0f2\x1d\x8f\xc4\xbd\x10D\xb0\x8a\x12\xe9\x9b\xef\x1cW#\x16\xcbm\xae\xc1\x9e\x92\xd2\xa57\xa2\x92\x1bCYU\xe1\xecQ,\xb3y\x9d\xbc\xef\x9b+U\xd8\xe6j*\x9e%\xcc\x00N\x08\xd2\x9a\xaaY\r(\xc7+\xa7\xf2\xe96\xea\x1e\xb6C\xa7\xf9Bq3 \x16\x9e]`\xc6\x04\x0e\xee\xdd\xa8\xbez\x1a\xd0\xec\xa2\r}\xec\x1eN\xde\xc7\xa2\x04\xb9]\xad"m\x96\x80,\xdb\xf3s8\x1d\xe0\xc4\xa9\x10\x94\xf78\xc2\xc7\xd2\x9b\xc1\xd3\xc4-\x84\x8bIl\xe3\x1a\xb7\xbc;v\x87RI\xdb\xb0\xd59\xc0\xd9\xb0@~g\xd2ezv\xd9\x8f(A\xb7`%\xe4\xc8\xbe\x89\x12\x17\xb7/\xdd\xf9E\x0c\xf9\xb0\\\x13\xc8\x1b\r9\x97r', PrivateKey=PrivateKey, OAEPHashAlg='SHA-512', MGFHashAlg='MGF1')
# OUTPUT: 'TPCyberSec'
```

---
#### RSACipher(algorithm :str, provider :str=None).signature(message :str, PrivateKey :str) -> str
```
PrivateKey = '-----BEGIN PRIVATE KEY-----MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5PCykHq5vFUMEhvsgvuxKKccOZkuT/tFjM5bNWYtmjt3MEqI6YBu8UwwZFcVn/ft5OFDtU/fWp7owIfs+G24/4oo4Wl+BBzc726ajvxC63g0a4Jg2K5GtHHaO/UoRJL7MjGWV6XH8mYRu2swTdugxkntb/L9Ivx1+Fi4Zli6qsY57ZlHB6RaTEBQmUCUdP+R4NTypTegYOBUifoKTkxbSjzIGgyybujUt+8AZ23mN3EBNfLWnMiLdOv9stVWQ4+ZpiuZFDUxxAtJ6QYDT6Gf8xIxMgpEEDgm1ItpDtg9lA+rCW9ibnr3nwuvwU9xDt3PcpdZFjnAb4pJ/7e9adFndAgMBAAECggEAAQJP5/D22EoQXGTz10DS/rBtkimCfeLkdxrf1myHct6SXLs5QQInBIabSUOyGJfsl8NzxWcwsW2meP6mZLc3iYeNYzMy0/wbE+tlY/z1dV8iSSQyEBF6sKu4BZ1hmuhNVcXqA8AKy+p2Kzhr5is+po56t4yP6jCIU5iBVchYprtggIeLUDAKIGterKEYxJt/N8pdJ0oGhx4cNxcRBDylqdm0HJphyP19BtBOsFtdT9cN6khNpsWGl7UirvlI8eoJxfkXzSgRLn0XoZhl1gDKAD9XCWnII9nzZyINUY1ICG2fISMMGGCNs9YmaY0wzMkhNvty8fPoWH+XrvNyomxIQQKBgQDiMQqPsRYZEw51CsGyyJFALHUfCxsLv6lXeFgCzBY74rksF4CrrNR1rcrvbMe06P54el+dtGevnpb+C1x/iFUkncGW6hNZii/dpKlxUvFTnYYWAITOiOJltDliFlXt7jCZEkGO9WcYRmTibve3pgjxB79MxEo4bJQCRSHTd6ZaLQKBgQDRpWUxaA5IdwuX7/pxG9ekFvxkJCpjDj14rkA832SLs1Zoq/d4D6/0WTp+c6wHL7fzU1DFbgCwB560ktlAvI77J6tapl1hps6RYh9H3bz+Hb6d6eFlhdyUKuTX1XXw6RcK3pYtYOltavl3bwAal/7TEKjrdS59qwx2BlsbQvQ8cQKBgQCHjjRyIQLJTC5h3mxvJNxHxVz7mcA/rkFidnDoXD8G7L1ku0EVoaJCVEFGc77LoMbAlTYwYSmyiiybW1u34pCEPTcDpoyqILLG9iPGEpsmLUVqci0lScvEf9nT+ubMjO77DYHUlyWN2sIjIbW7jfnV2XrAGvMQFaIuKhg3j4FWkQKBgQCYfp2QBae2EFnviBD864q9AjdOxHvMl9QhD2cMoFZrw+SLuOMGgyqzK6B/0LYGeDBvH2B2a+C2KqTHprW/ACllCWL8Sl1MpeBGIkCsrt9FXO+FwFVC2s8rO9RAJzZmKbaoImbM1VyWSaTyulwx+/PRJaIpu5A4uw4SX+cvelFcEQKBgHz2GicI/2cgYlRaeeR8tDSrfVNkhkF1qQZpC3GlTLMjmzZQzLXkjxvYRjNfSJaTZ9CMlaD1PFnqu7Uk9KhUwkClGnSsvFBO2MrRh6P32XS5eDVoP7jZ1pk5/dvuB1RSJqLT63FRaBi8XPSPeT/9po9lCfipK2tlNnggFMPZf3qQ-----END PRIVATE KEY-----'

RSACipher('NONEwithRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'QHxZIo5hRnsMnmhZJalYEGR7Aa7IHTtJ/D4ZsRaIVgYnUwHDGFMvXKAPva/+9xqqkjdKMrLHTB/C8kCxoBE/9iP7F7FAfgd7hcnu4mL3fbdVYgcvUyOPJwFxSSSRl5twiqGv/MXns9jsG+0qm+W4BxRnZu8a4JufdIEZ/8Qmt6NB0je9lT4+/tqAdbiwuYT+0MIGTo4MsGsTkbmMy957C72FQa1v2NQYaSsFSQegpgRdFD4VSfI0aNJrQs28a/j4bFrtwz2VtIqW+bWtPib/woj2FTaWgH72HpoTnxwPbtwuonJKiLXzMSiCorwUpe0TA+jZ2sAVHpDkftbu+8IajA=='

RSACipher('SHA1withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'K5PU66dYTfebzlymu+mFNElKtqdIdWlBA2NopetY5lpH1ixF7N1FM090LDal73wP4K4BEoNNdQ9fFfv9byQaktt8xINqu9kxLBkd6GAwS1257a8fOElnBYc6ZzaiFOVewj0VOU+oyCdlNZjGN+xJuFHbfbv9SgZbcURhQMgJktlW2/ys95JqsAofdztBhHBGABgSQcXH1MqGI+6DQBZ9KK7t6IGhAUuBoDdZaCzH+gTZtDZofZw4EQVYf/qJ68WyvnpIepaR6S3Cdhmtb2oTx85kgwRHZ1EUYC22NUUKsN9NeV2QDHuanuctCQ/X3c4qiCRsUJbsD7j1luMblFhQUg=='

RSACipher('SHA224withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'ZnyGA86yT6NjF0+0A/NBmwmWOFX7qJOiYKqcGfYjJhn8JYz4qPHBXm7vvCnaky+o2kLId0VTu48Pw5W5nkttjJyQGRkJa9O8ed3n8IapV30aFpn4K8insMN/qW+DKDXSJnRpoHH3EikFPxIl1snGxCLxTu73wsdnU5uBRQsLgATzGwFDw9H5JGwklcA9qGcLWZ0UkYP9e6aR6jKBOTB6LbPEtfdzgexIONMdrY3dKyoYwg1JKAxBCQzBzlqTt2NkFkRFJ0q7buhFkZmylxi/V9ZSguih/sAgAX/D1Eoo5L1HyUPd1C7DrqnFycfkq53EAKj6196/gS1YIabxUPFvSQ=='

RSACipher('SHA256withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'rptZbMzxaXPH/zj0nZdDJdHVizhwmFbB01rb7AVg26MVPlcJ0SY8/2MLKTeOw6+S44NKVoBKFAoDpVnQ9u5meB1HFOhxexvoFdwhU5b0G2RDKXxvEuKfV/wD0vcpEALnlkAKMMcGuZhsHf7aRPQ/cBPISP9WvgsHhZIIOav0pX0ge/LXK36VuRReuuVLMPF/lGPdJeBMn6JbKZzhTkXXR561lvVhknMsOFeALlpt8wSJ/A7jgaLzAdk1Hfq61MMFZr50xriy4wS7EQq0zr7xuP/ymgY7uplvE5aYHbWwIc4YUxaUctKhgtjqU+NS/i2JetnPVmZoymF/YKoUbyhnIQ=='

RSACipher('SHA384withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'JKkZc/KqRSixvj0yhLFO4DHDLqwbUi07ZenG/NiYS+WqywKSkDqcoA5Z9iU0guMpRntUftEjBVmtsA/cgE+984+2+TyRTb9e2+aQjam1eydmp9aXB42oDpw4ZSfMtCu975f0M3gILQqTAn2ty8w4+JC/Y9yHwhEZZ8VAQ8dTgEljfqgRHtaCVvekGA/5WYXeIrvl8eWvAVCQAbUh5a8tnUdbDTmFX9BVC5GprQeyPkyjcsoxdANE58szOtX7n0OVBYgvyiTIHLXZGPoDViKa9gwDqjdid5KSm1kgKY4bHJSfb12hL/J7VMUcPTb5temteerUF10giYMREJFeuwr78w=='

RSACipher('SHA512withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'JYPaemEghHTD21VkXZPlVNUMR7loLJ+4CbR+rrhtzg7eqTNmEFjGUSx6p1StTG6LTb+4Oki99ZcBXt+ynaErwZqO6hEXHR/Mivatd1FQDH/kC6dwCNAYImdQP+vhA8KoQtdLrDGkVB6o8zgU7FBSvcmKNL3tieIFY0Tehf5nPpRJJgiufucXClmwHYUzBRGopipygHpdts6T+ATcFQPq5Q6bwomcHmT/z6gL+KXQZb0N6dyfCAAPjpk360TWf5+LDcYbw8MpqZg2AH/xueL7ldX2hoi7VGphVQlvmDJwFDxB7LVNd0rHae4qOOTyuEUUQouo3qZg2FosDngEKOK2Bw=='

RSACipher('SHA3-224withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'igCoIM2nF9BMT5SIc+VNY2qUzHCOkaFlQDNJt82tSfXxL6kHRc2x88+ZoNGxSnPBavsFD9euAvAW5daleLJD9wxHk+7Ye+DWWOVw/1dOLeM9vyaRcCBEVshPBX7NzLwIKyBJIL+tseAwM0w8pieuovFb/3BHqhzOpcUGhl+aqD/MvfQEQdh2hhTKaCZnBa/qpHqFIO2VyRMSN0JFLLPABWt8b6iGegNQvexDP3l5Md8xSZx6OFBpooKAoxVY5IhQm6AhG0197ZNjnxFkBbzlKuMxi1pjEi4zHhqAiFNp9XEoMkFiZGBMEHQ1S5BnMkSHDE4vCjyFzVkw5E5D7gyhOA=='

RSACipher('SHA3-256withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'pKG3SfdAgDpuWAbHS2IBeJiTgsGCJVuB0VdSKM5oMv9xAZBaBHOZ05AH7P0VHDommd54iLEf5+BqQHCxnrpmMi+tXYBhpM/WhmjTMeq8zyUDubS9g6Vs7cQd4rswaz1BhJHwrYEx7Zmj3SwRxT/d62KVq4QPkQ3uljE0+zP9I6L5+0apPdvhmv83ftpq0wrLw7MbXb2KcFxYJx/HLm4Eij/8daQ/HMqh/0hqchOjxAZRaikJ3GXMAr79RZRs8V60u8GXQBufg2EY2eWFF/PGxcdlAmuNpSpu4BQrwOgpTk7xDgiGLheC2d50wlyKFwxqt7HuuC5OLWVn+XRjyM8VNQ=='

RSACipher('SHA3-384withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'Y8kxemkWXJV5Ea5TZ6m3TKaYsEEZqct7qNssVmE0tfeIWaX8BsOZy0IVPIQi2cBvpSmDW28VYWmTIiR/FgHaqq3RD93uICtIdD7vsPI4FRbrDnppXCQM6ZUMJzGG8/s/KYPSfWJtpRASg3YgeFyMTk/dKle+MQDxb/S+8uUlElNnGKqWC7t8nP73CUL4P8h6gXgXp/vTbX8kTlngrPu1NoqqbiKHWjFWmqJN2ER96WH+gz8lX7EOlihE8+D6OzN6u1TR9wM1eEFz0usmbIQD/xNzW9Ph9EH6rMiA/IwHycV676afoxANR+IzJ2VCqHbSw9YudZ2ZIJwy4/DHl6cYhg=='

RSACipher('SHA3-512withRSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'aGI8rhuAWcCT+4uhpIGE4iWzG03KCDy3E0nvjMZWSWkaXFV0oJVBg68uOi90/XmknK/5Qxo0poGL52aM8vDH8JCNx02KB5X5omLK3grRf2rAzLv8xz2Q9jcwK26eoKHJ7XP9aYJZdJIO82qGgb1iel6zv0VvDQOPO3eQK6nAhYSHfmJ7YXmGpTTJu/eGRbQ6x9AADC6kLmf15LBLxO8ik+GjV5bKK/DetauN2U8mhIzhFnqh9+GHRGNrkEjpjqCKeHthKim+9fwB+OsLTjLvEAeJVs40P6EKVo23Iha1Oy1ZY/ROsXoLns9wo0vfaL3Tzgvgb+cAO2jow9t7oyiocA=='
```

---
#### RSACipher(algorithm :str, provider :str=None).verify(message :str, signedData :str, PublicKey :str) -> boolean
```
PublicKey = '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuTwspB6ubxVDBIb7IL7sSinHDmZLk/7RYzOWzVmLZo7dzBKiOmAbvFMMGRXFZ/37eThQ7VP31qe6MCH7PhtuP+KKOFpfgQc3O9umo78Qut4NGuCYNiuRrRx2jv1KESS+zIxllelx/JmEbtrME3boMZJ7W/y/SL8dfhYuGZYuqrGOe2ZRwekWkxAUJlAlHT/keDU8qU3oGDgVIn6Ck5MW0o8yBoMsm7o1LfvAGdt5jdxATXy1pzIi3Tr/bLVVkOPmaYrmRQ1McQLSekGA0+hn/MSMTIKRBA4JtSLaQ7YPZQPqwlvYm56958Lr8FPcQ7dz3KXWRY5wG+KSf+3vWnRZ3QIDAQAB-----END PUBLIC KEY-----'

RSACipher('NONEwithRSA').verify('TPCyberSec', '@|Y"\x8eaF{\x0c\x9ehY%\xa9X\x10d{\x01\xae\xc8\x1d;I\xfc>\x19\xb1\x16\x88V\x06\'S\x01\xc3\x18S/\\\xa0\x0f\xbd\xaf\xfe\xf7\x1a\xaa\x927J2\xb2\xc7L\x1f\xc2\xf2@\xb1\xa0\x11?\xf6#\xfb\x17\xb1@~\x07{\x85\xc9\xee\xe2b\xf7}\xb7Ub\x07/S#\x8f\'\x01qI$\x91\x97\x9bp\x8a\xa1\xaf\xfc\xc5\xe7\xb3\xd8\xec\x1b\xed*\x9b\xe5\xb8\x07\x14gf\xef\x1a\xe0\x9b\x9ft\x81\x19\xff\xc4&\xb7\xa3A\xd27\xbd\x95>>\xfe\xda\x80u\xb8\xb0\xb9\x84\xfe\xd0\xc2\x06N\x8e\x0c\xb0k\x13\x91\xb9\x8c\xcb\xde{\x0b\xbd\x85A\xado\xd8\xd4\x18i+\x05I\x07\xa0\xa6\x04]\x14>\x15I\xf24h\xd2kB\xcd\xbck\xf8\xf8lZ\xed\xc3=\x95\xb4\x8a\x96\xf9\xb5\xad>&\xff\xc2\x88\xf6\x156\x96\x80~\xf6\x1e\x9a\x13\x9f\x1c\x0fn\xdc.\xa2rJ\x88\xb5\xf31(\x82\xa2\xbc\x14\xa5\xed\x13\x03\xe8\xd9\xda\xc0\x15\x1e\x90\xe4~\xd6\xee\xfb\xc2\x1a\x8c', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA1withRSA').verify('TPCyberSec', '+\x93\xd4\xeb\xa7XM\xf7\x9b\xce\\\xa6\xbb\xe9\x854IJ\xb6\xa7HuiA\x03ch\xa5\xebX\xe6ZG\xd6,E\xec\xddE3Ot,6\xa5\xef|\x0f\xe0\xae\x01\x12\x83Mu\x0f_\x15\xfb\xfdo$\x1a\x92\xdb|\xc4\x83j\xbb\xd91,\x19\x1d\xe8`0K]\xb9\xed\xaf\x1f8Ig\x05\x87:g6\xa2\x14\xe5^\xc2=\x159O\xa8\xc8\'e5\x98\xc67\xecI\xb8Q\xdb}\xbb\xfdJ\x06[qDa@\xc8\t\x92\xd9V\xdb\xfc\xac\xf7\x92j\xb0\n\x1fw;A\x84pF\x00\x18\x12A\xc5\xc7\xd4\xca\x86#\xee\x83@\x16}(\xae\xed\xe8\x81\xa1\x01K\x81\xa07Yh,\xc7\xfa\x04\xd9\xb46h}\x9c8\x11\x05X\x7f\xfa\x89\xeb\xc5\xb2\xbezHz\x96\x91\xe9-\xc2v\x19\xadoj\x13\xc7\xced\x83\x04GgQ\x14`-\xb65E\n\xb0\xdfMy]\x90\x0c{\x9a\x9e\xe7-\t\x0f\xd7\xdd\xce*\x88$lP\x96\xec\x0f\xb8\xf5\x96\xe3\x1b\x94XPR', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA224withRSA').verify('TPCyberSec', 'f|\x86\x03\xce\xb2O\xa3c\x17O\xb4\x03\xf3A\x9b\t\x968U\xfb\xa8\x93\xa2`\xaa\x9c\x19\xf6#&\x19\xfc%\x8c\xf8\xa8\xf1\xc1^n\xef\xbc)\xda\x93/\xa8\xdaB\xc8wES\xbb\x8f\x0f\xc3\x95\xb9\x9eKm\x8c\x9c\x90\x19\x19\tk\xd3\xbcy\xdd\xe7\xf0\x86\xa9W}\x1a\x16\x99\xf8+\xc8\xa7\xb0\xc3\x7f\xa9o\x83(5\xd2&ti\xa0q\xf7\x12)\x05?\x12%\xd6\xc9\xc6\xc4"\xf1N\xee\xf7\xc2\xc7gS\x9b\x81E\x0b\x0b\x80\x04\xf3\x1b\x01C\xc3\xd1\xf9$l$\x95\xc0=\xa8g\x0bY\x9d\x14\x91\x83\xfd{\xa6\x91\xea2\x8190z-\xb3\xc4\xb5\xf7s\x81\xecH8\xd3\x1d\xad\x8d\xdd+*\x18\xc2\rI(\x0cA\t\x0c\xc1\xceZ\x93\xb7cd\x16DE\'J\xbbn\xe8E\x91\x99\xb2\x97\x18\xbfW\xd6R\x82\xe8\xa1\xfe\xc0 \x01\x7f\xc3\xd4J(\xe4\xbdG\xc9C\xdd\xd4.\xc3\xae\xa9\xc5\xc9\xc7\xe4\xab\x9d\xc4\x00\xa8\xfa\xd7\xde\xbf\x81-X!\xa6\xf1P\xf1oI', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA256withRSA').verify('TPCyberSec', '\xae\x9bYl\xcc\xf1is\xc7\xff8\xf4\x9d\x97C%\xd1\xd5\x8b8p\x98V\xc1\xd3Z\xdb\xec\x05`\xdb\xa3\x15>W\t\xd1&<\xffc\x0b)7\x8e\xc3\xaf\x92\xe3\x83JV\x80J\x14\n\x03\xa5Y\xd0\xf6\xeefx\x1dG\x14\xe8q{\x1b\xe8\x15\xdc!S\x96\xf4\x1bdC)|o\x12\xe2\x9fW\xfc\x03\xd2\xf7)\x10\x02\xe7\x96@\n0\xc7\x06\xb9\x98l\x1d\xfe\xdaD\xf4?p\x13\xc8H\xffV\xbe\x0b\x07\x85\x92\x089\xab\xf4\xa5} {\xf2\xd7+~\x95\xb9\x14^\xba\xe5K0\xf1\x7f\x94c\xdd%\xe0L\x9f\xa2[)\x9c\xe1NE\xd7G\x9e\xb5\x96\xf5a\x92s,8W\x80.Zm\xf3\x04\x89\xfc\x0e\xe3\x81\xa2\xf3\x01\xd95\x1d\xfa\xba\xd4\xc3\x05f\xbet\xc6\xb8\xb2\xe3\x04\xbb\x11\n\xb4\xce\xbe\xf1\xb8\xff\xf2\x9a\x06;\xba\x99o\x13\x96\x98\x1d\xb5\xb0!\xce\x18S\x16\x94r\xd2\xa1\x82\xd8\xeaS\xe3R\xfe-\x89z\xd9\xcfVfh\xcaa\x7f`\xaa\x14o(g!', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA384withRSA').verify('TPCyberSec', '$\xa9\x19s\xf2\xaaE(\xb1\xbe=2\x84\xb1N\xe01\xc3.\xac\x1bR-;e\xe9\xc6\xfc\xd8\x98K\xe5\xaa\xcb\x02\x92\x90:\x9c\xa0\x0eY\xf6%4\x82\xe3)F{T~\xd1#\x05Y\xad\xb0\x0f\xdc\x80O\xbd\xf3\x8f\xb6\xf9<\x91M\xbf^\xdb\xe6\x90\x8d\xa9\xb5{\'f\xa7\xd6\x97\x07\x8d\xa8\x0e\x9c8e\'\xcc\xb4+\xbd\xef\x97\xf43x\x08-\n\x93\x02}\xad\xcb\xcc8\xf8\x90\xbfc\xdc\x87\xc2\x11\x19g\xc5@C\xc7S\x80Ic~\xa8\x11\x1e\xd6\x82V\xf7\xa4\x18\x0f\xf9Y\x85\xde"\xbb\xe5\xf1\xe5\xaf\x01P\x90\x01\xb5!\xe5\xaf-\x9dG[\r9\x85_\xd0U\x0b\x91\xa9\xad\x07\xb2>L\xa3r\xca1t\x03D\xe7\xcb3:\xd5\xfb\x9fC\x95\x05\x88/\xca$\xc8\x1c\xb5\xd9\x18\xfa\x03V"\x9a\xf6\x0c\x03\xaa7bw\x92\x92\x9bY )\x8e\x1b\x1c\x94\x9fo]\xa1/\xf2{T\xc5\x1c=6\xf9\xb5\xe9\xady\xea\xd4\x17] \x89\x83\x11\x10\x91^\xbb\n\xfb\xf3', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA512withRSA').verify('TPCyberSec', '%\x83\xdaza \x84t\xc3\xdbUd]\x93\xe5T\xd5\x0cG\xb9h,\x9f\xb8\t\xb4~\xae\xb8m\xce\x0e\xde\xa93f\x10X\xc6Q,z\xa7T\xadLn\x8bM\xbf\xb8:H\xbd\xf5\x97\x01^\xdf\xb2\x9d\xa1+\xc1\x9a\x8e\xea\x11\x17\x1d\x1f\xcc\x8a\xf6\xadwQP\x0c\x7f\xe4\x0b\xa7p\x08\xd0\x18"gP?\xeb\xe1\x03\xc2\xa8B\xd7K\xac1\xa4T\x1e\xa8\xf38\x14\xecPR\xbd\xc9\x8a4\xbd\xed\x89\xe2\x05cD\xde\x85\xfeg>\x94I&\x08\xae~\xe7\x17\nY\xb0\x1d\x853\x05\x11\xa8\xa6*r\x80z]\xb6\xce\x93\xf8\x04\xdc\x15\x03\xea\xe5\x0e\x9b\xc2\x89\x9c\x1ed\xff\xcf\xa8\x0b\xf8\xa5\xd0e\xbd\r\xe9\xdc\x9f\x08\x00\x0f\x8e\x997\xebD\xd6\x7f\x9f\x8b\r\xc6\x1b\xc3\xc3)\xa9\x986\x00\x7f\xf1\xb9\xe2\xfb\x95\xd5\xf6\x86\x88\xbbTjaU\to\x982p\x14<A\xec\xb5MwJ\xc7i\xee*8\xe4\xf2\xb8E\x14B\x8b\xa8\xde\xa6`\xd8Z,\x0ex\x04(\xe2\xb6\x07', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA3-224withRSA').verify('TPCyberSec', '\x8a\x00\xa8 \xcd\xa7\x17\xd0LO\x94\x88s\xe5Mcj\x94\xccp\x8e\x91\xa1e@3I\xb7\xcd\xadI\xf5\xf1/\xa9\x07E\xcd\xb1\xf3\xcf\x99\xa0\xd1\xb1Js\xc1j\xfb\x05\x0f\xd7\xae\x02\xf0\x16\xe5\xd6\xa5x\xb2C\xf7\x0cG\x93\xee\xd8{\xe0\xd6X\xe5p\xffWN-\xe3=\xbf&\x91p DV\xc8O\x05~\xcd\xcc\xbc\x08+ I \xbf\xad\xb1\xe003L<\xa6\'\xae\xa2\xf1[\xffpG\xaa\x1c\xce\xa5\xc5\x06\x86_\x9a\xa8?\xcc\xbd\xf4\x04A\xd8v\x86\x14\xcah&g\x05\xaf\xea\xa4z\x85 \xed\x95\xc9\x13\x127BE,\xb3\xc0\x05k|o\xa8\x86z\x03P\xbd\xecC?yy1\xdf1I\x9cz8Pi\xa2\x82\x80\xa3\x15X\xe4\x88P\x9b\xa0!\x1bM}\xed\x93c\x9f\x11d\x05\xbc\xe5*\xe31\x8bZc\x12.3\x1e\x1a\x80\x88Si\xf5q(2Abd`L\x10t5K\x90g2D\x87\x0cN/\n<\x85\xcdY0\xe4NC\xee\x0c\xa18', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA3-256withRSA').verify('TPCyberSec', '\xa4\xa1\xb7I\xf7@\x80:nX\x06\xc7Kb\x01x\x98\x93\x82\xc1\x82%[\x81\xd1WR(\xceh2\xffq\x01\x90Z\x04s\x99\xd3\x90\x07\xec\xfd\x15\x1c:&\x99\xdex\x88\xb1\x1f\xe7\xe0j@p\xb1\x9e\xbaf2/\xad]\x80a\xa4\xcf\xd6\x86h\xd31\xea\xbc\xcf%\x03\xb9\xb4\xbd\x83\xa5l\xed\xc4\x1d\xe2\xbb0k=A\x84\x91\xf0\xad\x811\xed\x99\xa3\xdd,\x11\xc5?\xdd\xebb\x95\xab\x84\x0f\x91\r\xee\x9614\xfb3\xfd#\xa2\xf9\xfbF\xa9=\xdb\xe1\x9a\xff7~\xdaj\xd3\n\xcb\xc3\xb3\x1b]\xbd\x8ap\\X\'\x1f\xc7.n\x04\x8a?\xfcu\xa4?\x1c\xca\xa1\xffHjr\x13\xa3\xc4\x06Qj)\t\xdce\xcc\x02\xbe\xfdE\x94l\xf1^\xb4\xbb\xc1\x97@\x1b\x9f\x83a\x18\xd9\xe5\x85\x17\xf3\xc6\xc5\xc7e\x02k\x8d\xa5*n\xe0\x14+\xc0\xe8)NN\xf1\x0e\x08\x86.\x17\x82\xd9\xdet\xc2\\\x8a\x17\x0cj\xb7\xb1\xee\xb8.N-eg\xf9tc\xc8\xcf\x155', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA3-384withRSA').verify('TPCyberSec', 'c\xc91zi\x16\\\x95y\x11\xaeSg\xa9\xb7L\xa6\x98\xb0A\x19\xa9\xcb{\xa8\xdb,Va4\xb5\xf7\x88Y\xa5\xfc\x06\xc3\x99\xcbB\x15<\x84"\xd9\xc0o\xa5)\x83[o\x15ai\x93"$\x7f\x16\x01\xda\xaa\xad\xd1\x0f\xdd\xee +Ht>\xef\xb0\xf28\x15\x16\xeb\x0ezi\\$\x0c\xe9\x95\x0c\'1\x86\xf3\xfb?)\x83\xd2}bm\xa5\x10\x12\x83v x\\\x8cNO\xdd*W\xbe1\x00\xf1o\xf4\xbe\xf2\xe5%\x12Sg\x18\xaa\x96\x0b\xbb|\x9c\xfe\xf7\tB\xf8?\xc8z\x81x\x17\xa7\xfb\xd3m\x7f$NY\xe0\xac\xfb\xb56\x8a\xaan"\x87Z1V\x9a\xa2M\xd8D}\xe9a\xfe\x83?%_\xb1\x0e\x96(D\xf3\xe0\xfa;3z\xbbT\xd1\xf7\x035xAs\xd2\xeb&l\x84\x03\xff\x13s[\xd3\xe1\xf4A\xfa\xac\xc8\x80\xfc\x8c\x07\xc9\xc5z\xef\xa6\x9f\xa3\x10\rG\xe23\'eB\xa8v\xd2\xc3\xd6.u\x9d\x99 \x9c2\xe3\xf0\xc7\x97\xa7\x18\x86', PublicKey=PublicKey)
# OUTPUT: True

RSACipher('SHA3-512withRSA').verify('TPCyberSec', 'hb<\xae\x1b\x80Y\xc0\x93\xfb\x8b\xa1\xa4\x81\x84\xe2%\xb3\x1bM\xca\x08<\xb7\x13I\xef\x8c\xc6VIi\x1a\\Ut\xa0\x95A\x83\xaf.:/t\xfdy\xa4\x9c\xaf\xf9C\x1a4\xa6\x81\x8b\xe7f\x8c\xf2\xf0\xc7\xf0\x90\x8d\xc7M\x8a\x07\x95\xf9\xa2b\xca\xde\n\xd1\x7fj\xc0\xcc\xbb\xfc\xc7=\x90\xf670+n\x9e\xa0\xa1\xc9\xeds\xfdi\x82Yt\x92\x0e\xf3j\x86\x81\xbdbz^\xb3\xbfEo\r\x03\x8f;w\x90+\xa9\xc0\x85\x84\x87~b{ay\x86\xa54\xc9\xbb\xf7\x86E\xb4:\xc7\xd0\x00\x0c.\xa4.g\xf5\xe4\xb0K\xc4\xef"\x93\xe1\xa3W\x96\xca+\xf0\xde\xb5\xab\x8d\xd9O&\x84\x8c\xe1\x16z\xa1\xf7\xe1\x87Dck\x90H\xe9\x8e\xa0\x8ax{a*)\xbe\xf5\xfc\x01\xf8\xeb\x0bN2\xef\x10\x07\x89V\xce4?\xa1\nV\x8d\xb7"\x16\xb5;-Yc\xf4N\xb1z\x0b\x9e\xcfp\xa3K\xdfh\xbd\xd3\xce\x0b\xe0o\xe7\x00;h\xe8\xc3\xdb{\xa3(\xa8p', PublicKey=PublicKey)
# OUTPUT: True
```

---
#### ECDSACipher(algorithm :str).signature(message :str, PrivateKey :str) -> str
```
<!-- secp256r1 (P-256), secp384r1 (P-384), secp521r1 (P-521), secp256k1 (Bitcoin/ Ethereum/ Litecoin) -->
PrivateKey = '-----BEGIN PRIVATE KEY-----MEECAQAwEwYHKoZIzj0CAQYIKoZIzj0DAQcEJzAlAgEBBCBt63OSea+CQorfYNy9WAVqiHtQvaIzNLozTfLlAMWQMg==-----END PRIVATE KEY-----'

ECDSACipher('NONEwithECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEQCIDo/341hFaYcwlsb4nHzedJHqkhqe6PZ1JtgKPSDlzhFAiBqMzF0emR7n8l1jHmEy4K+XDsdZI+MXwuYPJ4qywJoBg=='

ECDSACipher('SHA1withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEUCIQDPBrziUJG1uW0u6MlGDEGfJU69J04dH+FtF36TlHtDBAIgSMfKDJVtDGfdFjqMDsD4oJXo4RHdWBsUqp9Z4Nds3Sw='

ECDSACipher('SHA224withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEUCIFiiE2wZEXxyHc9rd6agJMpHbwTuuylQrn6z+ulZFoGVAiEA2fLfgTD+6kI0FW8kYsKzWIy1rQw0M9CirpeosvxV58o='

ECDSACipher('SHA256withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEYCIQDBBn69fgo/moywYiyC1dMknKI6okB8ypb/fyYHP9riUwIhALYLLsf27IQMQKuBUd2obe185bxBb5A0MqJn/g2K21SV'

ECDSACipher('SHA384withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEUCIQD5/pA0D8Bt7hChvHu0HXxZGG474WH1CYGTyimDBrQAIAIgflBTMd9kOsTWMHklL8QprGB/6ZDcpHkYXvW4D6aiO2I='

ECDSACipher('SHA512withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEYCIQC/bLXSIfRQD/BzNljcvQH4ZDYyzUz+EZYKbTLwY7xAPAIhAPDwWsICVZCMiojc6zsQ6ce7ENpvkULC4IfT+JbImzH0'

ECDSACipher('SHA3-224withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEUCIQDHdwdE3TO60MgAaB9hZ/iESGskEDaJBnUEIWIxg7SmlAIgDSjlu6Dj7akChReeMUrOWvHH+f4Y34kt5OoqcoedQwM='

ECDSACipher('SHA3-256withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEQCIEgdfLyqfsIFndSkFzIqkkzptGArIKjR6tdb9PxoykfPAiAhvnc5D4IkjmcNAlq+vG5ZQ/MElu+GdUgJLFKIDY7Sbg=='

ECDSACipher('SHA3-384withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEQCIFnyYy4jV/rJ0GRSUIT5TGBFf36NPc2qXQEbVLkLRoG5AiAMpLtljbOjaVvDdfssAkN6Pxu1S2NRycmLyXYY2BEDmg=='

ECDSACipher('SHA3-512withECDSA').signature('TPCyberSec', PrivateKey=PrivateKey)
# OUTPUT: 'MEQCICwLWFtNDeRj/+iOu8kvFE/0B73aijPrqhRE7URlOQxNAiAwweDEUZMUOjUkKdd3aD6OhCRL8gRLHErP6fNIQqJ9Mg=='
```

---
#### ECDSACipher(algorithm :str).verify(message :str, signedData :str, PublicKey :str) -> boolean
```
<!-- secp256r1 (P-256), secp384r1 (P-384), secp521r1 (P-521), secp256k1 (Bitcoin/ Ethereum/ Litecoin) -->
PublicKey = '-----BEGIN PUBLIC KEY-----MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEhyMMvdnaui5hFj5iitqp2H2siJUJh8Siy49fBhdCWhivTFzs36ee6dgAhrmaXDQ3oGRhwgH0qxDmI2WaABIXSQ==-----END PUBLIC KEY-----'

ECDSACipher('NONEwithECDSA').verify('TPCyberSec', '0D\x02 :?\xdf\x8da\x15\xa6\x1c\xc2[\x1b\xe2q\xf3y\xd2G\xaaHj{\xa3\xd9\xd4\x9b`(\xf4\x83\x978E\x02 j31tzd{\x9f\xc9u\x8cy\x84\xcb\x82\xbe\\;\x1dd\x8f\x8c_\x0b\x98<\x9e*\xcb\x02h\x06', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA1withECDSA').verify('TPCyberSec', '0E\x02!\x00\xcf\x06\xbc\xe2P\x91\xb5\xb9m.\xe8\xc9F\x0cA\x9f%N\xbd\'N\x1d\x1f\xe1m\x17~\x93\x94{C\x04\x02 H\xc7\xca\x0c\x95m\x0cg\xdd\x16:\x8c\x0e\xc0\xf8\xa0\x95\xe8\xe1\x11\xddX\x1b\x14\xaa\x9fY\xe0\xd7l\xdd,', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA224withECDSA').verify('TPCyberSec', '0E\x02 X\xa2\x13l\x19\x11|r\x1d\xcfkw\xa6\xa0$\xcaGo\x04\xee\xbb)P\xae~\xb3\xfa\xe9Y\x16\x81\x95\x02!\x00\xd9\xf2\xdf\x810\xfe\xeaB4\x15o$b\xc2\xb3X\x8c\xb5\xad\x0c43\xd0\xa2\xae\x97\xa8\xb2\xfcU\xe7\xca', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA256withECDSA').verify('TPCyberSec', '0F\x02!\x00\xc1\x06~\xbd~\n?\x9a\x8c\xb0b,\x82\xd5\xd3$\x9c\xa2:\xa2@|\xca\x96\xff\x7f&\x07?\xda\xe2S\x02!\x00\xb6\x0b.\xc7\xf6\xec\x84\x0c@\xab\x81Q\xdd\xa8m\xed|\xe5\xbcAo\x9042\xa2g\xfe\r\x8a\xdbT\x95', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA384withECDSA').verify('TPCyberSec', '0E\x02!\x00\xf9\xfe\x904\x0f\xc0m\xee\x10\xa1\xbc{\xb4\x1d|Y\x18n;\xe1a\xf5\t\x81\x93\xca)\x83\x06\xb4\x00 \x02 ~PS1\xdfd:\xc4\xd60y%/\xc4)\xac`\x7f\xe9\x90\xdc\xa4y\x18^\xf5\xb8\x0f\xa6\xa2;b', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA512withECDSA').verify('TPCyberSec', '0F\x02!\x00\xbfl\xb5\xd2!\xf4P\x0f\xf0s6X\xdc\xbd\x01\xf8d62\xcdL\xfe\x11\x96\nm2\xf0c\xbc@<\x02!\x00\xf0\xf0Z\xc2\x02U\x90\x8c\x8a\x88\xdc\xeb;\x10\xe9\xc7\xbb\x10\xdao\x91B\xc2\xe0\x87\xd3\xf8\x96\xc8\x9b1\xf4', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA3-224withECDSA').verify('TPCyberSec', '0E\x02!\x00\xc7w\x07D\xdd3\xba\xd0\xc8\x00h\x1fag\xf8\x84Hk$\x106\x89\x06u\x04!b1\x83\xb4\xa6\x94\x02 \r(\xe5\xbb\xa0\xe3\xed\xa9\x02\x85\x17\x9e1J\xceZ\xf1\xc7\xf9\xfe\x18\xdf\x89-\xe4\xea*r\x87\x9dC\x03', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA3-256withECDSA').verify('TPCyberSec', '0D\x02 H\x1d|\xbc\xaa~\xc2\x05\x9d\xd4\xa4\x172*\x92L\xe9\xb4`+ \xa8\xd1\xea\xd7[\xf4\xfch\xcaG\xcf\x02 !\xbew9\x0f\x82$\x8eg\r\x02Z\xbe\xbcnYC\xf3\x04\x96\xef\x86uH\t,R\x88\r\x8e\xd2n', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA3-384withECDSA').verify('TPCyberSec', '0D\x02 Y\xf2c.#W\xfa\xc9\xd0dRP\x84\xf9L`E\x7f~\x8d=\xcd\xaa]\x01\x1bT\xb9\x0bF\x81\xb9\x02 \x0c\xa4\xbbe\x8d\xb3\xa3i[\xc3u\xfb,\x02Cz?\x1b\xb5KcQ\xc9\xc9\x8b\xc9v\x18\xd8\x11\x03\x9a', PublicKey=PublicKey)
# OUTPUT: True

ECDSACipher('SHA3-512withECDSA').verify('TPCyberSec', '0D\x02 ,\x0bX[M\r\xe4c\xff\xe8\x8e\xbb\xc9/\x14O\xf4\x07\xbd\xda\x8a3\xeb\xaa\x14D\xedDe9\x0cM\x02 0\xc1\xe0\xc4Q\x93\x14:5$)\xd7wh>\x8e\x84$K\xf2\x04K\x1cJ\xcf\xe9\xf3HB\xa2}2', PublicKey=PublicKey)
# OUTPUT: True
```

---
#### KeyExchange(algorithm :str).getSharedSecret(serverPublicKey :str, clientPrivateKey :str) -> str
```
## algorithm: ECDH
Alice_PrivateKey = """-----BEGIN PRIVATE KEY-----MEECAQAwEwYHKoZIzj0CAQYIKoZIzj0DAQcEJzAlAgEBBCBt63OSea+CQorfYNy9WAVqiHtQvaIzNLozTfLlAMWQMg==-----END PRIVATE KEY-----"""
Alice_PublicKey = """-----BEGIN PUBLIC KEY-----MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEhyMMvdnaui5hFj5iitqp2H2siJUJh8Siy49fBhdCWhivTFzs36ee6dgAhrmaXDQ3oGRhwgH0qxDmI2WaABIXSQ==-----END PUBLIC KEY-----"""

Bob_PrivateKey = """-----BEGIN PRIVATE KEY-----MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgOwwHV5XAJo+ZwkA3
nR6gmMT/iUxMgGsCQSdTh0cRbJ2hRANCAAR0MbyY3Zbwcz5o2IhSXnFjBl ozWh6V
pTI8RKlsRujvaqbQZLVuzpurgYTy1mueR/Q9pXTsVK3vqXNxeC/n54bw-----END PRIVATE KEY-----"""
Bob_PublicKey = """-----BEGIN PUBLIC KEY-----MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdDG8mN2W8HM+aNiIUl5xYwZaM1oe
laUyPESpbEbo72qm0GS1bs6bq4GE8tZrnkf0PaV07FSt76lzcXgv5+eG8A==-----END PUBLIC KEY-----"""

KeyExchange("ECDH").getSharedSecret(Alice_PublicKey, Bob_PrivateKey)
# OUTPUT: 'rDXpDalu1zlNeVPHf6cx+cZBMtTE3bLFFINsI+zP5l0='
KeyExchange("ECDH").getSharedSecret(Bob_PublicKey, Alice_PrivateKey)
# OUTPUT: 'rDXpDalu1zlNeVPHf6cx+cZBMtTE3bLFFINsI+zP5l0='


## algorithm: DH
Alice_PrivateKey = """-----BEGIN PRIVATE KEY-----
MIICJgIBADCCARcGCSqGSIb3DQEDATCCAQgCggEBAOJuU92EQ9Z3ako9xyJc/uEy
+Iy75jQtGocWJkBLXwN/LVNCYEyzexVsiXaE9y8paMQDTkIHA3dRbqWA77++qDf1
Ti++KN51WqItTumVDC+YQG/05UUY/IHLvwMxujsbN485/zn+AMoBxMXyOEZxxoU9
FtjUJNu7E6BU3nir7tHVzHhSxBx/oW9yx0M+s3rd9VJTVCPHI1zhA8D7//eTz7Q1
QotNpfshei8DCRjvOq4ETNGB7o0tZKOmdnrGZmg65t7yLLptCzV3i7vH7PBBF/lw
O2/3G/HWVC4xN8rWFzOW2jaGoHxThX4ORU/tfIB/B3KZWL+rPuFonoSBEmT7ms8C
AQIEggEEAoIBADwR5n6obu1x4u/8fQ81Lf+Z7pWumVy6IrvjYCuKjILLszaHb7x5
rEaZyYgY99rwxDuZRdC4EYOGO2vgQA/e4IoD/TbEXSOYTC0+otcIC3y828WZKpF6
tSh7yAQNBJGIoMuctmiDcmXT5XOnC6DROfgGFezc+Qpf6wxMmx1717szbSxDSCLa
dJ5xogAy11+e16pdxXo+DJZtfsyKfPKmy5dKsQEx624TzvsqZcn7A0a6NZMDb4/W
NdhXBf+OlxBS9yLyv6hg2v4qXWVuc8RDxGHGrRgiRXjIs7E6bdAReydQaYPEwjjh
tDl8sF0EZugbK9+++Q+ejKxe8r8TdyYgyy0=
-----END PRIVATE KEY-----"""
Alice_PublicKey = """-----BEGIN PUBLIC KEY-----
MIICJDCCARcGCSqGSIb3DQEDATCCAQgCggEBAOJuU92EQ9Z3ako9xyJc/uEy+Iy7
5jQtGocWJkBLXwN/LVNCYEyzexVsiXaE9y8paMQDTkIHA3dRbqWA77++qDf1Ti++
KN51WqItTumVDC+YQG/05UUY/IHLvwMxujsbN485/zn+AMoBxMXyOEZxxoU9FtjU
JNu7E6BU3nir7tHVzHhSxBx/oW9yx0M+s3rd9VJTVCPHI1zhA8D7//eTz7Q1QotN
pfshei8DCRjvOq4ETNGB7o0tZKOmdnrGZmg65t7yLLptCzV3i7vH7PBBF/lwO2/3
G/HWVC4xN8rWFzOW2jaGoHxThX4ORU/tfIB/B3KZWL+rPuFonoSBEmT7ms8CAQID
ggEFAAKCAQAjHx4KNha8o7tfhul1Hw9TgsfgwRNEdpZlBN4sagvMDJI7dwUPVI7h
Wm0DA8QrpBGlv2FwENSwfbQT3bWnosVdN29uW497+jcuwv3PVeJfQwEgMoKNFy+R
9cSPN0s4Ce4c80CWd+XQW5toZFGgyu1LMuKxfcZbHWImsjCznbhXIqh75z2KUfID
jj8CcktZyaSuNUHnIpq1+DGgmzNRh8L98tVOCFjYSPEqShbvHz7fcaO9ffaPqb5d
DfsITGtZrUmuq0hPTdSGAkHzF4yfAZa8P4UEmXcMU8cho5UjHSzTZyoNwBWtvWRx
VPgxfu19q+fFUZDwRhHn92nkjxR6sT5a
-----END PUBLIC KEY-----"""

Bob_PrivateKey = """-----BEGIN PRIVATE KEY-----
MIICJgIBADCCARcGCSqGSIb3DQEDATCCAQgCggEBAOJuU92EQ9Z3ako9xyJc/uEy
+Iy75jQtGocWJkBLXwN/LVNCYEyzexVsiXaE9y8paMQDTkIHA3dRbqWA77++qDf1
Ti++KN51WqItTumVDC+YQG/05UUY/IHLvwMxujsbN485/zn+AMoBxMXyOEZxxoU9
FtjUJNu7E6BU3nir7tHVzHhSxBx/oW9yx0M+s3rd9VJTVCPHI1zhA8D7//eTz7Q1
QotNpfshei8DCRjvOq4ETNGB7o0tZKOmdnrGZmg65t7yLLptCzV3i7vH7PBBF/lw
O2/3G/HWVC4xN8rWFzOW2jaGoHxThX4ORU/tfIB/B3KZWL+rPuFonoSBEmT7ms8C
AQIEggEEAoIBACWxjoeg0oiNqMc6vEEvTIa4TOSlPg7mJlwcAwpVEb4xdM88G6bf
8OJxpo4038d7+xZFB3DbxJf2LcpCJ2OfD3LZPJJS1Vai5CewsR24IykB9Iozj/Us
1mSr1pU8CAGSggCt+prwjKnPtkcsz0R/CX3WsbFAGgx2LqEpnByC9ju25Ulv30MY
r7ZJcnr7Hg7eDpjx7FZrfJx4aSIc8fHj+R8vgfNcj8eRdtj7T0xa2kVMnFFfTTce
G287GLVghllOsFYJz8A01hPAhKc/2Gkjyz2ld/oQ28vbC+WSqSPHqsbS+hO/J6Eu
ZmSZ46su12Ec+pELVIcuTUZ5EL9CBQPjgpg=
-----END PRIVATE KEY-----"""
Bob_PublicKey = """-----BEGIN PUBLIC KEY-----
MIICJDCCARcGCSqGSIb3DQEDATCCAQgCggEBAOJuU92EQ9Z3ako9xyJc/uEy+Iy7
5jQtGocWJkBLXwN/LVNCYEyzexVsiXaE9y8paMQDTkIHA3dRbqWA77++qDf1Ti++
KN51WqItTumVDC+YQG/05UUY/IHLvwMxujsbN485/zn+AMoBxMXyOEZxxoU9FtjU
JNu7E6BU3nir7tHVzHhSxBx/oW9yx0M+s3rd9VJTVCPHI1zhA8D7//eTz7Q1QotN
pfshei8DCRjvOq4ETNGB7o0tZKOmdnrGZmg65t7yLLptCzV3i7vH7PBBF/lwO2/3
G/HWVC4xN8rWFzOW2jaGoHxThX4ORU/tfIB/B3KZWL+rPuFonoSBEmT7ms8CAQID
ggEFAAKCAQBKVhtCTsGHsO8rAuqRxsIQoaZstLWW6Szmc4Jqd+zFI0U6i0FPkOeB
ikLm/uDesUI2IRl72C+2QVuGzBPsjigjNP8UDBa7DYDLcZgmaMu3ySx7hkMVQPEL
7YxJJA0dVx5YpYcJogE5a3P3HCwaXbUQBHD+A77FSBBvDoyMXmnDAP6+bDEvDxQw
OWMtDI5WOeRQUWVWnUQmqG9Lp1m5STkCc61uMSkDQxuYdlPsU13Mf/db3cbXtm4z
ge74dpI2Ns17sujzhfFpQX1CREOOcDED8/+DmeAWeSSiqma6L3DcqTl6tMW/fDgW
pJW74quhWQ+BQo+m+fvrIYxoQchIviGH
-----END PUBLIC KEY-----"""

KeyExchange("DH").getSharedSecret(Alice_PublicKey, Bob_PrivateKey)
# OUTPUT: 'miZRk/j2/E5XRDpMZKN9s3VcAmi4JbHumuD6FKkcAm2Be6uMIOYNSKkavkEOU1NAbkk4jZ9QI5ab8xSm559KbXjNdF27HYImuVeAVIO9Ny0VjUz7RU48duV8Iydc7D5iQX+3wHzwppJC3D/u4BrFVd3pIrrU8SwIelYyddcMrjxqMiGlZ0I0UzudnpGwzEZNHQ5MZUoOVZm19g4+xzm/gnj7VbuX54DIK2GxuOpaAtDEI+FbEjuTgWRMH3oOTzJHnaqko8lFhcDBJj891rSpshJ3XCO+WGyaHbEpV//IcsHVFSOVYS4m/z8CWq83AwSeO+6g/DCXDycjIFb8JT6Mwg=='
KeyExchange("DH").getSharedSecret(Bob_PublicKey, Alice_PrivateKey)
# OUTPUT: 'miZRk/j2/E5XRDpMZKN9s3VcAmi4JbHumuD6FKkcAm2Be6uMIOYNSKkavkEOU1NAbkk4jZ9QI5ab8xSm559KbXjNdF27HYImuVeAVIO9Ny0VjUz7RU48duV8Iydc7D5iQX+3wHzwppJC3D/u4BrFVd3pIrrU8SwIelYyddcMrjxqMiGlZ0I0UzudnpGwzEZNHQ5MZUoOVZm19g4+xzm/gnj7VbuX54DIK2GxuOpaAtDEI+FbEjuTgWRMH3oOTzJHnaqko8lFhcDBJj891rSpshJ3XCO+WGyaHbEpV//IcsHVFSOVYS4m/z8CWq83AwSeO+6g/DCXDycjIFb8JT6Mwg=='
```

---
### Crypto.Hash modules
**Usage scope in the configuration file:**
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `ProxyMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Request||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `HttpMessage||Response||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptRequest||[RequestIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||DecryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||LOOPVAR`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||CONDITION`
- `CipherTab||EncryptResponse||[ResponseIndex]||DATA||[DataIndex]||OUTPUT||[OutputIndex]||ExprStmt`

---
#### CRC32().checksum(message :str) -> str
```
CRC32().checksum('TPCyberSec')
# OUTPUT: '88d65e56'
```

---
#### HMAC_MD5().digest(message :str, SECRET_KEY :str) -> str
```
HMAC_MD5().digest('TPCyberSec', 'TPCS')
# OUTPUT: '\xe8e\xe8\xfc\xb2\xd5\xfd\xee!\xdd\xfc\x05D\x04\t\x0e'
```

---
#### HMAC_MD5().hexdigest(message :str, SECRET_KEY :str) -> str
```
HMAC_MD5().hexdigest('TPCyberSec', 'TPCS')
# OUTPUT: 'e865e8fcb2d5fdee21ddfc054404090e'
```

---
#### HMAC_SHA1().digest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA1().digest('TPCyberSec', 'TPCS')
# OUTPUT: ' :rd\xed\xac|^\xe8\xf8h\xd8\xd0\x8e\x11\x1a%\x81\x85\xf6'
```

---
#### HMAC_SHA1().hexdigest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA1().hexdigest('TPCyberSec', 'TPCS')
# OUTPUT: '203a7264edac7c5ee8f868d8d08e111a258185f6'
```

---
#### HMAC_SHA224().digest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA224().digest('TPCyberSec', 'TPCS')
# OUTPUT: 't\xf3j\xc1\xbf\x8a%\xa6r\xabB\xa0ci5N\x99\xf7\xf2\xc5\x92T:%\x8b8\xb0\xf2'
```

---
#### HMAC_SHA224().hexdigest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA224().hexdigest('TPCyberSec', 'TPCS')
# OUTPUT: '74f36ac1bf8a25a672ab42a06369354e99f7f2c592543a258b38b0f2'
```

---
#### HMAC_SHA256().digest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA256().digest('TPCyberSec', 'TPCS')
# OUTPUT: ">-\x914{y\xb7\x1fKS{\xdc\x15R\xb1'I\x08\x92*\x89\x1a$}\x85-u4=\x1bN\xea"
```

---
#### HMAC_SHA256().hexdigest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA256().hexdigest('TPCyberSec', 'TPCS')
# OUTPUT: '3e2d91347b79b71f4b537bdc1552b1274908922a891a247d852d75343d1b4eea'
```

---
#### HMAC_SHA384().digest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA384().digest('TPCyberSec', 'TPCS')
# OUTPUT: '\xaa\x98\xf0\xc4#D\xc1\xc3\xc9\x96\x11\xde\xa8\x92\xa7\x88;m\x92\x9f\xc6\x86\x1e\xae\x8bl\xf4\x08\x13\xf8u)\xc9kq\xa2O\x97\xa3C\x84O\xbc\x17\xf5\xe7\x19\xe1'
```

---
#### HMAC_SHA384().hexdigest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA384().hexdigest('TPCyberSec', 'TPCS')
# OUTPUT: 'aa98f0c42344c1c3c99611dea892a7883b6d929fc6861eae8b6cf40813f87529c96b71a24f97a343844fbc17f5e719e1'
```

---
#### HMAC_SHA512().digest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA512().digest('TPCyberSec', 'TPCS')
# OUTPUT: 'C\t\x16\xe09r\n\x0bH2{?q\xe2\xd4\xeb[\xf8\x8d\x1e\xc7\xfe_\xab2\x98\x99\xf8\x00\xe9<Bd]x\x87\x1c\x9fS\ti3\x11\xba\xcc\xc3\xa8\x0e\xdaNOR\x1e\xd39\n\xf9sG0\xeb,Yy'
```

---
#### HMAC_SHA512().hexdigest(message :str, SECRET_KEY :str) -> str
```
HMAC_SHA512().hexdigest('TPCyberSec', 'TPCS')
# OUTPUT: '430916e039720a0b48327b3f71e2d4eb5bf88d1ec7fe5fab329899f800e93c42645d78871c9f5309693311baccc3a80eda4e4f521ed3390af9734730eb2c5979'
```

---
#### MD2().digest(message :str) -> str
```
MD2().digest('TPCyberSec')
# OUTPUT: '\xbd\xeb.\x07l\x0c\x85\xd1I\x8d~t\xeej\xdb\xa4'
```

---
#### MD2().hexdigest(message :str) -> str
```
MD2().hexdigest('TPCyberSec')
# OUTPUT: 'bdeb2e076c0c85d1498d7e74ee6adba4'
```

---
#### MD5().digest(message :str) -> str
```
MD5().digest('TPCyberSec')
# OUTPUT: 'm\xaeKjs\xc427\xf0\x05h\x7f\x84\xb1\x02\xda'
```

---
#### MD5().hexdigest(message :str) -> str
```
MD5().hexdigest('TPCyberSec')
# OUTPUT: '6dae4b6a73c43237f005687f84b102da'
```

---
#### SHA1().digest(message :str) -> str
```
SHA1().digest('TPCyberSec')
# OUTPUT: '\x9f\xa1\xa6\xed<\xdc\xff\xff\xefA3tFb\xd8m\xc8\x8c\x92\xac'
```

---
#### SHA1().hexdigest(message :str) -> str
```
SHA1().hexdigest('TPCyberSec')
# OUTPUT: '9fa1a6ed3cdcffffef4133744662d86dc88c92ac'
```

---
#### SHA224().digest(message :str) -> str
```
SHA224().digest('TPCyberSec')
# OUTPUT: '.\xc1\xb9\xb4A[/\x90\xd7\xec_\xb35f\x7f\xec\xba9\xa4O\x18?\xfb\xaa*\xf9\x93\xa1'
```

---
#### SHA224().hexdigest(message :str) -> str
```
SHA224().hexdigest('TPCyberSec')
# OUTPUT: '2ec1b9b4415b2f90d7ec5fb335667fecba39a44f183ffbaa2af993a1'
```

---
#### SHA256().digest(message :str) -> str
```
SHA256().digest('TPCyberSec')
# OUTPUT: 'L\n\x99\xe8khH\xa5\x05*\xdcT\xd90\x81\x18U\xf8\x8e\xe5\xd7|F\x8b/U\xc18\x88 \xe6\xeb'
```

---
#### SHA256().hexdigest(message :str) -> str
```
SHA256().hexdigest('TPCyberSec')
# OUTPUT: '4c0a99e86b6848a5052adc54d930811855f88ee5d77c468b2f55c1388820e6eb'
```

---
#### SHA384().digest(message :str) -> str
```
SHA384().digest('TPCyberSec')
# OUTPUT: '\xca\xec^\x17b\x10\xd6\x9d\xa5Gy\rZR\xd5\x9a\xadv\x94\x9fD\x89IyK\xb9Y\xce&H\xdc\xa6|I\xd0hHL\x9f\x9c"2@/\x9f\x19\xc0\x1a'
```

---
#### SHA384().hexdigest(message :str) -> str
```
SHA384().hexdigest('TPCyberSec')
# OUTPUT: 'caec5e176210d69da547790d5a52d59aad76949f448949794bb959ce2648dca67c49d068484c9f9c2232402f9f19c01a'
```

---
#### SHA512().digest(message :str) -> str
```
SHA512().digest('TPCyberSec')
# OUTPUT: '\xbeue=?I\xe7\x9cD4G\xc2\xf3}Z_M\x11k\xb3e\xb3-\x9b\xea\x1d\xc3\xd3g\xe550&\xe1\xb7\xd0B\xeb\x05\x87\x84Nl]\t `\x05*0H\xa7\r\xb1\xd5\xf7\xfa\x11\x89*,\xf42Y'
```

---
#### SHA512().hexdigest(message :str) -> str
```
SHA512().hexdigest('TPCyberSec')
# OUTPUT: 'be75653d3f49e79c443447c2f37d5a5f4d116bb365b32d9bea1dc3d367e5353026e1b7d042eb0587844e6c5d092060052a3048a70db1d5f7fa11892a2cf43259'
```

---
# 📘 Basic Usage
## Rule Structure
```json
{
	"ProxyMessage": {
		"Request": [
			{
				"TARGET": StringRegex,
				"ENDPOINT": StringRegex,
				"PATTERN": List<StringRegex>,
				"DATA": [
					{
						"CONDITION": StringExpr,
						"OUTPUT": [
							{
								"LOOPVAR": String,
								"CONDITION": StringExpr,
								"exec_func": Boolean,
								"ExprStmt": StringExpr
							},
							...
						]
					},
					...
				]
			},
			...
		],
		"Response": [ ... ]
	},
	"HttpMessage": {
		"Request": [
			{
				"TARGET": StringRegex,
				"ENDPOINT": StringRegex,
				"PATTERN": List<StringRegex>,
				"DATA": [
					{
						"CONDITION": StringExpr,
						"OUTPUT": [
							{
								"LOOPVAR": String,
								"CONDITION": StringExpr,
								"exec_func": Boolean,
								"ExprStmt": StringExpr
							},
							...
						]
					},
					...
				]
			},
			...
		],
		"Response": [ ... ]
	},
	"CipherTab": {
		"EncryptRequest": [
			{
				"TARGET": StringRegex,
				"PATTERN": List<StringRegex>,
				"DATA": [
					{
						"CONDITION": StringExpr,
						"OUTPUT": [
							{
								"LOOPVAR": String,
								"CONDITION": StringExpr,
								"exec_func": Boolean,
								"ExprStmt": StringExpr
							},
							...
						]
					},
					...
				]
			},
			...
		],
		"DecryptRequest": [ ... ],
		"EncryptResponse": [ ... ],
		"DecryptResponse": [ ... ]
	}
}
```

## How to Write a Rule
Each rule in TP-BCF is defined in the JSON configuration file and consists of the following main components:
- **TARGET**: A regex string to match the domain you want the rule to apply to
- **ENDPOINT**: A regex string to match the specific endpoint or path you want the rule to apply to (ProxyMessage and HttpMessage only)
- **PATTERN**: A list of regex patterns to match specific content in the request or response
- **DATA**: A list of processing steps. Each step can have:
  - **CONDITION**: (Optional) A Python expression. If true, the OUTPUT block will be executed
  - **OUTPUT**: A list of actions to perform. Each action can have:
    - **LOOPVAR**: (Optional) An iterable variable for looping over items
    - **CONDITION**: (Optional) A Python expression for conditional execution inside the loop
    - **exec_func**: Boolean. If true, executes as a statement; if false, evaluates as an expression
    - **ExprStmt**: Python code to execute or evaluate

### Example Rule Structure
```json
{
  "HttpMessage": {
    "Request": [
      {
        "TARGET": "example.com",
        "ENDPOINT": "",
        "PATTERN": ["\"token\""],
        "DATA": [
          {
            "CONDITION": "",
            "OUTPUT": [
              {
                "LOOPVAR": "",
                "CONDITION": "",
                "exec_func": false,
                "ExprStmt": "RequestParser.request_body.get('token')['value']"
              },
              {
                "LOOPVAR": "",
                "CONDITION": "",
                "exec_func": true,
                "ExprStmt": "TEMP['decrypted_token'] = AESCipher('AES/CFB/NoPadding').decrypt(Utils.base64Decode(O[0]), envs['defaultSecretKey'], envs['defaultIV'])"
              },
              {
                "LOOPVAR": "",
                "CONDITION": "",
                "exec_func": false,
                "ExprStmt": "RequestParser.request_body.update('token', TEMP['decrypted_token'])"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### Tips
- Use built-in variables like `RequestParser`, `ResponseParser`, `envs`, `TEMP`, `O`, and `LOOPDATA` for data extraction and transformation
- Use built-in modules and functions for cryptographic operations and data manipulation
- You can chain multiple OUTPUT actions for complex workflows
- For looping over arrays or lists, set `LOOPVAR` to the iterable and use `LOOPDATA` inside your expressions

See the [examples](./example/) directory for more sample rules

#### [TP BCF] Decrypt Interactsh response
[![\[TP BCF\] Decrypt Interactsh response](https://img.youtube.com/vi/Ip12vB2wWG8/0.jpg)](https://www.youtube.com/watch?v=Ip12vB2wWG8 "[TP BCF] Decrypt Interactsh response")

---
# 👥 Contributors

---
# 📝 CHANGELOG
### [TP-BCF v2026.6.30](https://github.com/TPCyberSec/TP-BCF/tree/2026.6.30)
- **Added**: KeyExchange for generating a shared secret
- **Added**: Proxy Handlers menu with Requests and Responses options
- **Updated**: Parsing and processing of request/ response containing duplicate JSON keys
- **Added**: ECDSA signature generation and verification
- **Added**: RSA encyption/ decryption functions with support for various padding schemes ("RSA/ECB/OAEPWithSHA-1AndMGF1Padding", "RSA/ECB/OAEPWithSHA-224AndMGF1Padding", "RSA/ECB/OAEPWithSHA-384AndMGF1Padding", "RSA/ECB/OAEPWithSHA-512AndMGF1Padding")

### [TP-BCF v2026.5.18](https://github.com/TPCyberSec/TP-BCF/tree/2026.5.18)
- **Added**: Handle HTTP Requests/ Responses at the Proxy tab with the `ProxyMessage` rules, allowing users to intercept and modify traffic before it reaches the target server or after it leaves the server, providing more control over the data flow
- **Added**: RSA encyption/ decryption functions with support for various padding schemes ("RSA/ECB/OAEPPadding", "RSA/ECB/OAEPWithSHA-256AndMGF1Padding")

### [TP-BCF v2026.3.15](https://github.com/TPCyberSec/TP-BCF/tree/2026.3.15)
- **Updated**: Encryption/ Decryption and Signature/ Verify functions accept raw data as input. Encryption and Signature return Base64-encoded data, while Decryption returns raw data, allowing more flexible use cases

### [TP-BCF v2025.12.18](https://github.com/TPCyberSec/TP-BCF/tree/2025.12.18)
- **Added**: New field `ENDPOINT` to match specific endpoint or path in `HttpMessage` rules
- **Added**: New menu item `Reload Refresh TARGETS Config` to manually reload all target configurations

### [TP-BCF v2025.9.18](https://github.com/TPCyberSec/TP-BCF/tree/2025.9.18)
- **Fixed**: Issue when installing dependencies
- **Updated**: Change the inputs and outputs of the encrypt/decrypt and signature/verify functions
- **Fixed**: Security issue
- **Added**: New tool name (**fromTool**) sent the request
- **Updated**: Set the default to disable intercepting request/response traffic from the `Proxy` and `Extender` tools

### [TP-BCF v2025.8.24](https://github.com/TPCyberSec/TP-BCF/tree/2025.8.24)
- Initial release of TP-BCF
- Support for intercepting and rewriting HTTP Requests/ Responses
- Add Cipher Tab for manual Encryption/ Decryption
- Support built-in symmetric, asymmetric, and hash-based cryptography
- JSON-based configuration for custom rules

---