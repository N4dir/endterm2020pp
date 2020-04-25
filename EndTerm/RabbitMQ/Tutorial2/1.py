#WORK QUEUES   
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'task_queue', durable = True)
#MAKING BASIC CONNECTIONS
#PARAMETER 'DURABLE' SAVES ALL MESSAGES ON QUEUE


#MESSAGE WHICH WILL CONTAIN ALL THE STUFF WHICH IS WRITTEN AFTER '1.py' IN TERMINAL
message = ' '.join(sys.argv[1:]) or "Hello World!"

#DELIVERING MESSAGE TO QUEUE
channel.basic_publish(exchange = '',
                      routing_key = 'task_queue',
                      body = message,
                      properties = pika.BasicProperties(
                          #TO MAKE SURE THAT OUR QUEUE WILL NOT LOSE MESSAGES
                          #EVEN IF RABBITMQ RESTARTS
                          delivery_mode = 2
                      ))

print(" [x] Sent %r" % message)

#CLOSING THE CHANNEL
channel.close()
