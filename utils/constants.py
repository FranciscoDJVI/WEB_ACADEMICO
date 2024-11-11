from enum import Enum


class Display(Enum):
    VERY_SMALL = "8vh"
    SMALL = "10vh"
    MEDIUN = "20vh"
    LARGE = "50vh"


class FontSize(Enum):
    VERY_SMALL = "0.7rem"
    SMALL = "1.5rem"
    MEDIUN = "5.5rem"
    LARGE = "10rem"


class FontFamily(Enum):
    CURSIVE = "cursive"
    VERDANA = "verdana"
    ARIAL = "arial"
    TIMES = "times"
    GEORGIA = "georgia"


class Border(Enum):
    MINIMUN = "50%"
    MAXIMUN = "100%"
