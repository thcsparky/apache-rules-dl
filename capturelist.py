import os
import requests
import json

filenames = []
link = 'https://rules.emergingthreats.net/open/old/snort-2.8.6/rules/'
o = requests.get(link)
a = o.text

## <a href="emerging-web_client.rules">emerging-web_client.rules</a>

listy = []
e = str(a)
e = e.split('<a href="')
for x in e:
    z = x.split('">')[0]
    listy.append(z)
it = 0

print('initiating download sequence\n\n')
## \'<!
output = os.getcwd() + '/'
for x in listy:

    if x.find('.rules') > -1:
        print('Downloading: ' + link + x + '\n')

        no = requests.get(link + x)
        filenames.append('include $RULE_PATH/' + x)

        o = no.text
        o = str(o)
        print('Saving to: ' + output + x + '\n')
        file = open(output + x, 'w')
        file.write(o)
        file.close()


##save the names
strout = ''
for x in filenames:
    strout += x + '\n'

file = open(os.getcwd() + '/list.txt', 'w')
file.write(strout)
file.close()

print('Complete, i have made a pre format for your snort config as list.txt')
