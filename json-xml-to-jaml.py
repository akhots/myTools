#!/usr/bin/env python3
# JSON/XML to YAML Converter

print('JSON/XML to YAML Converter')

from xmltodict import parse
from yaml import dump, Dumper
from json import loads

class IndentedDumper(Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentedDumper, self).increase_indent(flow, False)


src_f = input('Enter file name: ')
frmt_f = input('Enter format [xml/json]: ').strip().lower()

with open(src_f + '.' + frmt_f) as f:
    src = f.read()


if frmt_f == 'xml':
    dct = parse(src)
elif frmt_f == 'json':
    dct = loads(src)

# dst = dump(dct, sort_keys=False)
dst = dump(dct, Dumper=IndentedDumper, sort_keys=False)


with open(src_f + '.yml', 'w') as f:
    f.write(dst)

input('\nDone')
