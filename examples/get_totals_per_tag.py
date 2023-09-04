from the_trivia_api_library.client import TriviaAPIClient


def main():

    #create trivia api client
    trivia_api_client = TriviaAPIClient()

    tags = trivia_api_client.get_totals_per_tag()

    for tag in tags:
        print(f"tag: {tag} -> total: {tags[tag]}")


if __name__ == '__main__':
    main()