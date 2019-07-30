import requests

BASE_URL = 'https://world.openfoodfacts.org/cgi/search.pl'

class Api:
    """Get and sort API data"""

    def __init__(self, cat):
        """Initialisation"""
        self.category = cat
        self.name = []
        self.nutri_score = []
        self.url = []
        self.stores = []
        self.payload = {"action" : "process", "page_size" : "50", "tagtype_0" : "categories",\
        "tag_contains_0" : "contains", "tag_0" : self.category, "tagtype_1" : "countries",\
        "tag_contains_1" : "contains", "tag_1" : "France", "json": "1"}

    def get_data(self):
        """Make the API call and save the data"""
        answer = requests.get(BASE_URL, params=self.payload).json()['products']
        current_int = 0
        for current in answer:
            if 'product_name' in current and 'nutrition_grades' in current \
            and 'url' in current and 'stores_tags' in current \
            and self.is_product_saved(current['product_name']):
                self.name.append(current['product_name'])
                self.nutri_score.append(current['nutrition_grades'])
                self.url.append(current['url'])
                self.stores.append([])
                for current_store in range(len(current['stores_tags'])):
                    self.stores[current_int].append(current['stores_tags'][current_store])
                current_int += 1

    def is_product_saved(self, check):
        """Check if the name is already saved

        Return  True if the name is not saved
        Return False if the name is already saved"""
        state = True
        for i in range(len(self.name)):
            if check == self.name[i]:
                state = False
        return state
