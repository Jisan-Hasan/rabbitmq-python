import pika

# prepare a connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# create channel
channel = connection.channel()

# define a queue name
queue = "hello"

# declare a queue
channel.queue_declare(queue=queue)

# publish a message
channel.basic_publish(exchange="", routing_key=queue, body="Hello World")

print(" [x] Sent 'Hello World!'")

# close connection
connection.close()
