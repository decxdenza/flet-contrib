from flet import *
from typing import Optional
from dataclasses import dataclass, field
from random import randint
from enum import Enum
from time import sleep


@dataclass
class NotifyMode():
    """A **`dataclass`** that describes basic appearance parameters for **`Notify`** object.
    
    This allows you to change appearance of notifications by using **`NotifyMode.name`** as a parameter for the **`Notify.open()`**

    :param str name: The name by which this **`NotifyMode`** instance will be available in future
    \n        - Defaults to **`'mode{randint(100, 500)}'`**
    :param Colors | str color: Background colors of main notification container
    \n        - Defaults to **`'black`**
    :param LinearGradient | RadialGradient | SweepGradient gradient: Gradient of main notification container
    \n        - Defaults to **`None`**
    :param Icons | str icon: Notification icon
    \n        - Defaults to **`Icons.INFO_ROUNDED`**
    :param Colors | str icon_color: Icon color
    \n        - Defaults to **`'white70'`**
    :param Colors | str header_color: Header text color
    \n        - Defaults to **`'white70'`**
    :param Colors | str message_color: Message text color
    \n        - Defaults to **`'white60'`**
    :param Colors | str divider_color: Color of divider that separates icon and text
    \n        - Defaults to **`'grey800'`**
    """

    name: str = 'mode{0}'.format(str(randint(100, 500)))

    color: Optional[Colors | str] = 'black'
    gradient: Optional[LinearGradient | RadialGradient | SweepGradient] = None
    icon: Optional[Icons | str] = Icons.INFO_ROUNDED
    icon_color: Optional[Colors | str] = 'white70'
    header_color: Optional[Colors | str] = 'white70'
    message_color: Optional[Colors | str] = 'white60'
    divider_color: Optional[Colors | str] = 'grey800'


@dataclass
class NotifyTheme():
    """A **`dataclass`** that describes appearance of a **`Notify`** and its elements
    
    :param Optional[int | float] header_size: Size of header text
    \n        - Defaults to **`11`**
    :param Optional[FontWeight | str] header_weight: Font weight of header text
    \n        - Defaults to **`'bold`**
    :param Optional[TextAlign | str] header_text_align: Alignment of header text
    \n        - Defaults to **`'left'`**
    :param Optional[int | float] message_size: Size of message text
    \n        - Defaults to **`10`**
    :param Optional[FontWeight | str] message_weight: Font weight of message text
    \n        - Defaults to **`'w500'`**
    :param Optional[TextAlign | str] message_text_align: Alignment of message text
    \n        - Defaults to **`'left`**
    :param Optional[int | float] text_animate_opacity: Text controls opacity animation speed (**`header`**, **`message`**)
    \n        - Defaults to **`400`**
    :param Optional[int | float] divider_width: Width of divider between icon and text
    \n        - Defaults to **`1`**
    :param Optional[int | float] divider_thickness: Thickness of divider between icon and text
    \n        - Defaults to **`2`**
    :param Optional[Animation] animate: Animation of main notification container
    \n        - Defaults to **`Animation(600, 'decelerate')`**
    :param Optional[int | float] animate_offset: Main notification container offset animation speed
    \n        - Defaults to **`400`**
    :param Optional[int | float] animate_opacity: Main notification container opacity animation speed
    \n        - Defaults to **`400`**
    """

    header_size: Optional[int | float] = 11
    header_weight: Optional[FontWeight | str] = 'bold'
    header_text_align: Optional[TextAlign | str] = 'left'
    message_size: Optional[int | float] = 10
    message_weight: Optional[FontWeight | str] = 'w500'
    message_text_align: Optional[TextAlign | str] = 'left'
    text_animate_opacity: Optional[int | float] = 400
    divider_width: Optional[int | float] = 1
    divider_thickness: Optional[int | float] = 2
    animate: Optional[Animation] = field(default_factory=lambda : Animation(600, 'decelerate'))
    animate_offset: Optional[int | float] = 400
    animate_opacity: Optional[int | float] = 400


class NotifyOpenDirection(Enum):
    """.. Enum:: of notification display directions
    - **BOTTOM_TO_TOP** - From bottom to top direction, centered, at bottom
    - **BOTTOM_RIGHT_TO_LEFT** - From right to left direction, at bottom
    - **BOTTOM_LEFT_TO_RIGHT** - From left to right direction, at bottom
    - **TOP_TO_BOTTOM** - From top to bottom direction, centered, at top
    - **TOP_RIGHT_TO_LEFT** - From right to left direction, at top
    - **TOP_LEFT_TO_RIGHT** - From left to right direction, at top
    """
    
    BOTTOM_TO_TOP = 'bottom_to_top'
    BOTTOM_RIGHT_TO_LEFT = 'bottom_right_to_left'
    BOTTOM_LEFT_TO_RIGHT = 'bottom_left_to_right'
    TOP_TO_BOTTOM = 'top_to_bottom'
    TOP_RIGHT_TO_LEFT = 'top_right_to_left'
    TOP_LEFT_TO_RIGHT = 'top_left_to_right'


@dataclass
class DefaultOffsets():
    """**`Enum`** of basic offsets for beginning and end of animation
    
    \n`Start offset` - offset at which the animation begins
    \n`End offset` - offset at which the animation ends.
    
    - **bottom_to_top_start**
        - From bottom to top, centered, at bottom. Start offset
        - Defaults to **`Offset(0, 9)`**
    - **bottom_to_top_end**
        - From bottom to top, centered, at bottom. End offset
        - Defaults to **`Offset(0, 4.1)`**
    - **bottom_right_to_left_start**
        - From right to left, at bottom. Start offset
        - Defaults to **`Offset(2, 4.1)`**
    - **bottom_right_to_left_end**
        - From right to left, at bottom. End offset
        - Defaults to **`Offset(0.625, 4.1)`**
    - **bottom_left_to_right_start**
        - From left to right, at bottom. Start offset
        - Defaults to **`Offset(-2, 4.1)`**
    - **bottom_left_to_right_end**
        - From left to right, at bottom. End offset
        - Defaults to **`Offset(-0.625, 4.1)`**
    - **top_to_bottom_start**
        - From top to bottom, centered, at top. Start offset
        - Defaults to **`Offset(0, -9)`**
    - **top_to_bottom_end**
        - From top to bottom, centered, at top. End offset
        - Defaults to **`Offset(0, -4.1)`**
    - **top_right_to_left_start**
        - From right to left, at top. Start offset
        - Defaults to **`Offset(2, -4.1)`**
    - **top_right_to_left_end**
        - From right to left, at top. End offset
        - Defaults to **`Offset(0.625, -4.1)`**
    - **top_left_to_right_start**
        - From left to right, at top. Start offset
        - Defaults to **`Offset(-2, -4.1)`**
    - **top_left_to_right_end**
        - From left to right, at top. End offset
        - Defaults to **`Offset(-0.625, -4.1)`**
    """
    bottom_to_top_start = Offset(0, 9)
    bottom_to_top_end = Offset(0, 4.1)
    bottom_right_to_left_start = Offset(2, 4.1)
    bottom_right_to_left_end = Offset(0.625, 4.1)
    bottom_left_to_right_start = Offset(-2, 4.1)
    bottom_left_to_right_end = Offset(-0.625, 4.1)
    top_to_bottom_start = Offset(0, -9)
    top_to_bottom_end = Offset(0, -4.1)
    top_right_to_left_start = Offset(2, -4.1)
    top_right_to_left_end = Offset(0.625, -4.1)
    top_left_to_right_start = Offset(-2, -4.1)
    top_left_to_right_end = Offset(-0.625, -4.1)


class Notify(Container):
    """Main **`class`** of notifications. Based on **`Container`**

    :param list[NotifyMode] modes: List of notification modes
    :param Optional[int | float] open_time: Notification display time
    \n        - Defaults to **`3`**
    :param Optional[NotifyOpenDirection] open_direction: Notification animation direction
    \n        - Defaults to **`NotifyOpenDirection.BOTTOM_TO_TOP`**
    :param Optional[int | float] width: Width of main notification container
    \n        - Defaults to **`300
    :param Optional[int | float] height: Height of main notification container
    \n        - Defaults to **`60`**
    :param Optional[int | float] header_width: Width of header control
    \n        - Defaults to **`240`**
    :param Optional[int | float] message_width: Width of message control
    \n        - Defaults to **`240`**
    :param Optional[NotifyTheme] theme: Theme of **`Notify`** object
    \n        - Defaults to **`NotifyTheme()`**
    :param Optional[int | float] padding: Padding of main notification container
    \n        - Defaults to **`12`**
    :param Optional[int | float] row_spacing: Spacing between controls in a row (**`Icon`**, **`VerticalDivider`**, **`Text`**)
    \n        - Defaults to **`15`**
    :param Optional[MainAxisAlignment | str] row_alignment: Alignment of controls in a row (**`Icon`**, **`VerticalDivider`**, **`Text`**)
    \n        - Defaults to **`'start'`**
    :param Optional[int | float] text_column_spacing: Spacing between text controls in a column (**`header`**, **`message`**)
    \n        - Defaults to **`1`**
    :param Optional[MainAxisAlignment | str] text_column_alignment: Alignment of text controls in a column (**`header`**, **`message`**)
    \n        - Defaults to **`'start'`**
    :param Optional[int | float] border_width: Width of borders of main notification container
    \n        - Defaults to **`1`**
    :param Optional[int | float] border_radius: Radius of rounding corners of main notification container
    \n        - Defaults to **`10`**
    :param Optional[Colors | str] border_color: Color of borders of main notification container
    \n        - Defaults to **`'grey800`**
    :param Optional[bool] divider_visible: Visibility of divider between icon and text
    \n        - Defaults to **`True`**
    :param Optional[Offset] bottom_to_top_start: Custom start offset for `from bottom to top, centered, at bottom` direction
    \n        - Defaults to **`DefaultOffsets.bottom_to_top_start`**
    :param Optional[Offset] bottom_to_top_end: Custom end offset for `from bottom to top, centered, at bottom` direction
    \n        - Defaults to **`DefaultOffsets.bottom_to_top_end`**
    :param Optional[Offset] bottom_right_to_left_start: Custom start offset for `from right to left, at bottom` direction
    \n        - Defaults to **`DefaultOffsets.bottom_right_to_left_start`**
    :param Optional[Offset] bottom_right_to_left_end: Custom end offset for `from right to left, at bottom` direction
    \n        - Defaults to **`DefaultOffsets.bottom_right_to_left_end`**
    :param Optional[Offset] bottom_left_to_right_start: Custom start offset for `from left to right, at bottom` direction
    \n        - Defaults to **`DefaultOffsets.bottom_left_to_right_start`**
    :param Optional[Offset] bottom_left_to_right_end: Custom end offset for `from left to right, at bottom` direction
    \n        - Defaults to **`DefaultOffsets.bottom_left_to_right_end`**
    :param Optional[Offset] top_to_bottom_start: Custom start offset for `from top to bottom, centered, at top` direction
    \n        - Defaults to **`DefaultOffsets.top_to_bottom_start`**
    :param Optional[Offset] top_to_bottom_end: Custom end offset for `from top to bottom, centered, at top` direction
    \n        - Defaults to **`DefaultOffsets.top_to_bottom_end`**
    :param Optional[Offset] top_right_to_left_start: Custom start offset for `from right to left, at top` direction
    \n        - Defaults to **`DefaultOffsets.top_right_to_left_start`**
    :param Optional[Offset] top_right_to_left_end: Custom end offset for `from right to left, at top` direction
    \n        - Defaults to **`DefaultOffsets.top_right_to_left_end`**
    :param Optional[Offset] top_left_to_right_start: Custom start offset for `from left to right, at top` direction
    \n        - Defaults to **`DefaultOffsets.top_left_to_right_start`**
    :param Optional[Offset] top_left_to_right_end: Custom end offset for `from left to right, at top` direction
    \n        - Defaults to **`DefaultOffsets.top_left_to_right_end`**
    """

    def __init__(
            self,
            modes: list[NotifyMode],
            open_time: Optional[int | float] = 3,
            open_direction: Optional[NotifyOpenDirection] = NotifyOpenDirection.BOTTOM_TO_TOP,
            width: Optional[int | float] = 300,
            height: Optional[int | float] = 60,
            header_width: Optional[int | float] = 240,
            message_width: Optional[int | float] = 240,
            theme: Optional[NotifyTheme] = NotifyTheme(),
            padding: Optional[int |float] = 12,
            row_spacing: Optional[int | float] = 15,
            row_alignment: Optional[MainAxisAlignment | str] = 'start',
            text_column_spacing: Optional[int | float] = 1,
            text_column_alignment: Optional[MainAxisAlignment | str] = 'start',
            border_width: Optional[int | float] = 1,
            border_radius: Optional[int | float] = 10,
            border_color: Optional[Colors | str] = 'grey800',
            divider_visible: Optional[bool] = True,
            bottom_to_top_start: Optional[Offset] = DefaultOffsets.bottom_to_top_start,
            bottom_to_top_end: Optional[Offset] = DefaultOffsets.bottom_to_top_end,
            bottom_right_to_left_start: Optional[Offset] = DefaultOffsets.bottom_right_to_left_start,
            bottom_right_to_left_end: Optional[Offset] = DefaultOffsets.bottom_right_to_left_end,
            bottom_left_to_right_start: Optional[Offset] = DefaultOffsets.bottom_left_to_right_start,
            bottom_left_to_right_end: Optional[Offset] = DefaultOffsets.bottom_left_to_right_end,
            top_to_bottom_start: Optional[Offset] = DefaultOffsets.top_to_bottom_start,
            top_to_bottom_end: Optional[Offset] = DefaultOffsets.top_to_bottom_end,
            top_right_to_left_start: Optional[Offset] = DefaultOffsets.top_right_to_left_start,
            top_right_to_left_end: Optional[Offset] = DefaultOffsets.top_right_to_left_end,
            top_left_to_right_start: Optional[Offset] = DefaultOffsets.top_left_to_right_start,
            top_left_to_right_end: Optional[Offset] = DefaultOffsets.top_left_to_right_end
    ):
        
        self.theme = theme

        self.__open_time = open_time
        self.__open_direction = open_direction
        
        self.__bottom_to_top_start = bottom_to_top_start
        self.__bottom_to_top_end = bottom_to_top_end
        self.__bottom_right_to_left_start = bottom_right_to_left_start
        self.__bottom_right_to_left_end = bottom_right_to_left_end
        self.__bottom_left_to_right_start = bottom_left_to_right_start
        self.__bottom_left_to_right_end = bottom_left_to_right_end
        self.__top_to_bottom_start = top_to_bottom_start
        self.__top_to_bottom_end = top_to_bottom_end
        self.__top_right_to_left_start = top_right_to_left_start
        self.__top_right_to_left_end = top_right_to_left_end
        self.__top_left_to_right_start = top_left_to_right_start
        self.__top_left_to_right_end = top_left_to_right_end

        self.__set_direction(self.__open_direction, False)

        self.modes = modes
        self.__default_mode = NotifyMode('default')

        self.leading = Icon(
            name=self.__default_mode.icon
        )
        self.divider = VerticalDivider(
            width=self.theme.divider_width,
            thickness=self.theme.divider_thickness,
            visible=divider_visible
        )
        self.header = Text(
            value='header',
            size=self.theme.header_size,
            weight=self.theme.header_weight,
            width=header_width,
            text_align=self.theme.header_text_align
        )
        self.message = Text(
            value='message',
            size=self.theme.message_size,
            weight=self.theme.message_weight,
            width=message_width,
            text_align=self.theme.message_text_align
        )
        
        super().__init__(
            content=Row(
                controls=[
                    self.leading,
                    self.divider,
                    Column(
                        spacing=text_column_spacing,
                        alignment=text_column_alignment,
                        controls=[
                            self.header,
                            self.message
                        ],
                    )
                ],
                opacity=0,
                animate_opacity=self.theme.text_animate_opacity,
                spacing=row_spacing,
                alignment=row_alignment
            ),
            opacity=0,

            offset=self.__start,

            width=width,
            height=height,

            padding=padding,

            bgcolor=self.__default_mode.color if (self.__default_mode.color and
                not self.__default_mode.gradient) else None,

            gradient=self.__default_mode.gradient if (self.__default_mode.gradient and
                not self.__default_mode.color) else None,

            border=Border(
                BorderSide(width=border_width, color=border_color),
                BorderSide(width=border_width, color=border_color),
                BorderSide(width=border_width, color=border_color),
                BorderSide(width=border_width, color=border_color)
            ),
            border_radius=border_radius,

            animate=self.theme.animate,
            animate_offset=self.theme.animate_offset,
            animate_opacity=self.theme.animate_opacity
        )
    
    def open(self, mode: NotifyMode | str, message_text: str, header_text: str = None) -> None:
        """Notification display function

        :param header_text: Header text to display
        :type header_text: str
        :param message_text: Message text to display
        :type message_text: str
        :param mode: NotifyMode for formatting notification.
        \n  **`NotifyMode`** object or the name of **`NotifyMode`** object passed in the **`modes`** parameter earlier
        :type mode: NotifyMode | str
        """
        
        if (isinstance(mode, NotifyMode)):
            self._set_mode(mode)
            self.header.value = header_text
            self.message.value = message_text
        elif (isinstance(mode, str)):
            if (mode := self._get_mode(mode)):
                self._set_mode(mode)
                self.header.value = header_text
                self.message.value = message_text
        if (not header_text):
            self.header.visible = False
        elif (not self.header.visible):
            self.header.visible = True
        self.__draw()
    
    def __draw(self) -> None:
        """Notification animation function"""
        
        if (self.offset != self.__end):
            self.opacity = 1
            self.content.opacity = 1
            self.offset = self.__end
            self.update()
            sleep(self.__open_time)
            self.opacity = 0
            self.content.opacity = 0
            self.offset = self.__start
        self.update()
    
    def _reveal(self) -> None:
        """Function to remove transparency from main notification container.
        
        Can be used to calculate **`offsets`**
        """
        
        self.opacity = 1
        self.content.opacity = 1
        self.update()
    
    def __set_direction(self, direction: NotifyOpenDirection, upd: bool = True) -> None:
        """A function for specifying direction of notification animation

        :param direction:
        :type direction: NotifyOpenDirection
        """
        
        match(direction):
            case NotifyOpenDirection.BOTTOM_TO_TOP:
                self.__start, self.__end = (self.__bottom_to_top_start, self.__bottom_to_top_end)
            case NotifyOpenDirection.BOTTOM_RIGHT_TO_LEFT:
                self.__start, self.__end = (self.__bottom_right_to_left_start, self.__bottom_right_to_left_end)
            case NotifyOpenDirection.BOTTOM_LEFT_TO_RIGHT:
                self.__start, self.__end = (self.__bottom_left_to_right_start, self.__bottom_left_to_right_end)
            case NotifyOpenDirection.TOP_TO_BOTTOM:
                self.__start, self.__end = (self.__top_to_bottom_start, self.__top_to_bottom_end)
            case NotifyOpenDirection.TOP_RIGHT_TO_LEFT:
                self.__start, self.__end = (self.__top_right_to_left_start, self.__top_right_to_left_end)
            case NotifyOpenDirection.TOP_LEFT_TO_RIGHT:
                self.__start, self.__end = (self.__top_left_to_right_start, self.__top_left_to_right_end)
            case _:
                self.__start, self.__end = (self.__bottom_to_top_start, self.__bottom_to_top_end)
        
        if (upd):
            if (self.opacity == 0):
                self.offset = self.__start
                if (self.page): self.update()
    
    def _set_mode(self, mode: NotifyMode) -> None:
        """Notification formatting function

        :param mode: Formatting mode
        :type mode: NotifyMode
        """
        
        self.bgcolor = mode.color if (mode.color and
            not mode.gradient) else None
        self.gradient = mode.gradient if (mode.gradient) else None
        self.leading.name = mode.icon
        self.leading.color = mode.icon_color
        self.divider.color = mode.divider_color
        self.header.color = mode.header_color
        self.message.color = mode.message_color
        if (self.page): self.update()
    
    def _get_mode(self, name: str) -> NotifyMode | None:
        """Function for getting the **`NotifyMode`** object loaded into the **`modes`** list"""
        
        for mode in self.modes:
            if (mode.name == name):
                return mode
    
    # open_timeout
    @property
    def open_time(self):
        """Notification display time

        :returns: int | float
        """
        
        return self.__open_time

    @open_time.setter
    def open_time(self, value):
        """Notification display time

        :param value:
        :type value: int | float
        """
        
        self.__open_time = value
    
    # start
    @property
    def start(self):
        """Notification animation start offset

        :returns: Offset
        """
        
        return self.__start

    @start.setter
    def start(self, value):
        """Notification animation start offset

        :param value:
        :type value: Offset
        """
        
        self.__start = value
    
    # end
    @property
    def end(self):
        """Notification animation end offset

        :returns: Offset
        """
        
        return self.__end
    
    @end.setter
    def end(self, value):
        """Notification animation end offset

        :param value:
        :type value: Offset
        """
        
        self.__end = value
    
    # open_direction
    @property
    def open_direction(self):
        """Notification animation direction

        :returns: NotifyOpenDirection
        """
        
        return self.__open_direction

    @open_direction.setter
    def open_direction(self, value):
        """Notification animation direction

        :param value:
        :type value: NotifyOpenDirection
        """
        
        if (self.__open_direction != value):
            self.__set_direction(value)
        
        self.__open_direction = value