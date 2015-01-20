#!/usr/bin/env python
# coding: utf-8

import cgi
form = cgi.FieldStorage()

html_body = u"""
<html>
  <head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8">
  </head>
  <body>
  {0:s}
  </body>
</html>"""

content = ''
for cnt, item in enumerate(form.getvalue('language')):
    content += "{0:d} : {1:s} <br />".format(cnt+1, item)

print "Content-type: text/html\n"
print(html_body.format(content))
