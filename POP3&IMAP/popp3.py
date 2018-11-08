import poplib
import getpass

M = poplib.POP3('john.petra.ac.id')
try:
    M.user(input("input user?"))
    # M.user(getpass.getuser())
    M.pass_(getpass.getpass())
    print(len(M.list()[1]))
except Exception as e:
    print(e)
