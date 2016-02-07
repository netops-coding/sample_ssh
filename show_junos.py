
m Exscript.protocols import SSH2
from Exscript.Account import Account

username = 'user1'
password = 'pass1'
ipv4 = '192.168.0.1'

# establish ssh session
session = SSH2()
session.connect(ipv4)

# login a target router 
session.login(Account(name=username, password=password))

# send a command to router and get output
print '='*40
print 'Step 1. run show command'
print '='*40
session.execute('show configuration interfaces xe-0/0/0 | no-more')
print session.response

# close SSH session
if session:
    session.send('exit\r')
    session.close()
else:
    raise AttributeError('Cannot find a livied session')
