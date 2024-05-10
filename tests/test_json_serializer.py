import unittest

from moschitta_serialization.json_serializer import JSONSerializer


class TestJSONSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = JSONSerializer()

    def test_serialize(self):
        # Test serialization of a dictionary
        data = {"name": "John", "age": 30}
        expected_json = '{"name": "John", "age": 30}'
        self.assertEqual(self.serializer.serialize(data), expected_json)

        # Test serialization of a list
        data = [1, 2, 3]
        expected_json = "[1, 2, 3]"
        self.assertEqual(self.serializer.serialize(data), expected_json)

    def test_deserialize(self):
        # Test deserialization of a JSON string
        json_string = '{"name": "John", "age": 30}'
        expected_data = {"name": "John", "age": 30}
        self.assertEqual(self.serializer.deserialize(json_string), expected_data)

        # Test deserialization of a JSON string representing a list
        json_string = "[1, 2, 3]"
        expected_data = [1, 2, 3]
        self.assertEqual(self.serializer.deserialize(json_string), expected_data)


if __name__ == "__main__":
    unittest.main()
