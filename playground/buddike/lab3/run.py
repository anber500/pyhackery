import rabbitmq_client

# Publishing to designated message queue
rabbitmq_client.publish_to_rabbitmq("This is a test mesage", "labthreequeue")