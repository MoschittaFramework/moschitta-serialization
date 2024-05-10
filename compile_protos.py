import os
import subprocess

proto_dir = 'proto'
for filename in os.listdir(proto_dir):
    if filename.endswith('.proto'):
        subprocess.run(['protoc', '--python_out=.', os.path.join(proto_dir, filename)])
