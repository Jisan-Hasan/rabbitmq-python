import sys

import pika

# prepare a connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# create channel
channel = connection.channel()

# define a queue name
queue = "task_queue"

# declare a queue
channel.queue_declare(queue=queue, durable=True)

# get message from terminal
message = " ".join(sys.argv[1:]) or "Hello World!"

# publish a message
channel.basic_publish(
    exchange="",
    routing_key=queue,
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
    ),
)

print(" [x] Sent 'Hello World!'")

# close connection
connection.close()
