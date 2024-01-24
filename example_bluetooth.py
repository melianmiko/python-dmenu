from dmenu import DMenuContent
from utils.bt_tools import get_devices, connect, disconnect


def _get_device_item(device):
    title = f"{device['name']} ({device['uuid']})"
    if device["active"]:
        title = "[ONLINE]" + title

    def func():
        if device["active"]:
            disconnect(device["dbus_path"])
        else:
            connect(device["dbus_path"])

    return title, func


def show(extra_args=None):
    devices = get_devices()
    items = []
    for device in devices:
        items.append(_get_device_item(device))
    DMenuContent(items=items, extra_args=extra_args).run()


if __name__ == "__main__":
    show()
