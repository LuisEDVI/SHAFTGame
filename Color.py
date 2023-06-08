

class Color:

    Color_Off = "\u001b[0m"

    BACKGROUND_COLOR = "\033[48;2;72;72;72m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    
    BROWN = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    LIGHT_GRAY = "\033[37m"
    GRAY = "\x1b[38;2;128;128;128m"
    LIGHT_RED = "\033[31m"
    LIGHT_GREEN = "\033[32m"
    YELLOW = "\033[33m"
    LIGHT_BLUE = "\033[34m"
    LIGHT_PURPLE = "\033[35m"
    LIGHT_CYAN = "\033[36m"
    LIGHT_WHITE = "\033[37m"
    LIGHT_BLACK = "\033[90m"


    EMERALD = "\033[38;2;80;200;120m"
    GOLD = "\033[38;2;255;215;0m"
    DIAMOND = "\033[38;2;185;242;255m"
    RUBY = "\033[38;2;155;17;30m"

    SILVER = "\033[38;2;170;169;173m"
    BRONZE = "\033[38;2;205;127;50m"


    def setCor(self, color):
        self.color = color




