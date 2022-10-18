
import json
from typing import Dict

class Metadata(object):
    def __init__(self):
        try:
            with open('metadata.json') as f:
                self.data = json.load(f)
        except:
            raise Exception("File not found or not data found")
        
    def get_metadata(self) -> Dict:
        return self.data