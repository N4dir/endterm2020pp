import pika
import time

def callback(ch, method, properties, body):
    print('[x] received %r' % body)

    #WAITS [COUNT OF DOTS IN THE MESSAGE] SECONDS
    time.sleep(body.count(b'.'))

    print('[x] done')
    #IF AND ONLY IF MESSAGE IS DONE, RABBITMQ CAN DELETE IT FROM THE QUEUE
    ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = 'task_queue', durable = True)
#DECLARING QUEUE, CONNECTING TO LOCAL HOST AND QUEUE, MAKING QUEUE DURABLE

#CONSUMING FUNCTION
channel.basic_consume(queue = 'task_queue', on_message_callback = callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

#RABBITMQ WILL NOT GIVE THE MESSAGE TO CONSUMER IF IT IS BUSY
channel.basic_qos(prefetch_count = 1)

#STARTING CONSUMING
channel.start_consuming()

