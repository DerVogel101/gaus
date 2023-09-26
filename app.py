from gauss import Gauss
from gauss import list_to_matrix
from flet import Page, colors, ScrollMode, AppView, app
from flet import Text, TextField, ElevatedButton


def main(page: Page):
    global default_color  # NOQA needed for eval
    default_color = colors.PRIMARY
    fields = 3
    entry_elements = []

    def conf_submit_click(e):  # NOQA event parameter is needed
        """
        Deletes elements from the configuration Phase and adds the Elements for the input Phase
        """
        global fields  # NOQA needed for other functions
        if configuration_elements["input_fields"].value == "":
            configuration_elements["input_fields"].value = "3"
        fields = int(configuration_elements["input_fields"].value)

        for conf_element in configuration_elements:
            page.remove(configuration_elements[conf_element])

        page.title = "Gleichungssystem Eingabe"
        input_elements_keys = list(input_elements.keys())
        for i in range(0, 2):
            page.add(input_elements[input_elements_keys[i]])

        for i in range(fields):
            entry_elements.append(eval(dynamic_elements["entry"]))
            page.add(entry_elements[i])

        for i in range(2, 6):
            page.add(input_elements[input_elements_keys[i]])

    def input_clear_click(e):  # NOQA event parameter is needed
        for entryclr_element in entry_elements:
            entryclr_element.value = ""
            page.update(entryclr_element)
        input_elements["result"].value = ""
        page.update(input_elements["result"])

    def input_submit_click(e):  # NOQA event parameter is needed
        str_matrix = []
        for entryin_element in entry_elements:
            str_matrix.append(entryin_element.value)
        matrix = list_to_matrix(str_matrix)
        try:
            gauss = Gauss(matrix)
        except Gauss.SizeError:
            input_elements["result"].value = "Fehler: Die Matrix hat eine ungültige Größe!"
            page.update(input_elements["result"])
            return
        except Gauss.FormatError:
            input_elements["result"].value = "Fehler: Die Anzahl der Variablen stimmt nicht mit der Anzahl " \
                                             "der Gleichungen überein!"
            page.update(input_elements["result"])
            return
        try:
            gauss.gauss_solve()
        except Gauss.SolveError:
            input_elements["result"].value = "Fehler: Das Gleichungssystem ist nicht lösbar!"
            page.update(input_elements["result"])
            return
        gauss.gauss_solve_result()
        matrix_result = gauss.get_result()
        matrix_result_str = ""
        for row in matrix_result:
            matrix_result_str += f"{row} = {matrix_result[row]}\n"
        input_elements["result"].value = matrix_result_str
        page.update(input_elements["result"])

    configuration_elements = {"title": Text("Gleichungssystem Konfiguration", size=24),
                              "instructions": Text("Geben Sie die Anzahl der Variablen ein:", size=16),
                              "input_fields": TextField(label="Anzahl", value="3", hint_text="Anzahl der Variablen",
                                                        border_color=default_color),
                              "submit": ElevatedButton(text="Weiter", on_click=conf_submit_click)}

    input_elements = {"title": Text("Gleichungssystem Eingabe", size=24),
                      "tip": Text("Tipp: Die Einträge müssen wie folgt eingegeben werden:\n1+2=6\n2-1=2\n\n"
                                  "Die variblen werden dann wie folgt zugewiesen:\n"
                                  "x, y, z, a, b, c, d ... w", size=16),
                      "clear": ElevatedButton(text="Löschen", on_click=input_clear_click),
                      "submit": ElevatedButton(text="Weiter", on_click=input_submit_click),
                      "result_title": Text("Ergebnis:", size=24),
                      "result": TextField(value="", multiline=True, border_color=default_color,
                                          hint_text="Ergebnis wird hier angezeigt")
                      }

    dynamic_elements = {"entry": 'TextField(label=f"Zeile: {i+1}", border_color=default_color)'}

    page.scroll = ScrollMode.AUTO
    page.title = "Gleichungssystem Konfiguration"
    for element in configuration_elements:
        page.add(configuration_elements[element])


if __name__ == '__main__':
    web_app = False
    if web_app:
        app(target=main, view=AppView.WEB_BROWSER)
    else:
        app(target=main)
