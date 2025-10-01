from flet import *

from flet_contrib.notify import NotifyMode, NotifyOpenDirection, Notify

def main(page: Page):
    
    def open_notify(e):
        notify.open('test', message.value, header.value) # open notify with 'test' mode
    
    header = TextField(label='Header', value='Header')
    message = TextField(label='Message', value='Message')
    
    page.add(
        Column(
            tight=True,
            controls=[
                header,
                message,
                TextButton('open', on_click=open_notify),
            ]
        ),
    )
    
    page.window.width = 700
    page.window.height = 500
    
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    notify = Notify(
        modes=[
            NotifyMode(name='test') # register NotifyMode object with default parameters
        ],
        open_direction=NotifyOpenDirection.BOTTOM_TO_TOP,
        bottom_to_top_end=Offset(0, 1.95), # set custom end offset. Because default is not enough
        divider_visible=False # turn off divider visibility
    )
    
    page.add(notify)

app(target=main)