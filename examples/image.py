import pathlib
from gzuro import Grid, Image

current_dir = pathlib.Path(__file__).parent
image_path = current_dir / 'shiba.jpg'
root = Grid(cols=1)
root.append(Image(str(image_path)))
root.run()
