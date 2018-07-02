from gzuro import Grid, Text, TextInput

root = Grid(cols=2)
text_input = TextInput()
text = Text('Some text')


@text_input.on_change
def change_text():
    text.content = text_input.content.upper()


root.append(text_input)
root.append(text)
root.run()
