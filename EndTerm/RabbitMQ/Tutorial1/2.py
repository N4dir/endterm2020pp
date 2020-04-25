import pika

#FUNCTION WILL PRINT TO SCREEN THAT MESSAGE IS RECEIVED
def callback(ch, method, properties, body):
    print("[x] received %r" % body)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'example1')
#MAKING CONNECTION WITH LOCAL HOST AND QUEUE SAME AS PREVIOSLY

#FUNCTION WHICH SHOULD RECEIVE MESSAGES FROM OUR QUEUE
channel.basic_consume(queue = 'example1', auto_ack = True, on_message_callback = callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

#STARTING CONSUMING
channel.start_consuming()