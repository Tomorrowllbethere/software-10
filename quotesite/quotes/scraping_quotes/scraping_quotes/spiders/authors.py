import scrapy
from main import run_process

class AuthorsSpider(scrapy.Spider):
        name = "authors"
        allowed_domains = ["quotes.toscrape.com"]
        start_urls = ["https://quotes.toscrape.com"]
        custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}

        def parse(self, response):
        # Знаходимо всі посилання в контейнері div
                for quote in response.xpath("/html//div[@class='quote']"): 
                        link = quote.xpath("span//a/@href").get()
                        yield response.follow(link, self.parse_author)

                next_link = response.xpath("//li[@class='next']/a/@href").get()
                if next_link:
                        yield scrapy.Request(url=self.start_urls[0] + next_link)

        def parse_author(self, response):
        # Обробка інформації про автора
                author_name = response.xpath("//h3/text()").get()
                author_birthdate = response.xpath("//p/span/text()").get()
                author_birth_location = response.xpath("//p/span[@class='author-born-location']/text()").get()
                author_desc = response.xpath("//div[@class='author-description']/text()").get()
                
        # Збереження результатів
                yield {
                "fullname": author_name.strip(),
                "born_date": author_birthdate.strip(),
                "born_location": author_birth_location.strip(),
                "description": author_desc.strip()
                }
if __name__=="__main__":
        run_process(AuthorsSpider)
