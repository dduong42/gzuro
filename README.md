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
