from contextlib import contextmanager
from termiformer.layout import FormLayout
from termiformer.present import present

@contextmanager
def form(data):
    layout = FormLayout()
    try:
        yield layout
    finally:
        present(layout, data)
