from enum import Enum

class ItemRarity(Enum):
    # the value is the hex color, 
    # which will be used at frontend to show the rarity of a skin
    INDUSTRIAL  =   "1"
    MIL_SPEC    =   "2"
    RESTRICTED  =   "3"
    CLASSIFIED  =   "4"
    COVERT      =   "5"
