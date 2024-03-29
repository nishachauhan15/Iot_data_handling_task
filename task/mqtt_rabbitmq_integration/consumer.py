import pika

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_EXCHANGE = 'mqtt_exchange'

# MQTT topics to subscribe to
MQTT_TOPICS = ['topic1', 'topic2']  # Add your MQTT topics here

def callback(ch, method, properties, body):
    print("Received MQTT message:", body)

def connect_to_rabbitmq():
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                           port=RABBITMQ_PORT,
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declare exchange for MQTT messages
    channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='topic')

    return channel

def subscribe_to_mqtt_topics(channel):
    for topic in MQTT_TOPICS:
        # Declare queue for each MQTT topic
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        # Bind queue to exchange with the specified topic
        channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=queue_name, routing_key=topic)

        # Start consuming messages from the queue
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print("Subscribed to MQTT topics:", MQTT_TOPICS)

def start_consuming():
    channel = connect_to_rabbitmq()
    subscribe_to_mqtt_topics(channel)
    print("Waiting for MQTT messages...")
    channel.start_consuming()

if __name__ == "__main__":
    start_consuming()
