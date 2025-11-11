from dataclasses import dataclass
import json

@dataclass
class Key:
    data: dict
    def to_json(self):
        return json.dumps(self.data)
    @staticmethod
    def from_json(s: str):
        return Key(json.loads(s))
