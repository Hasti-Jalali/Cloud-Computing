import pika
import sys
import os


class RabbitMQ_Receive():
    def __init__(self, AMQP_URL, queue):
        self.AMQP_URL = AMQP_URL
        self.connection = pika.BlockingConnection(
            pika.URLParameters(self.AMQP_URL))
        self.channel = self.connection.channel()
        self.queue = queue
        

    def receive(self):
        self.channel.queue_declare(queue=self.queue)

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
        self.channel.basic_consume(
            queue=self.queue, on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()


AMQP_URL = "amqps://wqzfdbgv:H0k0rWOPf6vTBaFCgJ35vZgWn657nAQZ@albatross.rmq.cloudamqp.com/wqzfdbgv"


queue = "hello"
print(RabbitMQ_Receive(AMQP_URL, queue).receive())
