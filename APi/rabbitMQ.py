import pika

class rabbitmq:
    host = 'localhost'

    def send(self, que, msg):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            self.host
        ))
        channel = connection.channel()

        channel.queue_declare(queue=que)
        channel.basic_publish(exchange='',routing_key=que,body=msg)

        print('sent hello world.')

        connection.close();

    def receive(self, que):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            self.host
        ))
        channel = connection.channel()
        channel.queue_declare(queue=que)

        channel.basic_consume(self.callback,queue=que, no_ack=True)

        print("Currently in listening mode, to exit pres CTRL+C")

        channel.start_consuming()

    def callBack(self,ch,method,properties,body):
        print(" [x] Received %r" % body)
