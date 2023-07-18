# Example with 3 views

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
        self.manager = arcade.gui.UIManager()

    def build_ui(self, view, views):
        button_1 = arcade.gui.UIFlatButton(text="View 1", width=100)
        button_2 = arcade.gui.UIFlatButton(text="View 2", width=100)
        button_3 = arcade.gui.UIFlatButton(text="View 3", width=100)
        text_label = arcade.gui.UILabel(text=view, align="center", font_size=20, multiline=False)

        # Initialise the buttons with an on_click event.
        @button_1.event("on_click")
        def on_click_button_1(event):
            self.window.show_view(views.view_1)

        @button_2.event("on_click")
        def on_click_button_2(event):
            self.window.show_view(views.view_2)

        @button_3.event("on_click")
        def on_click_button_3(event):
            self.window.show_view(views.view_3)

       # Initialise a grid in which widgets can be arranged.
        self.grid = arcade.gui.UIGridLayout(column_count=5, row_count=1, horizontal_spacing=20, vertical_spacing=20)

        # Adding the buttons to the layout.
        self.grid.add(button_1, col_num=0, row_num=0)
        self.grid.add(button_2, col_num=1, row_num=0)
        self.grid.add(button_3, col_num=2, row_num=0)
        self.grid.add(text_label, col_num=3, row_num=0)


        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        self.anchor.add(anchor_x="center_x", anchor_y="center_y", child=self.grid)

    def on_show_view(self):
        """ This is run every time when we switch to this view """
        arcade.set_background_color(arcade.color.SAND)

        # Enable the UIManager when the view is shown.
        self.manager.enable()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

        # Draw the manager.
        self.manager.draw()


def create_viewport_window():

    # Screen title and size
    width = 800
    height = 600
    title = "Making a Menu"

    app_window = arcade.Window(width, height, title,
                           center_window=False, resizable=True, visible=True, antialiasing=False)
    return app_window

def main():

    # Create the viewport window
    app_window = create_viewport_window()

    # Create a dictionary of all the views and view objects
    views = Views_dict()

    # Initialise the views and add the objects to the views dictionary
    views.view_1 = SlideView()
    views.view_2 = SlideView()
    views.view_3 = SlideView()

    # Build up the UI in each view
    # This is done after initialising all views so that a dictionary
    # of all views can be passed along to the class

    views.view_1.build_ui('view_1', views)
    views.view_2.build_ui('view_2', views)
    views.view_3.build_ui('view_3', views)

    app_window.show_view(views.view_1)

    # Start the arcade event loop
    arcade.run()


if __name__ == "__main__":
    main()