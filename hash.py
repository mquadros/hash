import hashlib, os, base64

def hash(password):
	h = hashlib.sha256()
	salt = os.urandom(64)
	salt = str(base64.b16encode(salt))
	h.update(password.encode('utf-8'))
	h.update(salt.encode('utf-8'))
	return [h.hexdigest(),salt];

def match(h1,s,p):
	h2 = hashlib.sha256()
	h2.update(p.encode('utf-8'))
	h2.update(s.encode('utf-8'))
	p1 = h1
	p2 = h2.hexdigest()
	if(p1==p2):
		return(True)
	else:
		return(False)

