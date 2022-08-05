import PySimpleGUI as sg
import os


class GUI:
    def __init__(self):
        self.layout = [[]]
        self.current_row = 0
        self.window = None

    def set_input_to_layout(self, _key):
        self.layout[self.current_row].append(sg.InputText(key=_key))

    def set_label_to_layout(self, text):
        self.layout[self.current_row].append(sg.Text(text))

    def set_file_browser_to_layout(self):
        self.layout[self.current_row].append(sg.FileBrowse())

    def set_radio_button_to_layout(self, text, group, state, _key):
        self.layout[self.current_row].append(sg.Radio(text, group, default=state, key=_key))

    def set_output_field_to_layout(self, _size):
        self.layout[self.current_row].append(sg.Output(size=_size))

    def set_submit_button_to_layout(self):
        self.layout[self.current_row].append(sg.Submit())

    def set_cancel_button_to_layout(self):
        self.layout[self.current_row].append(sg.Cancel())

    def set_next_row(self):
        self.layout.append([])
        self.current_row += 1

    def get_window(self, title):
        self.window = sg.Window(title, self.layout)
        return self.window
