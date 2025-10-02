# Notify

`Notify` control is used to display information using a pop-up in-app notification.
`Notify` control inherits from [`Container`](https://flet.dev/docs/controls/container).

## Examples

<img src="media/default_notify.png"><img src="media/warning_notify.png"><img src="media/error_notify.png">

```python
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
```

## Properties

### `modes`

List of notification modes.

### `open_time`

Notification display time.

Defaults to `3`

### `open_direction`

Notification animation direction

Defaults to `NotifyOpenDirection.BOTTOM_TO_TOP`

### `width`

Width of main notification container

Defaults to `300`

### `height`

Height of main notification container

Defaults to `60`

### `header_width`

Width of header control

Defaults to `240`

### `message_width`

Width of message control

Defaults to `240`

### `theme`

Theme of `Notify` object

Defaults to `NotifyTheme()`

### `padding`

Padding of main notification container

Defaults to `12`

### `row_spacing`

Spacing between controls in a row (`Icon`, `VerticalDivider`, `Text`)

Defaults to `15`

### `row_alignment`

Alignment of controls in a row (`Icon`, `VerticalDivider`, `Text`)

Defaults to `'start'`

### `text_column_spacing`

Spacing between text controls in a column (`header`, `message`)

Defaults to `1`

### `text_column_alignment`

Alignment of text controls in a column (`header`, `message`)

Defaults to `'start'`

### `border_width`

Width of borders of main notification container

Defaults to `1`

### `border_radius`

Radius of rounding corners of main notification container

Defaults to `10`

### `border_color`

Color of borders of main notification container

Defaults to `'grey800`

### `divider_visible`

Visibility of divider between icon and text

Defaults to `True`

### `bottom_to_top_start`

Custom start offset for `NotifyOpenDirection.BOTTOM_TO_TOP` direction.

Defaults to `DefaultOffsets.bottom_to_top_start`

### `bottom_to_top_end`

Custom end offset for `NotifyOpenDirection.BOTTOM_TO_TOP` direction.

Defaults to `DefaultOffsets.bottom_to_top_end`

### `bottom_right_to_left_start`

Custom start offset for `NotifyOpenDirection.BOTTOM_RIGHT_TO_LEFT` direction.

Defaults to `DefaultOffsets.bottom_right_to_left_start`

### `bottom_right_to_left_end`

Custom end offset for `NotifyOpenDirection.BOTTOM_RIGHT_TO_LEFT` direction.

Defaults to `DefaultOffsets.bottom_right_to_left_end`

### `bottom_left_to_right_start`

Custom start offset for `NotifyOpenDirection.BOTTOM_LEFT_TO_RIGHT` direction.

Defaults to `DefaultOffsets.bottom_left_to_right_start`

### `bottom_left_to_right_end`

Custom end offset for `NotifyOpenDirection.BOTTOM_LEFT_TO_RIGHT` direction.

Defaults to `DefaultOffsets.bottom_left_to_right_end`

### `top_to_bottom_start`

Custom start offset for `NotifyOpenDirection.TOP_TO_BOTTOM` direction.

Defaults to `DefaultOffsets.top_to_bottom_start`

### `top_to_bottom_end`

Custom end offset for `NotifyOpenDirection.TOP_TO_BOTTOM` direction.

Defaults to `DefaultOffsets.top_to_bottom_end`

### `top_right_to_left_start`

Custom start offset for `NotifyOpenDirection.TOP_RIGHT_TO_LEFT` direction.

Defaults to `DefaultOffsets.top_right_to_left_start`

### `top_right_to_left_end`

Custom end offset for `NotifyOpenDirection.TOP_RIGHT_TO_LEFT` direction.

Defaults to `DefaultOffsets.top_right_to_left_end`

### `top_left_to_right_start`

Custom start offset for `NotifyOpenDirection.TOP_LEFT_TO_RIGHT` direction.

Defaults to `DefaultOffsets.top_left_to_right_start`

### `top_left_to_right_end`

Custom end offset for `NotifyOpenDirection.TOP_LEFT_TO_RIGHT` direction.

Defaults to `DefaultOffsets.top_left_to_right_end`

## Functions

### **`open(mode: NotifyMode | str, message_text: str, header_text: str = None) -> None`**

Notification display function.
  
**Parameters**
- `mode` - `NotifyMode` object or the name of `NotifyMode` object passed in the `modes` parameter earlier.
- `message_text` - Message text to display.
- `header_text` - Header text to display (*Optional).

### **`_reveal() -> None`**

Function to remove transparency from main notification container.

### **`_get_mode(name: str) -> NotifyMode | None`**

Function for getting the `NotifyMode` object loaded into the `modes` list.

### **`_set_mode(mode: NotifyMode) -> None`**

Notification formatting function.
- *Edits the appearance of main notification container. Based on passed mode.*
 
**Parameters**
- `mode` - `NotifyMode` object, which will change the appearance of main notification container.

### **`__set_direction(direction: NotifyOpenDirection, upd: bool = True) -> None`**

A function for specifying direction of notification animation.

**Parameters**
- `direction` - New notification animation direction.

### **`__draw() -> None`**

Notification animation function.

# NotifyMode
A `dataclass` that describes basic appearance parameters for `Notify` object.
    
This allows you to change appearance of notifications by using `NotifyMode.name` as a parameter for the `Notify.open()`.

## Properties

### `name`
The name by which this `NotifyMode` instance will be available in future.

Defaults to `'mode{randint(100, 500)}'`

### `color`
Background color of main notification container.

Defaults to `'black'`

### `gradient`
Gradient of main notification container.

Defaults to `None`

### `icon`
Notification icon.

Defaults to `Icons.INFO_ROUNDED`

### `icon_color`
Notification icon color.

Defaults to `'white70'`

### `header_color`
Header text color.

Defaults to `'white70'`

### `message_color`
Message text color.

Defaults to `'white60'`

### `divider_color`
Color of divider that separates icon and text.

Defaults to `'grey800'`

# NotifyTheme
A `dataclass` that describes parameters of a `Notify` and its elements.

## Properties

### `header_size`
Size of header text.

Defaults to `11`

### `header_weight`
Font weight of header text.

Defaults to `'bold'`

### `header_text_align`
Alignment of header text.

Defaults to `'left'`

### `message_size`
Size of message text.

Defaults to `10`

### `message_weight`
Font weight of message text.

Defaults to `'w500'`

### `message_text_align`
Alignment of message text.

Defaults to `'left'`

### `text_animate_opacity`
Text controls opacity animation speed (`header`, `message`).

Defaults to `400`

### `divider_width`
Width of divider between icon and text.

Defaults to `1`

### `divider_thickness`
Thickness of divider between icon and text.

Defaults to `2`

### `animate`
Animation of main notification container.

Defaults to `Animation(600, 'decelerate')`

### `animate_offset`
Main notification container offset animation speed.

Defaults to `400`

### `animate_opacity`
Main notification container opacity animation speed.

Defaults to `400`

# NotifyOpenDirection
Enum of notification display directions.

Each NotifyOpenDirection value has its own 2 offsets.

## Properties

### `BOTTOM_TO_TOP`
From bottom to top direction, centered, at bottom

### `BOTTOM_RIGHT_TO_LEFT`
From right to left direction, at bottom

### `BOTTOM_LEFT_TO_RIGHT`
From left to right direction, at bottom

### `TOP_TO_BOTTOM`
From top to bottom direction, centered, at top

### `TOP_RIGHT_TO_LEFT`
From right to left direction, at top

### `TOP_LEFT_TO_RIGHT`
From left to right direction, at top

# DefaultOffsets
Enum of basic offsets for beginning and end of animation.

`Start offset` - offset at which the animation begins.

`End offset` - offset at which the animation ends.

## Properties

### `bottom_to_top_start`
From bottom to top, centered, at bottom. Start offset.

Defaults to `Offset(0, 9)`

### `bottom_to_top_end`
From bottom to top, centered, at bottom. End offset.

Defaults to `Offset(0, 4.1)`

### `bottom_right_to_left_start`
From right to left, at bottom. Start offset.

Defaults to `Offset(2, 4.1)`

### `bottom_right_to_left_end`
From right to left, at bottom. End offset.

Defaults to `Offset(0.625, 4.1)`

### `bottom_left_to_right_start`
From left to right, at bottom. Start offset.

Defaults to `Offset(-2, 4.1)`

### `bottom_left_to_right_end`
From left to right, at bottom. End offset.

Defaults to `Offset(-0.625, 4.1)`

### `top_to_bottom_start`
From top to bottom, centered, at top. Start offset.

Defaults to `Offset(0, -9)`

### `top_to_bottom_end`
From top to bottom, centered, at top. End offset.

Defaults to `Offset(0, -4.1)`

### `top_right_to_left_start`
From right to left, at top. Start offset.

Defaults to `Offset(2, -4.1)`

### `top_right_to_left_end`
From right to left, at top. End offset.

Defaults to `Offset(0.625, -4.1)`

### `top_left_to_right_start`
From left to right, at top. Start offset.

Defaults to `Offset(-2, -4.1)`

### `top_left_to_right_end`
From left to right, at top. End offset.

Defaults to `Offset(-0.625, -4.1)`
