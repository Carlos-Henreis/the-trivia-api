from the_trivia_api_library.client import TriviaAPIClient
from the_trivia_api_library.enums.enum_category import EnumCategory



def main():

    #create trivia api client
    trivia_api_client = TriviaAPIClient()

    #create category list
    #categories = [EnumCategory.MUSIC.value, EnumCategory.GEOGRAPHY.value, EnumCategory.GENERAL_KNOWLEDGE.value]

    # get random question
    response = trivia_api_client.get_random_question(limit=45)

    print(response)
    print(len(response))


if __name__ == '__main__':
    main()

