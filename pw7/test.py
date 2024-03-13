import os
import getpass
print(os.getcwd())
os.chdir(f"/home/{getpass.getuser()}")
print(os.getcwd())