import pika

# Create a connection to the RabbitMQ server
class rabbitMQ_send():
    def __init__(self, AMQP_URL, ROUTING_KEY):
        self.AMQP_URL = AMQP_URL
        self.ROUTING_KEY = ROUTING_KEY
        self.connection = pika.BlockingConnection(pika.URLParameters(self.AMQP_URL))
        self.channel = self.connection.channel()

    def send_message(self, message):
        self.channel.queue_declare(queue=message)

        self.channel.basic_publish(exchange='', routing_key=self.ROUTING_KEY, body=message)
        print(f" sent {message}")
    
# test
AMQP_URL = "amqps://wqzfdbgv:H0k0rWOPf6vTBaFCgJ35vZgWn657nAQZ@albatross.rmq.cloudamqp.com/wqzfdbgv"
ROUTING_KEY = "hello"
message = "hello world"
rabbitMQ_send(AMQP_URL, ROUTING_KEY).send_message(message)
