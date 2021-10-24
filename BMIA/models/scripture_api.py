import os, requests

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

    # Lists books of the specified bible
    #   [bible_id] The bible you want the books from
    def list_books(self, bible_id):
        self.__check_key()

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles/{bible_id}/books"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json()

    # Searches bible for verses that match query
    #   [bible_id] The bible you want to search in
    #   [query] Wildcards are '?' for single a character and '*' for multiple characters
    #   [limit] Between 1-100
    #   [fuzziness] Accounts for misspellings. Options are 'AUTO', '0', '1' and '2'
    def search(self, bible_id, query, limit = 10, fuzziness = "AUTO"):
        self.__check_key()

        # Set query
        if (query == ""):
            raise ValueError(f"Error, Query cannot be empty!")

        # Set limit
        if (limit < 1):
            raise ValueError(f"Error, Limit cannot be less than 0! ('{limit}')")
        elif (limit > 100):
            raise ValueError(f"Error, Limit cannot be more than 100! ('{limit}')")

        # Set fuzziness
        if not (fuzziness == "AUTO" or fuzziness == "0" or fuzziness == "1" or fuzziness == "2"):
            raise ValueError(f"Error, Invalid fuzziness value! ('{fuzziness}') (Options are 'AUTO', '0', '1' and '2')")

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles/{bible_id}/search?query={query}&limit={limit}&fuzziness={fuzziness}"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json()
