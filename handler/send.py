import pika

class sending:

    def send(self, host,que,routekey, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host))
        channel = connection.channel()

        channel.queue_declare(queue=que)

        channel.basic_publish(exchange='',
                      routing_key=routekey,
                      body=message)
        print(" [x] Sent %r", message)
        connection.close()