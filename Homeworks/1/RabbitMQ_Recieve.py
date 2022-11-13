import pika
import sys
import os
import Object_Storage as Obj
import Image_Tagging as Tag
import Database
import Email

db = Database.Database()

class RabbitMQ_Receive():
    def __init__(self):
        self.AMQP_URL = "amqps://wqzfdbgv:H0k0rWOPf6vTBaFCgJ35vZgWn657nAQZ@albatross.rmq.cloudamqp.com/wqzfdbgv"
        self.connection = pika.BlockingConnection(
            pika.URLParameters(self.AMQP_URL))
        self.channel = self.connection.channel()
        self.queue = 'hello'
        

    def receive(self):
        self.channel.queue_declare(queue=self.queue)

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            body = body.decode('utf-8')
            id = int(os.path.splitext(body)[0])
            extention = os.path.splitext(body)[1]
            file_name = body
            file_name = Obj.S3().download_file(id, extention)
            tag, is_vehicle = Tag.ImageTagging().get_tags(file_name)
            if is_vehicle:
                state = 2
                db.update_data(id=id, state=state, category=tag)
                email = db.get_email(id)
                text = ' تبلیغ شما تایید شد'
                subject = 'تایید تبلیغ'
                Email.SendEmail().send_message(email, text, subject)

            if is_vehicle is False:
                state = 1
                db.update_data(id=id, state=state, category=tag)
                email = db.get_email(id)
                text = 'تبلیغ شما تایید نشد'
                subject = 'رد تبلیغ'
                Email.SendEmail().send_message(email, text, subject)
            
            print('Email Sent!')

            # print(" [x] Received %r" % body)
        
        self.channel.basic_consume(
            queue=self.queue, on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()



print(RabbitMQ_Receive().receive())
