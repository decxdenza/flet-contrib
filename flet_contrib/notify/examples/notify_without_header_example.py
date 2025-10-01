from flet import *

from flet_contrib.notify import NotifyMode, Notify

def main(page: Page):
    
    def open_notify(e):
        notify.open('test', 'Notification without header') # open notify with 'test' mode
        
    page.add(
        Row(
            tight=True,
            controls=[
                TextButton('notify without header', on_click=open_notify)
            ]
        )
    )
    
    page.window.width = 700
    page.window.height = 500
    
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    notify = Notify(
        modes=[
            NotifyMode(name='test') # register NotifyMode object with default parameters
        ],
        bottom_to_top_end=Offset(0, 2.9), # set custom end offset. Because default is not enough
        divider_visible=False # turn off divider visibility
    )
    
    page.add(notify)

app(target=main)