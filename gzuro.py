from kivy.adapters.listadapter import ListAdapter
from kivy.uix.button import Button as _Button
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image as _Image
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.textinput import TextInput as TInput


def _args_converter(index, item):
    return {
        'text': item
    }


class Element:
    def attach_to(self, grid):
        self._grid = grid
        grid.add_widget(self._element)

    def delete(self):
        self._grid.remove_widget(self._element)

    def run(self):
        class _MyApp(App):
            def build(_self):
                return self._element

        _MyApp().run()


class Button(Element):
    def __init__(self, text, on_click):
        self._element = _Button(text=text)
        self._element.bind(on_press=lambda instance: on_click())


class Image(Element):
    def __init__(self, path):
        self._element = _Image(source=path)


class Grid(Element):
    def __init__(self, **kwargs):
        self._element = GridLayout(**kwargs)

    def append(self, element):
        element.attach_to(self._element)


class Text(Element):
    def __init__(self, content=None):
        self._element = Label(text=content)

    @property
    def content(self):
        return self._element.text

    @content.setter
    def content(self, value):
        self._element.text = value


class TextInput(Element):
    def __init__(self):
        self._text_callbacks = []
        self._submit_callbacks = []

        class _TextInput(TInput):
            def on_text(_self, item, value):
                for callback in self._text_callbacks:
                    callback()

            def on_text_validate(_self):
                for callback in self._submit_callbacks:
                    callback()

        self._element = _TextInput(multiline=False)

    @property
    def content(self):
        return self._element.text

    @content.setter
    def content(self, value):
        self._element.text = value

    def on_change(self, f):
        self._text_callbacks.append(f)
        return f

    def on_submit(self, f):
        self._submit_callbacks.append(f)
        return f


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
        self._element = ListView(adapter=self._adapter)
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
