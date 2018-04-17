#!/usr/bin/env python3
#run command  - py -m http.server --cgi 8080
#then connect to address: localhost:8080/cgi-bin/webcalc.py

import cgi
#below is necessary for debug(enable error report on web)
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print("")

form = cgi.FieldStorage()

if (not 'v1' in form) or (not 'v2' in form):
  print("""
    <form>
    <input type="text" name="v1"> +
    <input type="text" name="v2">
    <input type="submit" value="calculate">
    </form>
  """)
else:
  v1 = form.getvalue("v1")
  v2 = form.getvalue("v2")
  try:
    ans = int(v1) + int(v2)
  except:
    ans = 0
  print("<h1>", ans, "</h1>")