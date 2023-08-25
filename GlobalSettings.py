import pygame
import pygame_menu
from pygame_menu import Theme

from GameState import GameState

COLORS = {
    "WHITE": [255, 255, 255],
    "GREY": [127, 127, 127],
    "CRIMSON": [154, 0, 0],
    "BLACK": [0, 0, 0],
    "DARK_YELLOW": [102, 102, 0],
    "DARK_BLUE": [0, 0, 153]
}

WINDOW_HEIGHT: int = 1280
WINDOW_WIDTH: int = 720
MENU_ENTRIES_FONT_SIZE: int = 80

MAIN_MENU_IMAGE = pygame_menu.baseimage.BaseImage(
    image_path="Resources/main_menu_background.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)

MAIN_MENU_THEME = Theme(background_color=MAIN_MENU_IMAGE,
                        widget_font_color=COLORS["BLACK"],
                        widget_font_size=MENU_ENTRIES_FONT_SIZE,
                        selection_color=COLORS["WHITE"],
                        widget_selection_effect=pygame_menu.widgets.LeftArrowSelection(),
                        widget_font="Resources/halfelvenboldital.ttf",
                        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
