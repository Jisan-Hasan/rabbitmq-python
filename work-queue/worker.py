import os
import sys
import time

import pika


def main():
    # prepare a connection
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    # create channel
    channel = connection.channel()

    # define a queue name
    queue = "task_queue"

    # declare a queue
    channel.queue_declare(queue=queue, durable=True)

    # define callback function for received message
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        # wait count(.) seconds
        time.sleep(body.count(b"."))
        print(f" [x] Done")
        # when done send ack
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # one task at a time
    channel.basic_qos(prefetch_count=1)

    # consume message
    channel.basic_consume(queue=queue, on_message_callback=callback)

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
