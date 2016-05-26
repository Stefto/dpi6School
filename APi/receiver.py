import pika

que ='hello'
host='localhost'


connection = pika.BlockingConnection(pika.ConnectionParameters(
host
))
channel = connection.channel()
channel.queue_declare(queue=que)


def callBack(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callBack,queue=que, no_ack=True)

print("Currently in listening mode, to exit pres CTRL+C")
channel.start_consuming()
