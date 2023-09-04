from the_trivia_api_library import TriviaAPIClient

def main():

        #create trivia api client
        trivia_api_client = TriviaAPIClient()

        # get random question
        response = trivia_api_client.get_all_tags()

        print(response)


if __name__ == '__main__':
    main()