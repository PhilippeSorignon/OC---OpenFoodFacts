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
        i_int = 0
        for i in answer:
            if 'product_name' in i and 'nutrition_grades' in i \
            and 'url' in i and 'stores_tags' in i and self.is_product_saved(i['product_name']):
                self.name.append(i['product_name'])
                self.nutri_score.append(i['nutrition_grades'])
                self.url.append(i['url'])
                self.stores.append([])
                for current_store in range(len(i['stores_tags'])):
                    self.stores[i_int].append(i['stores_tags'][current_store])
                i_int += 1

    def is_product_saved(self, check):
        """Check if the name is already saved

        Return  True if the name is not saved
        Return False if the name is already saved"""
        state = True
        for i in range(len(self.name)):
            if check == self.name[i]:
                state = False
        return state
