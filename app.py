from gauss import Gauss
import flet as ft


def main(page: ft.Page):
    page.title = "Gleichungssystem"

    # Überschrift
    title = ft.Text("Gleichungssystem")
    page.add(title)

    # Eingabefelder
    for i in range(5):
        entry = ft.TextField()
        page.add(entry)

    # Regler
    scale = ft.Slider(min=1, max=10)
    page.add(scale)


ft.app(main)
