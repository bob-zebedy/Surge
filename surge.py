#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from string import Template

url = "https://bpnigk.xyz/?L2Rvd25sb2FkQ29uZmlnL05vZGVMaXN0LmFzcHg/dXJrPTI5OWE4YjE0LWU2YTgtNDkxZC05OTQwLTY5NTJjZjUxNzMxNyZtbT02Nzc5MSYzNWQyNWRkMTc0NDY0OTk3OTYxMmUzMGVjZQ=="
response = requests.get(url, timeout=5)
proxy = ""
proxy_group = []
cust = "🇺🇸 Los Angeles = ss, shadowsocks.zebedy.com, 10240, encrypt-method=xchacha20-ietf-poly1305, password=NrO2ltTiJfDxumG4, obfs=http, obfs-host=world.taobao.com, tfo=true, udp-relay=true"
if response.status_code == 200:
    response = response.text

if response:
    for line in response.split("\n"):
        if line:
            if ("Hong Kong" in line or "USA Seattle" in line) and "Premium" not in line:
                if "Hong Kong 23" in line:
                    line = line.replace("Hong Kong 23", "Hong Kong 20")
                proxy += line + "\n"
    proxy += cust
print(proxy)

for line in proxy.split("\n"):
    if line:
        name = line.split(" = ")[0]
        proxy_group.append(name)

proxy_group = ", ".join(proxy_group)
print(proxy_group)

with open("surge.template", "r") as f:
    surge_template = Template(f.read())
    surge = surge_template.substitute(proxy=proxy, proxy_group=proxy_group)
    with open("surge", "w") as ff:
        ff.write(str(surge))
