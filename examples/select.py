from gzuro import Grid, SelectList, Text

root = Grid(cols=2)
select_list = SelectList(choices=['blue', 'black', 'grey'], default='blue')
text = Text('Selected: blue')
root.append(select_list)
root.append(text)

@select_list.on_selection
def change_text():
    text.content = f'Selected: {select_list.selected}'
root.run()
