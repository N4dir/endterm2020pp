#PUBLISH/SUBSCRIBE
import pika 
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#ESTABLISHING CONNECTION

#DIRECT TYPE EXCHANGE BROADCAST MESSAGES TO QUEUES WITH THE SAME ROUTING_KEY
channel.exchange_declare(exchange = 'direct_logs', exchange_type = 'direct')

#IF INFO IS MAJOR WE WILL ADD IT
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

#MESSAGE WHICH WILL CONTAIN ALL THE STUFF WHICH IS WRITTEN AFTER '1.py' IN TERMINAL
message = ' '.join(sys.argv[2:]) or "Hello World!"


#PUBLISHING TO EXCHANGE,
channel.basic_publish(exchange = 'direct_logs', 
                      routing_key = severity, body = message)

print('[x] sent%r:%r' % (severity, message))
connection.close()




