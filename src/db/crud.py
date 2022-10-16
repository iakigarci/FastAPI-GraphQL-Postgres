import csv
from typing import Dict, Optional

class Crud:

    def __init__(self):
        pass

    # function to get all data from a ad.csv file and return as a json 
    def get_all_data(self) -> list:
        try:
            with open('db/ad.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                data = []
                for row in reader:
                    data.append(row)
                return data
        except:
            raise Exception("File not found or not data found")
    # function to get an a specific ad by id from ad.csv file and return as a json
    def get_ad(self, id: int) -> Dict:
        for ad in self.get_all_data():
            if ad['id'] == str(id):
                return ad
        return {}

    # function to get an a specific page by term, per_page and page from ad.csv file and return as a json
    def get_page(self, term: str, per_page: int, page: int) -> Dict[str, Optional[str]]:
        data = self.get_all_data()
        ads = [ad for ad in data if term.lower() in ad['name'].lower()]
        page_result = ads[per_page*(page-1):per_page*page]
        return page_result  # type: ignore