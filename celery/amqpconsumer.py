

import pika


params = pika.URLParameters('amqp://guest:guest@157.230.201.187:5672')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='test_queue')


def callback(ch, method, properties, body):
    print(' [x] Received ' + str(body))

channel.basic_consume(queue='test_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [x] Waiting for messages')
channel.start_consuming()
connection.close()

channel.start_consuming()

connection.close()
