import pdf
import text_reader
import pygui as pg
import os

if __name__ == '__main__':
    gui = pg.GUI()

    gui.set_label_to_layout('PDF file')
    gui.set_input_to_layout('pdf_path')
    gui.set_file_browser_to_layout()
    gui.set_radio_button_to_layout('ru', 'radio_lang', True, 'ru')
    gui.set_radio_button_to_layout('en', 'radio_lang', False, 'en')
    gui.set_next_row()

    gui.set_label_to_layout('Output filename')
    gui.set_input_to_layout('output_filename')
    gui.set_next_row()

    gui.set_output_field_to_layout((80, 10))
    gui.set_next_row()

    gui.set_submit_button_to_layout()
    gui.set_cancel_button_to_layout()

    window = gui.get_window('PDF to voice reader')

    while True:
        event, values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == 'Submit':
            language_read_in = 'ru' if values['ru'] else 'en'
            pdf_file_path = values['pdf_path']
            output_filename = values['output_filename']
            if os.path.isfile(pdf_file_path):
                print("Script is working... Wait...")
                window.refresh()
                pdf_file = pdf.PDF(pdf_file_path)
                reader = text_reader.TextReader(pdf_file.get_text(), language_read_in)
                reader.convert_to_audio_and_save(output_filename)
                print(f"File {output_filename}.mp3 created!")
            else:
                print("PDF file is not exists")
