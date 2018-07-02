from gzuro import Grid, Text, Button

root = Grid(cols=2)
button = Button(text='Click me')
text = Text('Not clicked')


@button.on_click
def change_text():
    text.content = 'clicked'


root.append(button)
root.append(text)
root.run()
