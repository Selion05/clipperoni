from pathlib import Path
import json
import clipperoni.config


class Store(object):
    _data: []
    _location: Path

    def __init__(self):
        directory = clipperoni.config.directory
        if not directory.exists():
            directory.mkdir()
        self._location = directory / "data.json"
        if self._location.exists():
            with open(self._location, "r") as f:
                self._data = json.load(f)
        else:
            self._data = {"items": {}}

    def save(self, name: str, label: str, clipboard: str):
        self._data["items"][name] = {"clipboard": clipboard, "label": label}

    def get_by_name(self, name: str) -> dict:
        return self._data["items"][name]

    def get_by_label(self, label: str) -> dict:
        for name, item in self._data["items"].items():
            if item["label"] == label:
                return item
        raise ValueError(f'Item with Label "{label}" does not exist.')

    def all(self) -> dict:
        return self._data["items"]

    def labels(self) -> []:
        return [i["label"] for k, i in self._data["items"].items()]

    def persist_to_file(self):
        with open(self._location, "w") as f:
            json.dump(self._data, f)
