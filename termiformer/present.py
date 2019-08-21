from termpixels import App, Color
from termiformer.layout import item_focusable, item_value
from termiformer.render import render_item

class TermiformerApp(App):
    def on_start(self, layout, data):
        self.layout = layout
        self.data = data
        self.focused_index = next((i for i, item in enumerate(layout.items) if item_focusable(item)), 0)
        self.dirty = False
        self.render()
    
    def on_key(self, k):
        if k == "up" or k == "backtab":
            self.focused_index = max(self.focused_index - 1, 0)
        elif k == "down" or k == "tab":
            self.focused_index = min(self.focused_index + 1, len(self.layout.items) - 1)
        elif k == "\n":
            self.stop()
            return
        else:
            focused_item = self.layout.items[self.focused_index]
            if focused_item["type"] == "text":
                value = item_value(self.data, focused_item)
                if k == "\b":
                    self.data[focused_item["name"]] = value[:-1]
                elif k.char:
                    self.data[focused_item["name"]] = value + k.char
        self.dirty = True
    
    def on_frame(self):
        if self.dirty:
            self.dirty = False
            self.render()

    def render(self):
        self.screen.clear()
        self.screen.print_pos = (0, 0)
        self.screen.show_cursor = False

        for i, item in enumerate(self.layout.items):
            focused = i == self.focused_index
            render_item(
                screen=self.screen,
                data=self.data,
                item=item,
                focused=focused
            )

            self.screen.print("\n\n", x=0)
        self.screen.update()

def present(layout, data):
    TermiformerApp().start(layout, data)
