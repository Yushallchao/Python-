#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author xiao

import lxml.etree

doc = lxml.etree.parse("country.xml")

for node in doc.xpath("//PAT_NAME"):
    print(node.tag, node.text)