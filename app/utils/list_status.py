from enum import Enum


class StatusType(str, Enum):
    pending = "pending"
    ongoing = "ongoing"
    done = "done"