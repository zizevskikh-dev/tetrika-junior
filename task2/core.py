from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.parse import urljoin



# from config import WebdriverConfig


# class WikiAnimalParser:
#     def __init__(self):
#         self.driver = WebdriverConfig().DRIVER
#         self.start_page = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
#         self.animals_xpath='//div[@class="mw-category mw-category-columns"]//li'
#         self.next_page_xpath='//a[text()="Следующая страница"]'
#         self.animals = set()
#
#     def run(self):
#         self.driver.get(self.start_page)
#         self._inspect_page()
#
#     def _inspect_page(self):
#         li_elements = self.driver.find_elements("xpath", self.animals_xpath)
#
#         for li_element in li_elements:
#             animal_name = li_element.text
#             self.animals.add(animal_name)
#
#         print(len(self.animals))
#
#         next_page_link = self.driver.find_element("xpath",self.next_page_xpath)
#         next_page_link.click()
#
#         self._inspect_page()


class WikiAnimalParser:
    def __init__(self):
        self.home_page = "https://ru.wikipedia.org/"
        self.data = []

    def run(self):
        start_page_suffix = "w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
        start_page_url = urljoin(self.home_page, start_page_suffix)
        self._scan_wiki(url_to_parse=start_page_url)
        animals_report = self.group_animals_by_first_letter()
        self.write_report_to_csv(animals_report)

    def _scan_wiki(self, url_to_parse):
        page_html = requests.get(url=url_to_parse).text
        soup = BeautifulSoup(page_html, 'lxml')
        li_elements = soup.select('div.mw-category.mw-category-columns li')

        for li in li_elements:
            animal_name = li.a['title'].capitalize()
            first_letter = animal_name[0]
            data = {'First Letter': first_letter, 'Animal name': animal_name}
            self.data.append(data)

        next_page = soup.find('a', string="Следующая страница")
        if next_page:
            next_page_suffix = next_page['href']
            next_page_url = urljoin(self.home_page, next_page_suffix)
            self._scan_wiki(url_to_parse=next_page_url)

    def group_animals_by_first_letter(self):
        df = pd.DataFrame(self.data)
        query = df.groupby(['First Letter']).count().reset_index(names=['First Letter', 'Total Amount'])
        return query

    @staticmethod
    def write_report_to_csv(df):
        df.to_csv('report.csv', encoding='utf-8', index=False, header=False)
