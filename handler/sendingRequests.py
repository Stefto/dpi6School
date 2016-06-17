import sys
import json
from send import sending


s = sending()
if (sys.argv[1] == '1'):
    command = {'command': '1'}
    print(json.dumps(command))
    s.send('localhost', 'Sesame', 'Sesame', json.dumps(command))
if (sys.argv[1] == '2'):
    command =  {'command': '2','itemid':sys.argv[2] }
    print(json.dumps(command))
    s.send('localhost', 'Sesame', 'Sesame', json.dumps(command))