# DMenu generator for python

This repository provides bindings for dmenu-compatable launchers in python.
You can use it to create custm python-based menus inside `dmenu`/`rofi`/`tofi`
or any other compatable launcher.

## Configuration for launcher

For `dmenu`, default configuration is valid. For `tofi`, you must only change `dmenu.executable_path` to `/bin/tofi`.

For `rofi`, you must set `dmenu.executable_path` variable to `/bin/rofi` and also add `dmenu.extra_args = ["-dmenu"]`.

## Example: build menu with decorated functions

```python
import dmenu

# Use `tofi` dmenu
dmenu.executable_path = "/bin/tofi"

# Create new menu
menu = dmenu.DMenuContent()

# Fill it with decorators
@menu.item("Item 1")
def item_1():
    print("One!")


@menu.item("Item 2")
def item_1():
    print("Two!")

# Run!
menu.run()
```

## Example: create items in main loop

```python
import dmenu

# Use `tofi` dmenu
dmenu.executable_path = "/bin/tofi"

# Create new menu
menu = dmenu.DMenuContent()


# Callback function
def callback(item):
    print("Item", item)


# Build menu items
for i in range(0, 10):
    # name, callback, args (optional)
    menu.append(f"Item {i}", callback, [i])

# Run!
menu.run()
```

# More examples...
See `example_*.py` files in this repo.
