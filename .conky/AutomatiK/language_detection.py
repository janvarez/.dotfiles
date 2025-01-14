import os

def detect_language():
	Language_installed=os.popen("locale | grep LANG").read()
	if "fr" in Language_installed:
		Language="French"
	elif "de" in Language_installed:
		Language="German"
	elif "pt" in Language_installed:
		Language="Portuguese"
	elif "it" in Language_installed:
		Language="Italian"
	else:
		Language="English"
	return Language
