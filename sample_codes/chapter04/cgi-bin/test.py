#!/usr/bin/env python3

import datetime

#フォーマット文字列の作成
html_body = """
<html><body>
%Y/%m/%d %H:%M:%S
</body></html>"""

now = datetime.datetime.now()

print("Content-type: text/html\n")
print(html_body.format(now))


