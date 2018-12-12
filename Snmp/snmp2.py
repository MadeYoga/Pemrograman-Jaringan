import netsnmp
import time

ip = raw_input("input host: ")

try:
        # check apakah ada sess
        sess = netsnmp.Session(Version=2, DestHost=ip, Community="public")
except Exception as e:
        print(e)

# vars = netsnmp.VarList(netsnmp.Varbind('iso.3.6.1.2.1.2.2.1.2'))
vars = netsnmp.VarList(netsnmp.Varbind('1.3.6.1.2.1.17.7.1.2.2.1.2'))
a = sess.walk(vars)
print(a)
now = sess.get(vars)[0]
for loop in range (100):
        print("Time " + str(loop) + ":")
        print(now)
        time.sleep(1)
        next = sess.get(vars)[0]
        gap = int(next) - int(now)
        now = next
        print("Gap: " + str(gap))
