from flet import *

from flet_contrib.notify import NotifyMode, NotifyOpenDirection, Notify

def main(page: Page):
    
    def open_notify(e):
        notify.open(e.control.text, 'Message', 'Header') # open notify with 'e.control.text' mode
        
    page.add(
        Row(
            tight=True,
            controls=[
                TextButton('test', on_click=open_notify),
                TextButton('warning', on_click=open_notify),
                TextButton('error', on_click=open_notify)
            ]
        )
    )
    
    page.window.width = 700
    page.window.height = 500
    
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    notify = Notify(
        modes=[
            NotifyMode( # register NotifyMode object with default parameters
                name='test'
            ),
            NotifyMode( # register NotifyMode object with half of parameters
                name='warning',
                color='deeppurple500',
                icon=Icons.WARNING_ROUNDED
            ),
            NotifyMode( # register NotifyMode object with almost all parameters
                name='error',
                color='red900',
                icon=Icons.ERROR_ROUNDED,
                icon_color='bluegrey800',
                header_color='bluegrey800',
                message_color='bluegrey900'
            )
        ],
        open_direction=NotifyOpenDirection.BOTTOM_TO_TOP,
        bottom_to_top_end=Offset(0, 2.9), # set custom end offset. Because default is not enough
        divider_visible=False # turn off divider visibility
    )
    
    page.add(notify)

app(target=main)