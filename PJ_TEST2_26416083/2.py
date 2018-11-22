import getpass
import sys

domain = sys.argv[1]
username = sys.argv[2]

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

print(dir_path)

import poplib

M = poplib.POP3(domain)
M.user(username)

password = getpass.getpass()

try:
    M.pass_(password)
    print(len(M.list()[1]))
    print("Berhasil Login!")
except Exception as e:
    print(e)
