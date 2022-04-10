import pika


params = pika.URLParameters("amqp://guest:guest@157.230.201.187:5672")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.exchange_declare('test_exchange')
channel.queue_declare(queue='test_queue')
channel.queue_bind('test_queue', 'test_exchange', 'tests')

class Publish:
    def publish(self):
        channel.basic_publish(
            exchange='test_exchange',
            routing_key='tests',
            body='hello'
        )

x = Publish
x.publish(x)

channel.close()
connection.close()
© 2022 GitHub, Inc.
