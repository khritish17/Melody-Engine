import flet

from ui.home_page import HomePage
from ui.widgets import visualizer, generate_music_panel


def main(page: flet.Page):
    visualizer.page_ref = page
    generate_music_panel.page_ref = page
    page.title = "Melody Engine"

    page.window.width = 1400
    page.window.height = 900

    page.window.resizable = False
    page.window.center()

    HomePage(page=page)

flet.app(target = main)