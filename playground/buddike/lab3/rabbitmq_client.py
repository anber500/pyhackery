import pika


def publish_to_rabbitmq(message, queue):
    print("Trying to connect to RabbitMQ instance")

    try:
        with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
            print("Connected to local RabbitMQ instance")
            channel = connection.channel()

            try:
                channel.queue_declare(queue=queue)
                print("queue.....created")

                try:
                    print("Trying to publishing simple message...")
                    channel.basic_publish(exchange='', routing_key=queue, body=message)
                    print("Test message published")
                except:
                    print("Unable to publish the message to queue")
            except:
                print("Unable to create queue in local rabbit instance")
    except:
        print("Unable to connect to local RabbitMQ instance.")



