#HELLO WORLD

#LIBRARY WHICH CAN WORK WITH RABBITMQ
import pika

#ESTABLISHING CONNECTION WITH OUR LOCALHOST
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#WE'RE CONNECTED NOW, TO A BROKER ON THE LOCAL MACHINE - HENCE THE LOCALHOST

#MAKING CONNECTION WITH THE QUEUE, IF IT DOES NOT EXIST, WE CREATING IT
channel.queue_declare(queue = 'example1')

#SENDING A MESSAGE 'Hello World!' TO OUR NEW QUEUE THROW THE DEFAULT EXCHANGE
channel.basic_publish(exchange = '', routing_key = 'example1',body = 'Hello World!')

print('sent')

#CLOSING CONNECTION TO PREVENT ERROR
channel.close()