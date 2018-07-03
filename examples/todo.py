from gzuro import Grid, TextInput, Text, Button

root = Grid(cols=1)
text_input = TextInput()
root.append(text_input)


@text_input.on_submit
def add_element():
    grid = Grid(cols=2)
    grid.append(Text(text_input.content))
    button = Button(text='x')
    grid.append(button)
    button.on_click(grid.delete)
    text_input.content = ''
    root.append(grid)

root.run()
