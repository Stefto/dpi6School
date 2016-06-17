import pika
from send import sending
from facade import facade
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

fac = facade()

channel.queue_declare(queue='Sesame')

#main method
def callback(ch, method, properties, body):
    received = json.loads(body)

    if (received['command'] == '1'):
        result = fac.getAllHDDs()
        result = result.__dict__
        print(result)
        sending().send('localhost','result','result',json.dumps(result) )
    if (received['command'] == '2'):
        result= fac.getHDDByItemID(received['itemid'])
        result = result.__dict__
        print(result)
        sending().send('localhost','result','result',json.dumps(result) )
    else:
        print('No valid json Received')


    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='Sesame',
                      no_ack=True)

print(' [*] sever active, pres CTRL+C to exit')
channel.start_consuming()