from rabbitMQ import rabbitmq
import sys

rabb = rabbitmq()
msg = ' '.join(sys.argv[1:]) or 'hello world'
rabb.send('hello', msg)

rabb.receive('hello')