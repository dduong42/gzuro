from gzuro import Grid, Text

root = Grid(cols=1)
hello = Text('Hello World!')
hello.content = 'hello world :)'
root.append(hello)
root.run()
