#! /usr/bin/env python2
import simplejson as json

with open('../snippets/python.json', 'r') as f:
    data = json.load(f)

print('Python')
print("""| prefix | description |
---------|--------------|""")

for k in sorted(data.keys()):
    # print(k)

    prefix = data[k]['prefix']

    description = data[k]['description']

    print('| %s | %s  |' % (prefix, description))

with open('../snippets/xml.json', 'r') as f:
    data = json.load(f)

print('XML')
print("""| prefix | description |
---------|--------------|""")

for k in sorted(data.keys()):
    # print(k)

    prefix = data[k]['prefix']

    description = data[k]['description']

    print('| %s | %s  |' % (prefix, description))
