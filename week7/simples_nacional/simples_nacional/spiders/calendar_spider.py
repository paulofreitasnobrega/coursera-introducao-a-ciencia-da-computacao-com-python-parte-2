"""Spider - agenda do simples nacional."""

from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from simples_nacional.items import SimplesNacionalCalendar


class CalendarSpider(CrawlSpider):
    """Spider - agenda do simples nacional."""

    name = "calendar"
    start_urls = [
        "http://www8.receita.fazenda.gov.br/SimplesNacional/"
    ]

    def parse(self, response):
        """Realiza o parse do body da página web."""
        sel = Selector(response)
        url = sel.xpath("//img[@alt='Agenda']/parent::a//@href").extract()
        url = response.url + url[0]

        yield Request(url, self.parse_calendar)

    def parse_calendar(self, response):
        """Realiza o parse da agenda."""
        sel = Selector(response)

        # minerando os elementos
        note = sel.xpath("//p[@id='observacao']//text()").extract()
        title = sel.xpath("//div[@id='agenda']//h1//text()").extract()
        deadlines = sel.xpath("//td//span[@class='prazo']//text()").extract()
        date_update = sel.xpath("//div[@id='atualizado']//text()").extract()
        providences = sel.xpath("//tr//td//p//span//text()").extract()

        # gerando o modelo
        calendar = SimplesNacionalCalendar()
        calendar['title'] = title[0]
        calendar['date_update'] = "".join(date_update)
        calendar['note'] = note[2]
        calendar['deadlines'] = deadlines
        calendar['providences'] = providences

        self.print_calendar(calendar)

    def print_calendar(self, calendar):
        """Imprime o calendário."""
        print("----------------------------------------")
        print("{}\n{}\n\n".format(calendar['title'], calendar['date_update']))
        print("Prazos e Providências:")

        for i, providence in enumerate(calendar['providences']):
            print("{}: {}".format(calendar['deadlines'][i], providence))

        print("\n\nAtenção: {}".format(calendar['note']))
        print("----------------------------------------")
