import unittest
from moschitta_serialization.yaml_serializer import YAMLSerializer

class TestYAMLSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = YAMLSerializer()

    def test_serialize(self):
        # Test serialization of a dictionary
        data = {'name': 'John', 'age': 30}
        expected_yaml = "age: 30\nname: John\n"
        self.assertEqual(self.serializer.serialize(data), expected_yaml)

        # Test serialization of a list
        data = [1, 2, 3]
        expected_yaml = "- 1\n- 2\n- 3\n"
        self.assertEqual(self.serializer.serialize(data), expected_yaml)

    def test_deserialize(self):
        # Test deserialization of a YAML string
        yaml_string = "age: 30\nname: John\n"
        expected_data = {'name': 'John', 'age': 30}
        self.assertEqual(self.serializer.deserialize(yaml_string), expected_data)

        # Test deserialization of a YAML string representing a list
        yaml_string = "- 1\n- 2\n- 3\n"
        expected_data = [1, 2, 3]
        self.assertEqual(self.serializer.deserialize(yaml_string), expected_data)

if __name__ == '__main__':
    unittest.main()
