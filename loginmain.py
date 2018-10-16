# ! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os.path
if os.path.exists("usename"):
    login()
else:
        make_account()

    def make_account

filename = ("username");
with open (filename, "w") as f:
  f.write (input("Enter a username: "));

filename = ("password");
with open (filename, "w") as f:
  f.write (input("Enter a password: "));


def login
username = input("Enter your username: ")
password = input("Enter your password: ")
check()

def check
if username == open("username").read(): and
passsword == open("password").read():
    print("Successful login")
else:
    print('Incorrect')