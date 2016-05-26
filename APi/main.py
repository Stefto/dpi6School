from rabbitMQ import rabbitmq

rabb = rabbitmq()

rabb.send('hello', 'hello world')

rabb.receive('hello')