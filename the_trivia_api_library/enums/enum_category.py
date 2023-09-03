from enum import Enum

class EnumCategory(Enum):
    """
    Trivia categories.

    Attributes:
        MUSIC: Music category.
        SPORT_AND_LEISURE: Sport and leisure category.
        FILM_AND_TV: Film and TV category.
        ARTS_AND_LITERATURE: Arts and literature category.
        HISTORY: History category.
        SOCIETY_AND_CULTURE: Society and culture category.
        SCIENCE: Science category.
        GEOGRAPHY: Geography category.
        FOOD_AND_DRINK: Food and drink category.
        GENERAL_KNOWLEDGE: General knowledge category.
    """

    MUSIC = "music"
    SPORT_AND_LEISURE = "sport_and_leisure"
    FILM_AND_TV = "film_and_tv"
    ARTS_AND_LITERATURE = "arts_and_literature"
    HISTORY = "history"
    SOCIETY_AND_CULTURE = "society_and_culture"
    SCIENCE = "science"
    GEOGRAPHY = "geography"
    FOOD_AND_DRINK = "food_and_drink"
    GENERAL_KNOWLEDGE = "general_knowledge"