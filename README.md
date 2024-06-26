# Moschitta Serialization Documentation

`moschitta-serialization` is a Python package that provides serializers for converting data to and from various formats, including JSON, MessagePack, YAML, and Protobuf.

## Installation

To install `moschitta-serialization`, you'll need Python 3.7 or higher, as well as Poetry for dependency management and building the package.

1. **Install Poetry**: If you haven't already, install Poetry, a tool for dependency management and building Python packages. You can install it with the following command:

    ```bash
    curl -sSL https://install.python-poetry.org | python -
    ```

2. **Install Protobuf Compiler**: The Protobuf compiler (`protoc`) is required for compiling `.proto` files into Python code. You can install it as follows:

    - On Ubuntu/Debian:

        ```bash
        sudo apt-get install protobuf-compiler
        ```

    - On macOS:

        ```bash
        brew install protobuf
        ```

    - On Windows, download pre-compiled binaries from the [Protocol Buffers GitHub repository](https://github.com/protocolbuffers/protobuf/releases). After downloading and unzipping the archive, add the `bin/` directory to your PATH.

3. **Install the Package**: Navigate to the root directory of the `moschitta-serialization` package and run the following command to install the package and its dependencies:

    ```bash
    poetry install
    ```

## Usage

The `moschitta-serialization` package provides several serializers that you can use in your application. Here's an example of how to use the `JSONSerializer`:

```python
from moschitta_serialization.json_serializer import JSONSerializer

serializer = JSONSerializer()
data = {"name": "John", "age": 30}
serialized_data = serializer.serialize(data)
print(serialized_data)  # '{"name": "John", "age": 30}'
```

You can use the other serializers in a similar way.

## Protobuf Serialization

To use the `ProtobufSerializer`, you'll need to define your Protobuf messages in `.proto` files, compile these files into Python code, and import the generated classes in your application.

1. **Define Protobuf Messages**: Create a `.proto` file in the `proto/` directory and define your Protobuf messages in it.

2. **Compile `.proto` Files**: Run the `compile_protos.py` script to compile the `.proto` files into Python code:

    ```bash
    python compile_protos.py
    ```

3. **Import Message Types**: In your Python code, import the generated classes from the Python files:

    ```python
    from proto.person_pb2 import Person
    ```

You can then use these classes with the `ProtobufSerializer`.

## Testing

The `moschitta-serialization` package includes a suite of tests that you can run with pytest. To run the tests, navigate to the root directory of the package and run the following command:

```bash
poetry run pytest
```

## Contributing

Contributions to the `moschitta-serialization` package are welcome! Please submit a pull request or open an issue on the [GitHub repository](https://github.com/MoschittaFramework/moschitta-serialization).

## License

This project is licensed under the terms of the [MIT License](LICENSE).

