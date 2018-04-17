#run command  - py -m http.server --cgi 8080
#then connect to address: localhost:8080/cgi-bin/webapp1.py
#this file must be placed at ./cgi-bin/webapp1.py
print("Content-Type: text/html;charset=utf-8")
print("") #header and content

print("<html><head><meta charset='utf-8'></head><body>")
print("we're testing the basic of python webapp")
print("</body></html>")