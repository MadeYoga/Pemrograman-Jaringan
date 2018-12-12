from ftplib import FTP
import getpass
import sys
try:
	HOST = sys.argv[1]
	USERNAME = sys.argv[2]
	FILENAME = sys.argv[3]
	print(HOST, USERNAME, FILENAME)
except Exception as e:
	print("Not a valid pattern\nvalid: python 1.py <host> <username> <filename>")
	print(e)
	exit()

try:
	ftp = FTP(HOST)
	PASSWORD = getpass.getpass()
	print('Login...')
	ftp.login(USERNAME, PASSWORD)
	print('Login Successful!')
	print('Checking if file exist...')
	files = ftp.nlst()
	if FILENAME	in files:
		print('File Exist!')
		print('\nDownloading {}...'.format(FILENAME))
		ftp.retrbinary(
			'RETR {}'.format(FILENAME), 
			open("{}".format(FILENAME), "wb").write
			)
		print('File downloaded!')
	else:
		print('File {} is not exist\nno such file or directory'.format(FILENAME))
except Exception as e:
	print(e)
