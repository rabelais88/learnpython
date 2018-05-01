#!/user/bin/env python3
#run command  - py -m http.server --cgi 8080
#then connect to address: localhost:8080/cgi-bin/webchat.py

import cgi
import cgitb
import os.path
import html

cgitb.enable()

FILE_LOG = "chat-log.txt"

def print_html(body):
  print("Content-Type: text/html; charset=utf-8")
  print("")
  print("""
<html>
  <head>
    <meta charset="utf-8">
    <title>chat program</title>
  </head>
  <body>
    <h1>cgi-chatting app</h1>
    <div>
      <form>
        Name: <input type="text" name="name" size="8"/>
        Text: <input type="text" name="body" size="20"/>
        <input type="submit" value="say"/>
        <input type="hidden" name="mode" value="write">
      </form>
    </div>
    <hr>
    {0}
  </body>
</html>
  """.format(body))

def mode_read(form):
  log = ""

  if os.path.exists(FILE_LOG):
    with open(FILE_LOG, "r", encoding='utf-8') as f:
      log = f.read()
  print_html(log)

def jump(url):
  print("Status: 301 Moved Permanently")
  print("Localtion: " + url)
  print("")
  print('<html><head>')
  print('<meta http-equiv="refresh" content="0;' + url + '">')
  print('</head></body>')
  print('<a href="' + url + '">jump</a></body></html>')

def mode_write(form):
  name = form.getvalue("name", "no name")
  body = form.getvalue("body","")

  name = html.escape(name)
  body = html.escape(body)

  with open(FILE_LOG, "a+", encoding='utf-8') as f:
    f.write("<p>{0}: {1}</p><hr>\n".format(name,body))
  jump('webchat.py') # === res.redirect in Node.js

def main():
  form = cgi.FieldStorage()
  mode = form.getvalue("mode","read")

  if mode == "read": mode_read(form)
  elif mode =="write":mode_write(form)
  else:mode_read(form)


if __name__ == "__main__":
  main()