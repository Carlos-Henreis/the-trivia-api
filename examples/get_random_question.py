from the_trivia_api_library import TriviaAPIClient, EnumCategory, EnumDifficulty

def main():

    #create trivia api client
    trivia_api_client = TriviaAPIClient()

    #create category list
    categories = [EnumCategory.MUSIC.value, EnumCategory.GEOGRAPHY.value, EnumCategory.GENERAL_KNOWLEDGE.value]
    #Create difficulty list
    difficulties = [EnumDifficulty.EASY.value, EnumDifficulty.MEDIUM.value]


    # get random question
    response = trivia_api_client.get_random_question(limit=5, categories=categories, difficulties=difficulties)

    print(response)
    print(len(response))


if __name__ == '__main__':
    main()