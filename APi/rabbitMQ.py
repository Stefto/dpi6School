import pika

class rabbitmq:
    host = ''

    def __init__(self):
        host = 'localhost'

    def send(self, que, msg):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            self.host
        ))
        channel = connection.channel()

        channel.queue_declare(queue=que)
        channel.basic_publish(exchange='',
                              routing_key=que,
                              body=msg,
                              properties=pika.BasicProperties(delivery_mode= 2))#makes messages persist


        print('sent hello world.')

        connection.close();


