from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.textinput import TextInput as TInput
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.image import Image as _Image

def _args_converter(index, item):
    return {
        'text': item
    }


class Image:
    def __init__(self, path):
        self._image = _Image(source=path)

    def attach_to(self, grid):
        grid.add_widget(self._image)


class Grid:
    def __init__(self, **kwargs):
        self._grid = GridLayout(**kwargs)

    def append(self, element):
        element.attach_to(self._grid)

    def attach_to(self, grid):
        grid.add_widget(self._grid)

    def run(self):
        class _MyApp(App):
            def build(_self):
                return self._grid

        _MyApp().run()


class Text:
    def __init__(self, content=None):
        self._label = Label(text=content)

    @property
    def content(self):
        return self._label.text

    @content.setter
    def content(self, value):
        self._label.text = value

    def attach_to(self, grid):
        grid.add_widget(self._label)

    def run(self):
        class _MyApp(App):
            def build(self):
                return self._label

        _MyApp().run()


class TextInput:
    def __init__(self):
        self._callbacks = []

        class _TextInput(TInput):
            def on_text(_self, item, value):
                for callback in self._callbacks:
                    callback()

        self._txtinput = _TextInput()

    @property
    def content(self):
        return self._txtinput.text

    @content.setter
    def content(self, value):
        self._txtinput.text = value

    def on_change(self, f):
        self._callbacks.append(f)
        return f

    def attach_to(self, grid):
        grid.add_widget(self._txtinput)

    def run(self):
        class _MyApp(App):
            def build(self):
                return self._txtinput

        _MyApp().run()


class SelectList:
    def __init__(self, *, choices, default):
        self._selection_callbacks = []

        class _ListAdapter(ListAdapter):
            selected = StringProperty('')

            def on_selection(_self, item, value):
                if value:
                    _self.selected = value[0].text
                    for callback in self._selection_callbacks:
                        callback()

            def select(self, choice):
                v = self.get_view(self.data.index(choice))
                if v is not None:
                    self.handle_selection(v)

        self._adapter = _ListAdapter(
            data=choices,
            args_converter=_args_converter,
            cls=ListItemButton,
            selection_mode='single',
            allow_empty_selection=False,
        )
        self._listview = ListView(adapter=self._adapter)
        self._adapter.select(default)

    @property
    def choices(self):
        return self._adapter.data

    @choices.setter
    def choices(self, value):
        self._adapter.data = value

    @property
    def selected(self):
        return self._adapter.selected

    @selected.setter
    def selected(self, value):
        return self._adapter.select(value)

    def on_selection(self, f):
        self._selection_callbacks.append(f)
        return f

    def attach_to(self, grid):
        grid.add_widget(self._listview)

    def run(self):
        class _MyApp(App):
            def build(self):
                return self._listview

        _MyApp().run()
