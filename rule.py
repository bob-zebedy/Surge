#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def providers(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            yield filepath


for provider in providers('Provider'):
    print(f"正在处理 {provider}...")
    data = {}
    with open(provider, "r+") as file:
        for line in file:
            line = line.strip()
            if line:
                spline = list(map(lambda x: x.strip(), line.split(",")))
                key, value = spline[0], ", ".join(spline[1:])
                if key in data:
                    data[key].append(value)
                else:
                    data[key] = []
                    data[key].append(value)
        for _, v in data.items():
            v.sort()
        file.seek(0)
        file.truncate()
        for k, v in data.items():
            for r in v:
                file.write(f"{k}, {r}\n")
            file.write("\n")
