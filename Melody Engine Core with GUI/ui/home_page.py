import flet 
from . import theme
from ui.widgets import header, footer, middle_section

class HomePage:
    def __init__(self, page:flet.Page):
        self.page = page
        self.page.padding = 20
        self.build()
    
    def build(self):
        self.page.bgcolor = "#FFFFFE"
        self.page.add(
            flet.Column(
                expand = True,
                controls=[
                    header.header_ui(),
                    flet.Container(
                        expand = True,
                        content=middle_section.middle_section_ui()
                    ),
                    footer.footer_ui(),
                ]
            )
            
        )