# Example with 3 views that supports resizing of the viewport
#
# For Windows only, set DPI awareness to handle
# high resolution displays.
#
# import ctypes
# ctypes.windll.shcore.SetProcessDpiAwareness(2)

import arcade
import arcade.gui

class Views_dict(dict):
    """Store the mapping between view name and view object"""

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

class SlideView(arcade.View):
    """This is a general slide view class"""

    def __init__(self):
        super().__init__()

        # Add a GUI manager to manage the buttons
        self.manager = arcade.gui.UIManager()

    def build_ui(self, background_color, view, views):
        self.view = view
        self.background_color = background_color

        # Display the active view
        self.txt = arcade.Text(text=view, start_x=300, start_y=550, color=(0,0,0), bold=True,
                               anchor_x='left', anchor_y='top', font_size=80)

        self.button_1 = arcade.gui.UIFlatButton(text="View 1", width=100)
        self.button_2 = arcade.gui.UIFlatButton(text="View 2", width=100)
        self.button_3 = arcade.gui.UIFlatButton(text="View 3", width=100)

       # Initialise the buttons with an on_click event.
        @self.button_1.event("on_click")
        def on_click_button_1(event):
            self.window.show_view(views.view_1)

        @self.button_2.event("on_click")
        def on_click_button_2(event):
            self.window.show_view(views.view_2)

        @self.button_3.event("on_click")
        def on_click_button_3(event):
            self.window.show_view(views.view_3)
            # re-position the text elements
            self.txt.start_x = 100  # .on_resize(window.width, window.height) start_x=300, start_y=550
            self.txt.text = "Yeah"
            self.txt.draw()

       # Initialise a grid in which widgets can be arranged.
        self.grid = arcade.gui.UIGridLayout(column_count=3, row_count=1, horizontal_spacing=20, vertical_spacing=20)

        # Adding the buttons to the layout.
        self.grid.add(self.button_1, col_num=0, row_num=0)
        self.grid.add(self.button_2, col_num=1, row_num=0)
        self.grid.add(self.button_3, col_num=2, row_num=0)

        # Create an anchor for the layout
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        # Position the anchor
        self.anchor.add(anchor_x="center", anchor_y="bottom", child=self.grid)
        # anchor_x: Horizontal anchor. Valid options are ``left``, ``right``, and ``center``.
        # align_x: Offset or padding for the horizontal anchor.
        # anchor_y: Vertical anchor. Valid options are ``top``, ``center``, and ``bottom``.
        # align_y: Offset or padding for the vertical anchor.

    def on_show_view(self):
        """ This is run every time when we switch to this view """
        arcade.set_background_color(self.background_color)
        self.manager.enable()

        # re-position the GUI elements in case the viewport was resized
        window = arcade.get_window()
        self.manager.on_resize(window.width, window.height)

    def on_hide_view(self):

        # Disable the UIManager when the view is hidden
        self.manager.disable()

    def on_resize(self, width: int, height: int):
        pass

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

        # Draw the text
        self.txt.draw()

        # Draw the GUI manager including all buttons
        self.manager.draw()

def setup_app():
    width = 800
    height = 600

    # Create the app window
    app_window = arcade.Window(width, height, "Views example", resizable=True)
    # Additional properties: center_window = False, resizable = True, visible = True, antialiasing = False

    # Create a dictionary of all the views and view objects
    views = Views_dict()

    # Initialise the views and add the objects to the views dictionary
    views.view_1 = SlideView()
    views.view_2 = SlideView()
    views.view_3 = SlideView()

    # Build up the UI in each view
    # A dictionary of all views is passed to each view object
    # so that the buttons in each slide can refer to the views

    views.view_1.build_ui(arcade.color.DARK_BLUE_GRAY, 'View 1', views)
    views.view_2.build_ui(arcade.color.ARMY_GREEN, 'View 2', views)
    views.view_3.build_ui(arcade.color.KOBE, 'View 3', views)

    # Show the first view
    app_window.show_view(views.view_1)

def main():

    # Create viewport and views
    setup_app()

    # Start the arcade event loop
    arcade.run()


if __name__ == "__main__":
    main()