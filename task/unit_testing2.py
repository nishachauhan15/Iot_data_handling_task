import unittest
from mqtt_rabbitmq_integration.consumer import start_consuming
from mongodb_integration import insert_into_mongodb

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        # Start consuming MQTT messages
        start_consuming()
        
        # Simulate MQTT message processing and database insertion
        mqtt_message = '{"sensor_id": 1, "value": 25.5}'
        insert_into_mongodb(mqtt_message)

        # Check if message is inserted into MongoDB
        # Add assertions here to validate MongoDB insertion

if __name__ == '__main__':
    unittest.main()
