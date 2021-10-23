import json # TEMP - Debug
import os, requests
from http import client

class scripture_api:
    # Constructor
    def __init__(self):
        self.api_key = ""

    # Tests and sets api_key
    def authenticate(self, api_key):
        # Request
        URL = "https://api.scripture.api.bible/v1/bibles"
        HEADERS = {'api-key': api_key}
        status_code = requests.get(url = URL, headers=HEADERS).status_code

        # Verify by status code
        if (status_code == 200):
            print("API key is valid!\n") # TEMP - Debug
            self.api_key = api_key;
        elif (status_code == 500):
            raise ValueError(f"Error, Invalid API key! ('{api_key}')")
        else:
            raise Exception(f"Error while authenticating, Unknown status code '{status_code}'!")

    # Check if API has api_key
    def __check_key(self):
        if (self.api_key == ""):
            raise ValueError("Error, API key not found! (Make sure you have authenticated the API)")
        else:
            print()
            return True

    # Lists bibles
    #   [language_code] Filters bibles by language
    def list_bibles(self, language_code = None):
        self.__check_key()

        # Set language
        language = ""
        if (language_code != None):
            if (len(language_code) == 3):
                language = f"?language={language_code}"
            else:
                raise ValueError("Error, Invalid language code! (A language code is 3 characters)")

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles{language}"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json()

    # Lists books of specified bible
    def list_books(self, bible_id):
        self.__check_key()

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles/{bible_id}/books"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json()

    # TEMP - Add docs
    # Searches bible for relavant verses
    #   [query] # comment about wildcards and only one word
    #   [limit]
    #   [fuzziness] # Explain fuzziness values
    def search(self, bible_id, query, limit = 10, fuzziness = "AUTO"):
        self.__check_key()

        # Set query
        if (len(query.split(' ')) != 1):
            raise ValueError(f"Error, Query can only contain one word! (Contains {len(query.split(' '))} words)")
        elif (query == ""):
            raise ValueError(f"Error, Query cannot be empty!")

        # Set limit (Between 1-100)
        if (limit < 1):
            raise ValueError(f"Error, Limit cannot be less than 0! ('{limit}')")
        elif (limit > 100):
            raise ValueError(f"Error, Limit cannot be more than 100! ('{limit}')")

        # Set fuzziness (Accounts for misspellings)
        if not (fuzziness == "AUTO" or fuzziness == "0" or fuzziness == "1" or fuzziness == "2"):
            raise ValueError(f"Error, Invalid fuzziness value! ('{fuzziness}') (Options are 'AUTO', '0', '1' and '2')")

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles/{bible_id}/search?query={query}&limit={limit}&fuzziness={fuzziness}"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json()

# TEMP - Testing
def main():
    os.chdir("models/") # Change directory to "models/"

    # Retrieve API key
    api_key = ""
    with open("api_key.txt", "r") as api_key_file:
        lines =  api_key_file.readlines() # Read file

        # Validate file content
        if (len(lines) == 0):
            raise Exception(f"Error, API key not found! (\"{os.getcwd()}/api_key.txt\")")
        elif (len(lines) > 1):
            if (lines[1] != ""):
                raise  Exception(f"Error, API key cannot be across multiple lines! (\"{os.getcwd()}/api_key.txt\")")

        api_key = lines[0] # Access API key
    print(f"API key found! ('{api_key}')") # TEMP - Debug


    # TEMP - Debug
    api_test = scripture_api()
    api_test.authenticate(api_key)
    bible_id = '65eec8e0b60e656b-01' # Free Bible Version
    # TEMP - Debug
    # response = api_test.list_bibles("eng")
    # response = api_test.list_books(bible_id)
    response = api_test.list_books(bible_id)
    print(f"Response:\n{json.dumps(response, indent=4, sort_keys=True)}")

if __name__ == '__main__':
    main()