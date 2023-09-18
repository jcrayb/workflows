import json

class ContainerHandler():
    def __init__(self) -> None:
        json_data = json.load(open('config/container_handler.json', 'r'))
        self.protocol = json_data['protocol']
        self.host = json_data['host']
        self.port = json_data['port']

def verify_user(key):
    if key == open('config/key', 'r').read():
        return True
    return False