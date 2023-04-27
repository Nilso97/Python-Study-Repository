import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for movies in response.css('.titleColumn'):
            yield{
                'title': movies.css('.titleColumn a::text').get(),
                'release_year': movies.css('.secondaryInfo::text').get()[1:-1],
                'movie_review': response.css('strong::text').get()
            }
        pass