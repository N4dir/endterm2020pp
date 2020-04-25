import pika
import time

def callback(ch, method, properties, body):
    print('[x] received %r' % body)
    time.sleep(body.count(b'.'))
    print('[x] done')
    ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


#FANOUT TYPE EXCHANGE BROADCAST ALL THE MESSAGES IT RECEIVES
#TO ALL THE QUEUES IT KNOWS
channel.exchange_declare(exchange = 'logs', exchange_type = 'fanout')


#MAKING A NEW QUEUE WITH A RANDOM NAME
#AFTER THE CONSUMER CONNECTION IS CLOSED, QUEUE WILL BE DELETED BY PARAMETER exclusive
result = channel.queue_declare(queue = '', exclusive = True)
queue_name = result.method.queue


#BINDING EXCHANGES AND QUEUE
#'result.method.queue' STORES THE NAME OF RANDOM NAMED QUEUE
channel.queue_bind(exchange = 'logs',
                   queue = queue_name)

channel.basic_consume(queue = queue_name,
                      on_message_callback = callback)

channel.start_consuming()