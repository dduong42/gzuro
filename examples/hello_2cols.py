from gzuro import Grid, Text

root = Grid(cols=2)
hello = Text('Hello')
world = Text('World!')
root.append(hello)
root.append(world)
root.run()
