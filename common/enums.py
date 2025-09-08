from enum import Enum, unique, auto

@unique
class LOADING_STATE(Enum):
    IDLE = auto()
    INIT = auto()
    FETCHMORE = auto()
    LOADING = auto()
    SUBMIT = auto()

#USAGE
# print(Color.IDLE)        
# print(Color.IDLE.name)   
# print(Color.IDLE.value)  