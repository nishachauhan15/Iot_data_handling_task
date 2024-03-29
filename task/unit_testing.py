import unittest
import sys
sys.path.append('/path/to/your/module_directory')
from message_proccessing import process_message
from mongodb_integration import insert_into_mongodb

class TestMessageProcessing(unittest.TestCase):
    def test_process_message_valid(self):
        mqtt_message = '{"sensor_id": 1, "value": 25.5}'
        result = process_message(mqtt_message)
        self.assertTrue(result)

    def test_process_message_invalid(self):
        mqtt_message = '{"sensor_id": "invalid", "value": "invalid"}'
        result = process_message(mqtt_message)
        self.assertFalse(result)

class TestDatabaseOperations(unittest.TestCase):
    def test_insert_into_mongodb(self):
        message = {"sensor_id": 1, "value": 25.5}
        result = insert_into_mongodb(message)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
