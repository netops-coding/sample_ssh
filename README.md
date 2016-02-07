#sample_ssh
It's sample code for configuration to a router by SSH module.
It was posted the following blog(in Japanese).
http://qiita.com/taijijiji/items/351c48a8a77ee56f6e79

#Install

```
pip install Exscript
```

```
git clone git@github.com:netops-coding/sample_ssh.git
```

# How to use
## show_junos.py
It runs 'show configuration' command to JUNOS router.

How to run

```
python show_junos.py
```

Output

```
========================================
Step 1. run show command
========================================
show configuration interfaces xe-0/0/0 | no-more
disable;

user1@router>
```

## set_junos.py

It runs the following configuration command to JUNOS router.

``` junos_config.txt
delete interfaces xe-0/0/0 disable
set interfaces xe-0/0/0 unit 0 family inet address 10.0.0.1/30
```

How to run

```
python set_junos.py junos_config.txt
```

```
========================================
Step 1. run show command
========================================
show configuration interfaces xe-0/0/0 | no-more
disable;

user1@router>
========================================
Step 2. read config file
========================================
junos_config.txt
['delete interfaces xe-0/0/0 disable\n', 'set interfaces xe-0/0/0 unit 0 family inet address 10.0.0.1/30\n']
========================================
Step 3. run configure command
========================================
delete interfaces xe-0/0/0 disable

[edit]
user1@router#

[edit]
user1@router#
set interfaces xe-0/0/0 unit 0 family inet address 10.0.0.1/30

[edit]
user1@router#

[edit]
user1@router#
========================================
Step 4. commit check
========================================
show | compare
[edit interfaces xe-0/0/0]
-   disable;
[edit interfaces xe-0/0/0]
+    unit 0 {
+        family inet {
+            address 10.0.0.1/30;
+        }
+    }

[edit]
user1@router#
commit check
configuration check succeeds

[edit]
user1@router#
========================================
Step 5. commit
========================================
Do you commit? y/n
y
commit
commit complete

[edit]
user1@router#
exit
Exiting configuration mode

user1@router>
========================================
Step 6. run show command(again)
========================================
show configuration interfaces xe-0/0/0 | no-more
unit 0 {
    family inet {
        address 10.0.0.1/30;
    }
}

user1@router>
```
