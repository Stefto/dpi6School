import sys
import json
from send import sending


s = sending()
if (sys.argv[0] == '1'):
    command = '{"command": "1"}'
    s.send('localhost', 'Sesame', 'sesame', json.dumps(command))
if (sys.argv[0] == '2'):
    command = '{"command": "1","itemid":' + sys.argv[1] + ' }'
    s.send('localhost', 'Sesame', 'sesame', json.dumps(command))