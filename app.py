from gauss import Gauss
import flet as ft


def main_config(page: ft.Page):
    def submit_click(e):
        global fields
        if input_fields.value == "":
            input_fields.value = "3"
        fields = int(input_fields.value)
        page.window_destroy()

    def window_event(e):
        global fields
        if e.data == "close":
            fields = 3
            page.window_destroy()

    page.window_prevent_close = True
    page.on_window_event = window_event

    page.title = "Gleichungssystem"

    title = ft.Text("Gleichungssystem Konfiguration", size=24)
    page.add(title)

    # Instructions
    instructions = ft.Text("Geben Sie die Anzahl der Variablen ein:", size=16)
    page.add(instructions)

    input_fields = ft.TextField(label="Anzahl", value="3", hint_text="Anzahl der Variablen")
    submit = ft.ElevatedButton(text="Weiter", on_click=submit_click)
    page.add(input_fields, submit)
    print(page.controls)


def main_window(page: ft.Page):
    page.title = "Gleichungssystem"

    # Überschrift
    title = ft.Text("Gleichungssystem", size=24)
    page.add(title)

    # Tipp
    tip = ft.Text("Tipp: Die Einträge müssen wie folgt eingegeben werden:\n"
                  "1x+2y=6\n"
                  "2x-1y=2", size=16)
    page.add(tip)

    # Eingabefelder
    for i in range(fields):
        entry = ft.TextField()
        page.add(entry)

    # Regler
    scale = ft.Slider(min=1, max=10)
    page.add(scale)


ft.app(main_config)
fields: int = fields
ft.app(target=main_window)
