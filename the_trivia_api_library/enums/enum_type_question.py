from enum import Enum

class EnumTypeQuestion(Enum):
    """
    Trivia type question.

    Attributes:
        TEXT_CHOICE: Text choice.
        IMAGE_CHOICE: Image choice.
    """
    TEXT_CHOICE = "text_choice"
    IMAGE_CHOICE = "image_choice"