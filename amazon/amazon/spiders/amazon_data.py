import scrapy
from ..items import AmazonItem
class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.amazon.com/kindle-dbs/browse/?_encoding=UTF8&pd_rd_w=rXAnE&content-id=amzn1.sym.bb33addf-488a-4e99-909f-3acc87146400&pf_rd_p=bb33addf-488a-4e99-909f-3acc87146400&pf_rd_r=WWBK0C5QM2PBEEKB3FH7&pd_rd_wg=gyMfk&pd_rd_r=d14213c4-c197-4c81-ad8e-30c44d59ed36&ref_=ts&widgetId=unified-ebooks-storefront-default_TopSellersStrategy&title=Best%20sellers%20&ref_=books_storefront_desktop_mfs_ts&sourceType=RECS&page=1&pd_rd_w=rXAnE&content-id=amzn1.sym.bb33addf-488a-4e99-909f-3acc87146400&pf_rd_p=bb33addf-488a-4e99-909f-3acc87146400&pf_rd_r=WWBK0C5QM2PBEEKB3FH7&pd_rd_wg=gyMfk&pd_rd_r=d14213c4-c197-4c81-ad8e-30c44d59ed36&metadata=%24deviceID%3A%24deviceFormFactor%3Alarge%24deviceAppType%3ADESKTOP%24deviceTypeID%3A%24deviceFamily%3A%24deviceSurfaceType%3Adesktop%24cardAppType%3ADESKTOP%24cardSurfaceType%3Adesktop%24cardMobileOS%3AUnknown%24sidekickLocale%3Aen-US%24locale%3Aen-US%24clientRequestId%3AWWBK0C5QM2PBEEKB3FH7%24multiFormatWidgetSpClickUrlType%3Adefault'
    ]

    def parse(self, response):
        items = AmazonItem()
        raw_prices = response.css('span.browse-larger-text-one-line::text').getall()

        raw_names = response.css('span.a-color-price.a-text-bold::text').extract()
        raw_ratings = response.xpath('//span[contains(@class, "a-size-small") and contains(@class, "a-color-secondary")]/text()').re(r'\((\d+)\)')
        raw_ranks = response.xpath('//span[contains(@class, "p13n-amz-charts-qualifier-text")]/text()').re(r'#(\d+)')
        yield {
            'product_name': raw_names,
            'price': raw_prices,
            'ratings': raw_ratings,
            'rank_text': raw_ranks,
        }

        if AmazonSpider.page_number <= 10:
            AmazonSpider.page_number += 1
            next_page = f'https://www.amazon.com/kindle-dbs/browse/...&page={AmazonSpider.page_number}'  # shortened here
            yield response.follow(next_page, callback=self.parse)
