import unittest
from moschitta_serialization.msgpack_serializer import MsgPackSerializer

class TestMsgPackSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = MsgPackSerializer()

    def test_serialize(self):
        # Test serialization of a dictionary
        data = {'name': 'John', 'age': 30}
        expected_msgpack = b'\x82\xa4name\xa4John\xa3age\x1e'
        self.assertEqual(self.serializer.serialize(data), expected_msgpack)

        # Test serialization of a list
        data = [1, 2, 3]
        expected_msgpack = b'\x93\x01\x02\x03'
        self.assertEqual(self.serializer.serialize(data), expected_msgpack)

    def test_deserialize(self):
        # Test deserialization of a MessagePack binary
        msgpack_binary = b'\x82\xa4name\xa4John\xa3age\x1e'
        expected_data = {'name': 'John', 'age': 30}
        self.assertEqual(self.serializer.deserialize(msgpack_binary), expected_data)

        # Test deserialization of a MessagePack binary representing a list
        msgpack_binary = b'\x93\x01\x02\x03'
        expected_data = [1, 2, 3]
        self.assertEqual(self.serializer.deserialize(msgpack_binary), expected_data)

if __name__ == '__main__':
    unittest.main()
