import rabbitMQ

rabbitMQ.send('hello', 'hello world')

rabbitMQ.receive('hello')