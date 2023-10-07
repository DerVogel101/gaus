# Author: DerVogel101
# Github: https://github.com/DerVogel101
# Date: 26.09.2023
# Description: This is a simple Flutter app that solves a system of linear equations using the Gauss algorithm.

from gauss import Gauss
from gauss import list_to_matrix
from flet import Page, colors, ScrollMode, AppView, app
from flet import Text, TextField, ElevatedButton


def main(page: Page):
    """
    Main function of the app
    """
    global default_color  # NOQA needed for eval
    default_color = colors.PRIMARY  # Default color for the border of the text fields
    fields = 3  # Default value for the number of fields
    entry_elements = []

    def conf_submit_click(e):  # NOQA event parameter is needed
        """
        Deletes elements from the configuration Phase and adds the Elements for the input Phase
        """
        # gets the number of fields from the configuration, arguments are not available in event functions
        global fields  # NOQA needed for other functions
        # if the user doesn't enter a number, the default value is used
        if configuration_elements["input_fields"].value == "":
            configuration_elements["input_fields"].value = str(fields)
        fields = int(configuration_elements["input_fields"].value)

        # remove elements from configuration
        for conf_element in configuration_elements:
            page.remove(configuration_elements[conf_element])

        # add elements for input
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
        """
        Clears the input fields and the result fields
        """
        for entryclr_element in entry_elements:
            entryclr_element.value = ""
            page.update(entryclr_element)
        input_elements["result"].value = ""
        page.update(input_elements["result"])

    def input_submit_click(e):  # NOQA event parameter is needed
        """
        Solves the system of linear equations and displays the result
        """
        str_matrix = []
        # get the values from the input fields
        for entryin_element in entry_elements:
            if "," in entryin_element.value:
                entryin_element.value = entryin_element.value.replace(",", ".")
            str_matrix.append(entryin_element.value)
        matrix = list_to_matrix(str_matrix)
        # initialize Gauss object
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
        # solve the system of linear equations
        try:
            gauss.gauss_solve()
        except Gauss.SolveError:
            input_elements["result"].value = "Fehler: Das Gleichungssystem ist nicht lösbar!"
            page.update(input_elements["result"])
            return

        # display the result
        gauss.gauss_solve_result()
        matrix_result = gauss.get_result()
        matrix_result_str = ""
        for row in matrix_result:
            matrix_result_str += f"{row} = {matrix_result[row][0]}\n"
        matrix_result_str += "\n"
        for row in matrix_result:
            matrix_result_str += f"{row} = {matrix_result[row][1]}\n"
        input_elements["result"].value = matrix_result_str
        page.update(input_elements["result"])

    # Elements for the configuration Phase
    configuration_elements = {"title": Text("Gleichungssystem Konfiguration", size=24),
                              "instructions": Text("Geben Sie die Anzahl der Variablen ein:", size=16),
                              "input_fields": TextField(label="Anzahl", value="3", hint_text="Anzahl der Variablen",
                                                        border_color=default_color),
                              "submit": ElevatedButton(text="Weiter", on_click=conf_submit_click)}
    # Elements for the input Phase
    input_elements = {"title": Text("Gleichungssystem Eingabe", size=24),
                      "tip": Text("Tipp: Die Einträge müssen wie folgt eingegeben werden:\n1+2=6\n2-1=2\n"
                                  "Es besteht die Möglichkeit ein Leerzeichen anstelle eines + zu benutzen\n"
                                  "Es ist auch möglich Brüche zu benutzen\n\n"
                                  "Die variblen werden dann wie folgt zugewiesen:\n"
                                  "x, y, z, a, b, c, d ... w", size=16),
                      "clear": ElevatedButton(text="Löschen", on_click=input_clear_click),
                      "submit": ElevatedButton(text="Weiter", on_click=input_submit_click),
                      "result_title": Text("Ergebnis:", size=24),
                      "result": TextField(value="", multiline=True, border_color=default_color,
                                          hint_text="Ergebnis wird hier angezeigt")
                      }
    # Elements for the input fields
    dynamic_elements = {"entry": 'TextField(label=f"Zeile: {i+1}", border_color=default_color)'}

    # add elements for configuration
    page.scroll = ScrollMode.AUTO
    page.title = "Gleichungssystem Konfiguration"
    for element in configuration_elements:
        page.add(configuration_elements[element])


if __name__ == '__main__':
    web_app = True
    if web_app:
        app(target=main, view=AppView.WEB_BROWSER)
    else:
        app(target=main)
