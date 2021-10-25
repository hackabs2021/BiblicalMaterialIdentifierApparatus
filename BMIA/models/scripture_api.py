import os, requests, json

class scripture_api:
    global suffixes
    suffixes = [
        "able",
        "age",
        "al",
        "ance",
        "ate",
        "dom",
        "ed",
        "ee",
        "en",
        "ence",
        "er",
        "ese",
        "ful",
        "hood",
        "i",
        "ian",
        "ible",
        "ic",
        "ify",
        "ing",
        "ion",
        "ise",
        "ish",
        "ism",
        "ist",
        "ity",
        "ive",
        "ize",
        "less",
        "ly",
        "ment",
        "ness",
        "or",
        "ous",
        "ry",
        "s",
        "ship",
        "sion",
        "tion",
        "ty",
        "ward",
        "wards",
        "wise",
        "xion",
        "y"
    ]

    # Constructor
    def __init__(self):
        self.api_key = ""
        self.bible_id = ""
        self.book_codes = {}

    # Tests and sets api_key
    def authenticate(self, api_key: str) -> None:
        # Request
        URL = "https://api.scripture.api.bible/v1/bibles"
        HEADERS = {'api-key': api_key}
        status_code = requests.get(url = URL, headers=HEADERS).status_code

        # Verify by status code
        if (status_code == 200):
            self.api_key = api_key;
        elif (status_code == 500):
            raise ValueError(f"Error, Invalid API key! ('{api_key}')")
        else:
            raise Exception(f"Error while authenticating, Unknown status code '{status_code}'!")

    # Check if class has api_key and bible_id
    def __check_values(self) -> bool:
        if (self.api_key == ""):
            raise ValueError("Error, API key not found! (Make sure you have authenticated the API)")
        elif (self.bible_id == ""):
            raise ValueError("Error, Bible ID not found! (Make sure you have set the Bible)")
        else:
            return True

    # Lists bibles
    #   [language_code] Filters Bibles by language (English is "eng")
    #
    #   Returns: Array of Bibles
    def list_bibles(self, language_code: str = None):
        self.__check_values()

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
        return requests.get(url=URL, headers=HEADERS).json() # Return bibles

    # Lists books of the specified bible
    #   Returns: Array of books
    def list_books(self):
        self.__check_values()

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles/{self.bible_id}/books"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json() # Return books

    # Changes bible
    #   [bible_id] Id of the Bible you want to select (https://docs.api.bible/guides/bibles)
    def set_bible(self, bible_id: str) -> None:
        self.bible_id = bible_id # Update bible_id

        response = self.list_books() # Retrieve books

        # Check that response was successful
        if "data" not in response:
            raise ValueError(f"Error, Invalid Bible ID! ('{bible_id}')")

        self.book_codes = {} # Clear book_codes

        # Update book codes
        for book in response["data"]:
            self.book_codes[book["name"]] = book["abbreviation"]

    # Searches bible for verses that match query
    #   [bible_id]: The Bible you want to search in
    #   [query]: Wildcards are '?' for single a character and '*' for multiple characters
    #   [limit]: Between 1-100
    #   [fuzziness]: Accounts for misspellings. Options are 'AUTO', '0', '1' and '2'
    #
    #   Returns: Array of verses
    def search(self, query: str, limit: int = 10, fuzziness: str = "AUTO"):
        self.__check_values()

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
        URL = f"https://api.scripture.api.bible/v1/bibles/{self.bible_id}/search?query={query}&limit={limit}&fuzziness={fuzziness}"
        HEADERS = {'api-key': self.api_key}
        response = requests.get(url=URL, headers=HEADERS).json()

        # Response was unsuccessful
        if "data" not in response:
            return None

        return response["data"]["verses"] # Return verses

    # Lists verses from chapter
    #   [book] Book of the Bible
    #   [chapter] Chapter to list verses from
    #
    #   Returns: Array of verses
    def list_verses(self, book: str, chapter: int):
        self.__check_values()

        # Validate book
        if book not in self.book_codes:
            raise ValueError(f"Error, Book not found! (\"{book}\")")

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles/{self.bible_id}/chapters/{self.book_codes[book]}.{chapter}/verses"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json() # Return books

    # Gets verse from Bible
    #   [book] Book of the Bible
    #   [chapter] Chapter verse is from
    #   [verse] Verse
    #
    #   Returns: The verse
    def get_verse(self, book: str, chapter: int, verse: int):
        self.__check_values()

        # Validate book
        if book not in self.book_codes:
            raise ValueError(f"Error, Book not found! (\"{book}\")")

        # Request
        URL = f"https://api.scripture.api.bible/v1/bibles/{self.bible_id}/verses/{self.book_codes[book]}.{chapter}.{verse}?content-type=json"
        HEADERS = {'api-key': self.api_key}
        return requests.get(url=URL, headers=HEADERS).json()  # Return books

    # Replaces suffix with wildcard ('*')
    #   [word] Word to remove suffix from
    #
    #   Returns: Word with suffix replaced
    def replace_suffix_with_wildcard(word:str) -> str:
        # Find and replace suffix
        for suffix in suffixes:
            if (word.endswith(suffix)):
                return f"{word[:-len(suffix)]}*"

        return f"{word}*" # If no suffix just add wildcard

# Gets API key from file
def retrieve_api_key():
    CURRENT_DIRECTORY = os.path.dirname((os.path.realpath(__file__)))

    api_key = ""
    with open(CURRENT_DIRECTORY + "/api_key.txt", "r") as api_key_file:
        lines =  api_key_file.readlines() # Read file

        # Validate file content
        if (len(lines) == 0):
            raise Exception(f"Error, API key not found! (\"{os.getcwd()}/api_key.txt\")")
        elif (len(lines) > 1):
            if (lines[1] != ""):
                raise  Exception(f"Error, API key cannot be across multiple lines! (\"{os.getcwd()}/api_key.txt\")")

        api_key = lines[0] # Access API key

    print(f"API key found! ('{api_key}')\n") # TEMP - Debug
    return api_key

# For testing
def main():
    api_key = retrieve_api_key()

    # Setup
    api_test = scripture_api()
    api_test.authenticate(api_key)
    # api_test.set_bible('65eec8e0b60e656b-01') # Free Bible Version
    api_test.set_bible('de4e12af7f28f599-01') # King James (Authorised) Version

    ## Tests
    # response = api_test.list_bibles("eng")["data"]
    # response = api_test.list_books()["data"]
    # response = api_test.search("worry", limit = 3, fuzziness = "0")
    # response = api_test.list_verses("John", 11)["data"]
    # response = api_test.get_verse("John", 11, 35)["data"]["content"][0]["items"][1]

    print(scripture_api.replace_suffix_with_wildcard("Peace"))
    # print(f"Response:\n{json.dumps(response, indent=4, sort_keys=True)}")

if __name__ == '__main__':
    main()
