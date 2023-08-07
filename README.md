# Arcade notes
[Arcade API latest development release](https://api.arcade.academy/en/development/)

[Videoplayer bugfix commit](https://github.com/pythonarcade/arcade/commit/288fab37b8665276b0cef46c5e79c6dd95fde974#commitcomment-121642421)

[Pyglet bug 'free resource error on exit'](https://github.com/pyglet/pyglet/issues/885)

## Building a menu with buttons and views

https://api.arcade.academy/en/development/tutorials/menu/index.html


## Inventory demo in Arcade using VIEWS
[Arcade inventory VIEWS - part 1](https://youtu.be/fUf0Y_qTqsg)

[Arcade inventory VIEWS - part 2](https://www.youtube.com/watch?v=zeZqyhoN7-E)

## Window and View - Python Arcade 2.6.17

You need a gui manager for each view and enable/disable when the view changes.

Window.on_resize calls set_viewport by default. If you want to set your own custom viewport during the game, you may need to over-ride the on_resizemethod.

https://api.arcade.academy/en/latest/examples/index.html#view-management

https://realpython.com/platformer-python-arcade/#title-and-other-screens

https://api.arcade.academy/api/window.html
https://api.arcade.academy/en/latest/api/window.html#arcade-set-viewport

https://api.arcade.academy/en/latest/examples/full_screen_example.html#full-screen-example

https://api.arcade.academy/en/latest/examples/sections_demo_1.html#sections-demo-1

On window viewport resize 

https://api.arcade.academy/en/latest/api/window.html#arcade.View.on_resize

## Arcade.window function API

https://api.arcade.academy/en/latest/api/window.html#arcade-window
(Viewport fullscreen)

Maximise viewport window api function
https://api.arcade.academy/en/latest/api/window.html#arcade.Window.maximize

Set_fullscreen api function 
https://api.arcade.academy/en/latest/api/window.html#arcade.Window.set_fullscreen

Set maximum screen size
https://api.arcade.academy/en/latest/api/window.html#arcade.Window.set_maximum_size

Load font
https://api.arcade.academy/en/development/api_docs/api/text.html#arcade-load-font

## Build a Platform Game in Python With Arcade – Real Python --> covers VIEWS

https://realpython.com/platformer-python-arcade/

## GUI
https://api.arcade.academy/en/latest/api/gui_widgets.html#arcade-gui-uiboxlayout

https://api.arcade.academy/en/latest/api/text_pyglet.html

UIFlatButton - 2D flat button for simple interactions (hover, press, release, click)
UITextureButton - textured button (use arcade.load_texture()) for simple interactions (hover, press, release, click)
UILabel - Simple text, supports multiline, fits content

https://api.arcade.academy/gui/concept.html

https://api.arcade.academy/en/stable/gui/concept.html

https://api.arcade.academy/examples/gui_flat_button.html

https://api.arcade.academy/en/latest/examples/gui_flat_button.html

## Miscellaneous
https://api.arcade.academy/en/latest/examples/gradients.html#gradients

https://api.arcade.academy/en/latest/tutorials/raycasting/index.html#raycasting-tutorial

## Multiple rooms / multiple questions / rounds
https://api.arcade.academy/en/latest/examples/sprite_rooms.html#sprite-rooms

## Music player including example texture buttons hovered, pressed
https://api.arcade.academy/en/latest/examples/music_control_demo.html#music-control-demo

https://api.arcade.academy/en/latest/api/window.html#arcade-schedule

## Game platformer code ideas dataclass key input handler
https://youtu.be/uI5ChUr8NVw
https://github.com/jjossie/gravity-platformer

## Huntgame views example
https://github.com/pushfoo/arcade-huntgame/blob/main/huntgame/views.py

## Arcade text positioning anchor bug
https://github.com/pythonarcade/arcade/issues/1839
