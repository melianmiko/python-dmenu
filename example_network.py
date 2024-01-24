from dmenu import DMenuContent
from utils.nm_tools import get_connections, connect, disconnect


def _get_device_item(device):
    title = f"{device['name']} ({device['type']})"
    if device["active"]:
        title = "[ONLINE]" + title

    def func():
        if device["active"]:
            disconnect(device["uuid"])
        else:
            connect(device["uuid"])

    return title, func


def show(extra_args=None):
    devices = get_connections()
    items = []
    for device in devices:
        if device["type"] == "bridge":
            continue
        items.append(_get_device_item(device))
    DMenuContent(items=items, extra_args=extra_args).run()


if __name__ == "__main__":
    show()
