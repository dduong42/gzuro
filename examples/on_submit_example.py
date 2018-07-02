from gzuro import Grid, Text, TextInput

root = Grid(cols=2)
text_input = TextInput()
text = Text('Some text')


@text_input.on_submit
def change_text():
    text.content = text_input.content
    # Flush the TextInput
    text_input.content = ''


root.append(text_input)
root.append(text)
root.run()
