import pyperclip
import re
import argparse
import clipperoni.dmenu as dmenu
from clipperoni.store import Store


class CLI(object):
    description = "A simple clipboard manager"
    usage = f"""clipperoni <command> [<args>]

Available commands are:
    save    Saves current clipboard
    load    Loads saved clipboard
"""
    args: []
    store: Store

    def __init__(self, argv, store):
        parser = argparse.ArgumentParser(description=self.description, usage=self.usage)
        self.store = store
        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(argv[1:2])
        if not hasattr(self, args.command):
            print("Unknown command")
            parser.print_help()
            exit(1)
        self.args = argv[2:]
        getattr(self, args.command)()

    def save(self):

        parser = argparse.ArgumentParser(description="Save clipboard")

        parser.add_argument(
            "name", help="Optional - Name to store clipboard", nargs="?"
        )

        args = parser.parse_args(self.args)

        name = None
        if args.name:
            name = args.label

        while not name:
            name = dmenu.dmenu(["exit"], p="Enter Name")

        if name == "exit":
            return

        clipboard = pyperclip.paste()
        short = re.compile(r"\s+").sub(" ", clipboard)[:30]

        label = f"{name} - {short}"

        self.store.save(name, label, clipboard)

    def load(self):
        parser = argparse.ArgumentParser(description="Load a saved clipboard")

        parser.add_argument("name", help="Copy clipboard by name", nargs="?")

        args = parser.parse_args(self.args)

        if args.name:
            clipboard = self.store.get_by_name(args.name)
        else:
            label = dmenu.select(["exit"] + self.store.labels())
            if label == "exit" or not label:
                return

            clipboard = self.store.get_by_label(label)["clipboard"]

        pyperclip.copy(clipboard)


def main(args):
    store = Store()
    try:
        CLI(args, store)
    finally:
        store.persist_to_file()
