import unittest
from moschitta_serialization.protobuf_serializer import ProtobufSerializer
from proto.person_pb2 import Person
from proto.vehicle_pb2 import Vehicle
from proto.book_pb2 import Book
from proto.movie_pb2 import Movie
from proto.product_pb2 import Product
from proto.employee_pb2 import Employee

class TestProtobufSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = ProtobufSerializer()

    def test_serialize_deserialize(self):
        test_cases = [
            (Person(name="John", age=30), Person),
            (Vehicle(make="Toyota", model="Corolla", year=2020), Vehicle),
            (Book(title="1984", author="George Orwell", publication_year=1949), Book),
            (Movie(title="The Matrix", director="The Wachowskis", release_year=1999), Movie),
            (Product(name="Laptop", category="Electronics", price=999.99), Product),
            (Employee(first_name="John", last_name="Doe", position="Software Engineer", employee_id=1234), Employee),
        ]

        for message, message_type in test_cases:
            # Serialize the message
            serialized_message = self.serializer.serialize(message)

            # Check that the serialized data is a string
            self.assertIsInstance(serialized_message, str)

            # Deserialize the serialized message
            deserialized_message = self.serializer.deserialize(serialized_message, message_type)

            # Check that the deserialized data is a message of the correct type
            self.assertIsInstance(deserialized_message, message_type)

            # Check that the deserialized message matches the original message
            self.assertEqual(deserialized_message, message)

if __name__ == "__main__":
    unittest.main()
