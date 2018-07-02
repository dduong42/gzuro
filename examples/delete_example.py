from gzuro import Grid, Text

root = Grid(cols=1)
hello = Text('Hello')
world = Text('World!')
root.append(hello)
root.append(world)
world.delete()
root.run()
