import flet 
from . import theme
from ui.widgets import header, footer

class HomePage:
    def __init__(self, page:flet.Page):
        self.page = page
        self.build()
    
    def build(self):
        self.page.bgcolor = "#FFFFFE"
        self.page.add(
            flet.Column(
                controls=[
                    header.header_ui(),
                    footer.footer_ui()

                ]
            )
            
        )