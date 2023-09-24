from gauss import Gauss
import flet as ft
from flet import AppView


def main(page: ft.Page):
    global default_color
    default_color = ft.colors.PRIMARY
    fields = 3

    def conf_submit_click(e):
        """
        Deletes elements from the configuration Phase and adds the Elements for the input Phase
        """
        global fields
        if configuration_elements["input_fields"].value == "":
            configuration_elements["input_fields"].value = "3"
        fields = int(configuration_elements["input_fields"].value)

        for element in configuration_elements:
            page.remove(configuration_elements[element])

        page.title = "Gleichungssystem Eingabe"
        input_elements_keys = list(input_elements.keys())
        for i in range(0, 2):
            page.add(input_elements[input_elements_keys[i]])

        for i in range(fields):
            page.add(eval(dynamic_elements["entry"]))

        for i in range(2, 4):
            page.add(input_elements[input_elements_keys[i]])

    def input_clear_click(e):
        ...

    def input_submit_click(e):
        ...

    configuration_elements = {"title": ft.Text("Gleichungssystem Konfiguration", size=24),
                              "instructions": ft.Text("Geben Sie die Anzahl der Variablen ein:", size=16),
                              "input_fields": ft.TextField(label="Anzahl", value="3", hint_text="Anzahl der Variablen",
                                                           border_color=default_color),
                              "submit": ft.ElevatedButton(text="Weiter", on_click=conf_submit_click)}

    input_elements = {"title": ft.Text("Gleichungssystem Eingabe", size=24),
                      "tip": ft.Text("Tipp: Die Einträge müssen wie folgt eingegeben werden:\n1x+2y=6\n2x-1y=2", size=16),
                      "clear": ft.ElevatedButton(text="Löschen", on_click=input_clear_click),
                      "submit": ft.ElevatedButton(text="Weiter", on_click=input_submit_click)
                      }

    dynamic_elements = {"entry": 'ft.TextField(label=f"Zeile: {i+1}", border_color=default_color)'}

    page.scroll = ft.ScrollMode.AUTO
    page.title = "Gleichungssystem Konfiguration"
    for element in configuration_elements:
        page.add(configuration_elements[element])


ft.app(target=main, view=AppView.WEB_BROWSER)
