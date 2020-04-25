#PUBLISH/SUBSCRIBE
import pika 
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#ESTABLISHING CONNECTION

#FANOUT TYPE EXCHANGE BROADCAST ALL THE MESSAGES IT RECEIVES
#TO ALL THE QUEUES IT KNOWS
channel.exchange_declare(exchange = 'logs', exchange_type = 'fanout')


#MESSAGE WHICH WILL CONTAIN ALL THE STUFF WHICH IS WRITTEN AFTER '1.py' IN TERMINAL
message = ' '.join(sys.argv[1:]) or "Hello World!"


#PUBLISHING TO EXCHANGE
channel.basic_publish(exchange = 'logs', routing_key = '', body = message)

print('[x] sent%r' % message)
connection.close()




