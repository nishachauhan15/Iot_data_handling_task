import json
import logging


# Configure logging
logging.basicConfig(filename='message_processing.log', level=logging.ERROR)

def process_message(message):
    try:
        # Parse JSON message
        message_data = json.loads(message)
        
        # Validate message format
        if "sensor_id" in message_data and "value" in message_data:
            sensor_id = message_data["sensor_id"]
            value = message_data["value"]
            
            # Transform message content if needed
            # For example, convert sensor value to appropriate units
            
            # Example processing: Print sensor data
            print(f"Received message - Sensor ID: {sensor_id}, Value: {value}")
            
            # Additional processing logic here
            
            return True  # Message processed successfully
        else:
            logging.error("Invalid message format: %s", message)
            return False  # Message format is invalid
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON: %s", e)
        return False  # JSON decoding error
    except Exception as e:
        logging.error("Error processing message: %s", e)
        return False  # Other error during processing

# Example usage
if __name__ == "__main__":
    mqtt_message = '{"sensor_id": 1, "value": 25.5}'  # Example MQTT message
    process_message(mqtt_message)
