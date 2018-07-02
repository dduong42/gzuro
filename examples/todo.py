from gzuro import Button, Grid, Text, TextInput


def create_item(text):
    grid = Grid(cols=2)
    text = Text(text)
    btn = Button(text='x')
    btn.on_click(grid.delete)
    grid.append(text)
    grid.append(btn)

    return grid


if __name__ == '__main__':
    root = Grid(cols=1)
    txt_input = TextInput()

    @txt_input.on_submit
    def submit_callback():
        item = create_item(txt_input.content)
        txt_input.content = ''
        root.append(item)

    root.append(txt_input)
    root.run()
