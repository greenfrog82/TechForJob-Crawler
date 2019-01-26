import scrapy


class GovSpider(scrapy.Spider):
    name = 'gov'

    start_urls = [
        'http://www.motie.go.kr/motie/ne/presse/weekplan2/weekplanUser/weekplanView.do?title_seq_n=2897&currentPage=1&searchWord=',
    ]

    def parse(self, response):
        import pdb; pdb.set_trace()
        response.css('#idPrint > #content_box > #content > article > div > table > tbody > tr > td > table > tbody > tr')