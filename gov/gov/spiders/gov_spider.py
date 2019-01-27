import json
import scrapy


class GovSpider(scrapy.Spider):
    name = 'gov'

    def start_requests(self):
        with open('config.json', 'r') as in_:
            self.config = json.load(in_)
            self.config['pageId'] += 1

        url = f'http://www.motie.go.kr/motie/ne/presse/weekplan2/weekplanUser/weekplanView.do?title_seq_n={self.config["pageId"]}&currentPage=1&searchWord='
        yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        info_set = []
        rows = response.css('.detailTable08 > tbody > tr')
        for row in rows:
            info = {}
            tds = row.css('td::text')
            info['date'] = tds[0].extract()
            info['subject'] = tds[2].extract()
            info['distributed_date'] = tds[3].extract()
            info['depart'] = tds[4].extract()

            info_set.append(info)

        # with open('config.json', 'w') as out_:
        #     json.dump(self.config, out_)

        # import pdb; pdb.set_trace()