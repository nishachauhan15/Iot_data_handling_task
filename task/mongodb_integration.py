from pymongo import MongoClient
import json
import logging

# Configure logging
logging.basicConfig(filename='mongodb_integration.log', level=logging.ERROR)

# MongoDB connection parameters
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DATABASE = 'iot_data'
MONGODB_COLLECTION = 'processed_messages'

def connect_to_mongodb():
    try:
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client[MONGODB_DATABASE]
        collection = db[MONGODB_COLLECTION]
        return collection
    except Exception as e:
        logging.error("Error connecting to MongoDB: %s", e)

def insert_into_mongodb(message):
    try:
        collection = connect_to_mongodb()
        if collection:
            # Insert message into MongoDB
            result = collection.insert_one(json.loads(message))
            logging.info("Message inserted into MongoDB with ID: %s", result.inserted_id)
    except Exception as e:
        logging.error("Error inserting message into MongoDB: %s", e)

# Example usage
if __name__ == "__main__":
    mqtt_message = '{"sensor_id": 1, "value": 25.5}'  # Example MQTT message
    insert_into_mongodb(mqtt_message)
