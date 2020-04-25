import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#NEW EXCHANGE WHICH WILL ACCEPT LIST OF WORDS, DELIMITED BY DOTS
channel.exchange_declare(exchange = 'topic_logs', exchange_type = 'topic')

#IF WE WILL NOT TYPE ANYTHING AFTER THE NAME OF PROJECT
#IT WILL AUTOMATICALLY FILLED
routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange = 'topic_logs',routing_key = routing_key, body = message)

print("[x] sent %r:%r" %(routing_key, message))

connection.close()