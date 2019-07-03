#! /usr/bin/env python2
import simplejson as json

with open('data.json', 'r') as f:
    data = json.load(f)

xml= {}
python= {}


for k in  data.iterkeys():
    body = data[k]['body']
    prefix = data[k]['prefix']
    scope = data[k]['scope']
    description = data[k]['description']
    bl = body.split('\n')
    data[k]['body'] = bl
   
    new_data ={}
    new_data.update( { 'body': bl, 'prefix':prefix, 'description': description })

    if 'source.python' in scope:
        python.update( { k: new_data })

    if 'text.xml' in scope:
        xml.update( { k: new_data })

with open('../snippets/python.json', 'w') as p:
    p.write(json.dumps(python, indent=4, sort_keys=True))
with open('../snippets/xml.json', 'w') as x:
    x.write(json.dumps(xml, indent=4, sort_keys=True))
