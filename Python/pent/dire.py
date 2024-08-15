import requests as re 
import sys

sub_list = open("GENERIC WORDFILE").read()
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    r = re.get(dir_enum)
    if r.status_code == 404:
        pass
    else:
        print("Valid directory:", dir_enum)