#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Exscript.protocols import SSH2
from Exscript.Account import Account

username = 'user1'
password = 'pass1'
ipv4 = '192.168.0.1'

session = SSH2()
session.connect(ipv4)
session.login(Account(name=username, password=password))


print '='*40
print 'Step 1. run show command'
print '='*40
session.execute('show configuration interfaces xe-0/0/0 | no-more')
print session.response


print '='*40
print 'Step 2. read config file'
print '='*40
config_filename = sys.argv[1]
with open(config_filename, 'r') as config_file :
    config_lines = config_file.readlines()
    print config_filename
    print config_lines


print '='*40
print 'Step 3. run configure command'
print '='*40
session.execute('configure')
for config_line in config_lines :
    session.execute(config_line)
    print session.response


print '='*40
print 'Step 4. commit check'
print '='*40
session.execute('show | compare')
print session.response
session.execute('commi check')
print session.response


print '='*40
print 'Step 5. commit'
print '='*40
print 'Do you commit? y/n'
choice = raw_input().lower()
if choice == 'y':
    session.execute('commit')
    print session.response
else:
    session.execute('rollback')
    print session.response
session.execute('exit')
print session.response


print '='*40
print 'Step 6. run show command(again)'
print '='*40
session.execute('show configuration interfaces xe-0/0/0 | no-more')
print session.response


if session:
    session.send('exit\r')
    session.close()
else:
