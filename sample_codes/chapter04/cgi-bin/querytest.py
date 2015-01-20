#!/usr/bin/env python
# coding: utf-8

html_body = u"""
<html>
  <body>
  {:s}
  </body>
</html>"""

import cgi
form = cgi.FieldStorage()

#header
print("Content-type: text/html\n")

print(html_body.format(form['foo'].value))
