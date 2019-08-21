from termpixels import Color
from termiformer.layout import item_value

def render_label(*, screen, data, item, focused):
    color = Color.rgb(1,1,1) if focused else Color.rgb(0.5,0.5,0.5)
    screen.print(item["label"], fg=color)

def render_text(*, screen, data, item, focused):
    color = Color.rgb(1,1,1) if focused else Color.rgb(0.5,0.5,0.5)
    screen.print(item["label"], fg=color)
    screen.print("\n", x=0)
    screen.print(item_value(data, item), fg=color)
    if focused:
        screen.show_cursor = True
        screen.cursor_pos = screen.print_pos

renderers = {
    "label": render_label,
    "text": render_text
}

def render_item(*args, item, **kwargs):
    item_type = item["type"]
    if item_type in renderers:
        renderers[item_type](*args, item=item, **kwargs)
    else:
        raise Exception("No renderer for item type: '{}'".format(item_type))
