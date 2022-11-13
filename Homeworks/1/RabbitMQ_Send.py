import pika


# Create a connection to the RabbitMQ server
class rabbitMQ_send():
    def __init__(self):
        self.AMQP_URL = "amqps://wqzfdbgv:H0k0rWOPf6vTBaFCgJ35vZgWn657nAQZ@albatross.rmq.cloudamqp.com/wqzfdbgv"
        self.ROUTING_KEY = 'hello'
        self.connection = pika.BlockingConnection(pika.URLParameters(self.AMQP_URL))
        self.channel = self.connection.channel()

    def send_message(self, message):
        self.channel.queue_declare(queue='hello')

        self.channel.basic_publish(exchange='', routing_key=self.ROUTING_KEY, body=message)
        print(f" sent {message}")
    
# test

# message = "hello world"
# rabbitMQ_send().send_message(message)
