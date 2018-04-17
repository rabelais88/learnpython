#!/user/bin/env python3

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
        <!--- TODO: further work needed here --->
        <input
      </form>
    </div>
  </body>
</html>
  """)