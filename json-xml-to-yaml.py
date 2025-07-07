#!/usr/bin/env python3
# JSON/XML to YAML Converter

print('JSON/XML to YAML Converter')


try:
    from xmltodict import parse
except:
    print(' Need to install netmiko package.\n Command line: "pip install xmltodict"')
    input('\nPress Enter to exit...')
    quit()


try:
    from yaml import dump, Dumper
except:
    print(' Need to install netmiko package.\n Command line: "pip install pyyaml"')
    input('\nPress Enter to exit...')
    quit()



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
