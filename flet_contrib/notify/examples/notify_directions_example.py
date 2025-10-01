from flet import *

from flet_contrib.notify import NotifyMode, NotifyOpenDirection, Notify

def main(page: Page):
    
    def open_notify(e):
        notify.open('test', 'Message', 'Header') # open notify with 'test' mode
    
    def notify_direction_change(e):
        notify.open_direction = NotifyOpenDirection.__getattribute__(NotifyOpenDirection, e.control.value)
        
    page.add(
        Column(
            tight=True,
            controls=[
                Dropdown(
                    value='BOTTOM_TO_TOP',
                    options=[
                        DropdownOption('BOTTOM_TO_TOP'),
                        DropdownOption('BOTTOM_RIGHT_TO_LEFT'),
                        DropdownOption('BOTTOM_LEFT_TO_RIGHT'),
                        DropdownOption('TOP_TO_BOTTOM'),
                        DropdownOption('TOP_RIGHT_TO_LEFT'),
                        DropdownOption('TOP_LEFT_TO_RIGHT'),
                    ], on_change=notify_direction_change
                ),
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
        bottom_to_top_end=Offset(0, 2.4), # set custom end offset. Because default is not enough
        bottom_right_to_left_start=Offset(3, 2.4),
        bottom_right_to_left_end=Offset(0.625, 2.4),
        bottom_left_to_right_start=Offset(-3, 2.4),
        bottom_left_to_right_end=Offset(-0.625, 2.4),
        top_to_bottom_start=Offset(0, -6),
        top_to_bottom_end=Offset(0, -4.1),
        top_right_to_left_start=Offset(3, -4.1),
        top_right_to_left_end=Offset(0.625, -4.1),
        top_left_to_right_start=Offset(-3, -4.1),
        top_left_to_right_end=Offset(-0.625, -4.1),
        divider_visible=False # turn off divider visibility
    )
    
    page.add(notify)

app(target=main)