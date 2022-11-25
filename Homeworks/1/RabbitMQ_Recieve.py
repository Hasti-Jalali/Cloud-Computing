import pika
import sys
import os
import Object_Storage as Obj
import Image_Tagging as Tag
import database
import Email


class RabbitMQ_Receive():
    def __init__(self):
        self.AMQP_URL = "amqps://wqzfdbgv:H0k0rWOPf6vTBaFCgJ35vZgWn657nAQZ@albatross.rmq.cloudamqp.com/wqzfdbgv"
        self.connection = pika.BlockingConnection(
            pika.URLParameters(self.AMQP_URL))
        self.channel = self.connection.channel()
        self.queue = 'hello'
        print('start')
        self.db = database.Database()
        

    def receive(self):
        '''Receive a message from the RabbitMQ server.'''
        self.channel.queue_declare(queue=self.queue)

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            body = body.decode('utf-8')
            id = int(os.path.splitext(body)[0])
            extention = os.path.splitext(body)[1]
            file_name = body
            file_name = Obj.S3().download_file(id, extention)
            tag, is_vehicle = Tag.ImageTagging().get_tags(file_name)
            os.remove(file_name)
            if is_vehicle:
                state = 2
                self.db.update_data(id=id, state=state, category=tag)
                email = self.db.get_email(id)
                text = f'Your Advertisement with id: {id} is approved and your category is {tag}'
                subject = 'Approve Advertisment'
                Email.SendEmail().send_message(email, subject, text)

            if is_vehicle is False:
                state = 1
                self.db.update_data(id=id, state=state, category=tag)
                email = self.db.get_email(id)
                text = f'Your Advertisement with id: {id} is rejected because it is not a vehicle'
                subject = 'Reject Advertisment'
                Email.SendEmail().send_message(email, subject, text)
            
            print('Email Sent!')

            # print(" [x] Received %r" % body)
        
        self.channel.basic_consume(
            queue=self.queue, on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()



RabbitMQ_Receive().receive()
