import os
import sys

import pika


def main():
    # prepare a connection
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    # create channel
    channel = connection.channel()

    # define a queue name
    queue = "hello"

    # declare a queue
    channel.queue_declare(queue=queue)

    # define callback function for received message
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # consume message
    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
