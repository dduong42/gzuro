# gzuro
A simple Graphical User Interface framework

## Who is it for ?

I'm writing this framework for python beginners that don't understand classes yet. Don't use it on production.

## Install

```
pip install Cython==0.28.2
pip install https://github.com/kivy/kivy/archive/master.zip
pip install git+https://github.com/dduong42/gzuro.git
```

## Tutorial

### A simple Hello World

Let's start a simple Hello World. First, we need to import a `Grid` and a `Text`.

```python
from gzuro import Grid, Text
```

We want a `Grid` with 1 column and we're going to put a `Text` in that column.

```python
root = Grid(cols=1)
hello = Text('Hello World!')
root.append(hello)
```

Then we need to run the program from the `root`.

```python
root.run()
```

Let's put all this code in a file called `hello.py`

```python
from gzuro import Grid, Text

root = Grid(cols=1)
hello = Text('Hello World!')
root.append(hello)
root.run()
```

Now if you run `hello.py`, you should see `Hello World!`.

```
python3 hello.py
```

### Playing with the grid

Now, let's say we want to put `Hello` and `World!` in two different columns. We can do this `(hello_2cols.py)`:

```python
from gzuro import Grid, Text

root = Grid(cols=2)
hello = Text('Hello')
world = Text('World!')
root.append(hello)
root.append(world)
root.run()
```

We can also put in 2 different rows (`hello_2rows.py`):

```python
from gzuro import Grid, Text

root = Grid(rows=2)
hello = Text('Hello')
world = Text('World!')
root.append(hello)
root.append(world)
root.run()
```

### Questions about the grid

What happens when we do this?

```python
from gzuro import Grid, Text

root = Grid(rows=1)
root.append(Text('First'))
root.append(Text('Second'))
root.append(Text('Last'))
root.run()
```

What about this?

```python
from gzuro import Grid, Text

root = Grid(cols=1)
root.append(Text('First'))
root.append(Text('Second'))
root.append(Text('Last'))
root.run()
```

### Changing the content of a `Text`

You can change a content of a text like this:

```python
hello = Text('Hello')
hello.content = 'hello'
```

It will be useful when we write some callbacks.

`change_text.py`
```python
from gzuro import Grid, Text

root = Grid(cols=1)
hello = Text('Hello World!')
hello.content = 'hello world :)'
root.append(hello)
root.run()
```

### Our first `Button`

Let's do a 2 cols grid with a button and a text.

```python
from gzuro import Grid, Text, Button

root = Grid(cols=2)
button = Button(text='Click me')
text = Text('Not clicked')
root.append(button)
root.append(text)
root.run()
```

Now let's change the text when we click on the `Button`. To do that, we just need to write a callback.

```python
@button.on_clicked
def change_text():
    text.content = 'clicked'
```

Here is the whole code (`simple_btn.py`)

```python
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
```

### Removing an element

You can remove an element by using the `delete` method (`delete_example.py`).

```python
from gzuro import Grid, Text

root = Grid(cols=1)
hello = Text('Hello')
world = Text('World!')
root.append(hello)
root.append(world)
world.delete()
root.run()
```

Note that we're deleting the element after it's attached. It doesn't make sense to delete an element if it's not attached (it's not displayed).

### TextInput

Let's start with a grid with a `Text` and a `TextInput`.

```python
from gzuro import Grid, Text, TextInput

root = Grid(cols=2)
text_input = TextInput()
text = Text('Some text')
root.append(text_input)
root.append(text)
root.run()
```

Let's change the text when we submit something from the `TextInput`. Same thing as before, we will write a callback (`on_submit_example.py`).

```python
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
```

Now when we press `ENTER`, the text should change.

We can also do an action each time the content from the `TextInput` is changed (`on_change_example.py`):

```python
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
```

### A little TODO app

What do we need ? Well, first we need a `TextInput` to add our elements.

```python
from gzuro import Grid, TextInput

root = Grid(cols=1)
text_input = TextInput()
root.append(text_input)
root.run()
```

Now what happens when we submit? We want to add the element in our list.

```python
from gzuro import Grid, TextInput, Text

root = Grid(cols=1)
text_input = TextInput()
root.append(text_input)


@text_input.on_submit
def add_element():
    root.append(Text(text_input.content))
    text_input.content = ''

root.run()
```

Now let's add also a button to remove the element from the list (`todo.py`).

```python
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
```

### Images

Let's say you want to display an image. No problem, you can do it like this (`image.py`):

```python
import pathlib
from gzuro import Grid, Image

current_dir = pathlib.Path(__file__).parent
image_path = current_dir / 'shiba.jpg'
root = Grid(cols=1)
root.append(Image(str(image_path)))
root.run()
```

### SelectList

Let's say you have a few elements from a list and you want to select one from them. You can do that with a `SelectList`

```python
from gzuro import Grid, SelectList

root = Grid(cols=1)
select_list = SelectList(choices=['blue', 'black', 'grey'], default='blue')
root.append(select_list)
root.run()
```

Let's display the selected choice in a `Text`.

```python
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
```
