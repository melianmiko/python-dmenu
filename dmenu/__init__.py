import subprocess

executable_path = "/bin/dmenu"
extra_args = []


class DMenuContent:
    def __init__(self, items: list[tuple[str, callable]] = None, extra_args: list[str] = None):
        self._items = []
        self._args = [] if extra_args is None else extra_args   # type: list[str]

        if items is not None:
            for name, fnc in items:
                self._items.append((name, fnc, []))

        self.validate_items()

    def item(self, name):
        def _in(fnc):
            self._items.append((name, fnc, []))
            self.validate_items()
            return fnc

        return _in

    def append(self, name, fnc, args=None):
        if args is None:
            args = []
        self._items.append((name, fnc, args))
        self.validate_items()

    def run(self):
        process = subprocess.Popen([executable_path, *extra_args, *self._args],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        data_in = "\n".join([i[0] for i in self._items]).encode("utf8")
        data_out = process.communicate(input=data_in)[0].decode("utf8").split("\n")[0]
        if data_out == "":
            return False

        for name, fnc, args in self._items:
            if name == data_out:
                fnc(*args)
                return True

        return False

    def add_separator(self):
        self._items.append(("---", lambda: print("Ignore")))

    def validate_items(self):
        names = [i[0] for i in self._items]
        seen = []
        for i in names:
            if i == "---":
                continue

            if i not in seen:
                seen.append(i)
            else:
                raise Exception("Duplicate")
