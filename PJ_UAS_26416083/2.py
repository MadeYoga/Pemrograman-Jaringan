import imaplib
import sys
import getpass

try:
	HOST = sys.argv[1]
	USERNAME = sys.argv[2]
except Exception as e:
	print("Not a valid pattern\nvalid: python 1.py <host> <username>")
	print(e)
	exit()

try:
	print("Checking host Service...")
	imap = imaplib.IMAP4(HOST)
	PASSWORD = getpass.getpass()
	print("Login...")
	imap.login(USERNAME, PASSWORD)
	imap.select()
	print("Login Successful!")
	imap.close()
	imap.logout()
except Exception as e:
	print(e)