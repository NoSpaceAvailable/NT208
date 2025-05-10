from enum import Enum

class ItemRarity(Enum):
    # the value is the hex color, 
    # which will be used at frontend to show the rarity of a skin
    INDUSTRIAL  =   "4B69FF"
    MIL_SPEC    =   "8847FF"
    RESTRICTED  =   "D32CE6"
    CLASSIFIED  =   "EB4B4B"
    COVERT      =   "FFD700"
