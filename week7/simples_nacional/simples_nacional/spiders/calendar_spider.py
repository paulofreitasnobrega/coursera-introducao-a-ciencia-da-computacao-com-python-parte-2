"""Spider - agenda do simples nacional."""

from scrapy.selector import Selector
from simples_nacional.items import SimplesNacionalCalendar
from scrapy.spiders import CrawlSpider


class CalendarSpider(CrawlSpider):
    """Spider - agenda do simples nacional."""

    name = "calendar"
    u = "http://www8.receita.fazenda.gov.br/SimplesNacional/Agenda/Agenda.aspx"
    start_urls = [u]

    def parse(self, response):
        """Realiza o parse do body da página web."""
        sel = Selector(response)

        title = sel.xpath("//div[@id='agenda']//h1//text()").extract()[0]
        date_update = sel.xpath("//div[@id='atualizado']//text()").extract()[0]
        note = sel.xpath("//p[@id='observacao']//text()").extract()[0]
        deadlines = sel.xpath("//td//span[@class='prazo']//text()").extract()
        providences = sel.xpath("//tr//td//p//span//text()").extract()

        calendar = SimplesNacionalCalendar()
        calendar['title'] = title
        calendar['date_update'] = date_update
        calendar['note'] = note
        calendar['deadlines'] = deadlines
        calendar['providences'] = providences

        self.print_item(calendar)

    def print_item(self, calendar):
        """Imprime o calendário."""
        for k, v in calendar.items():
            print("{} : {}".format(k, v))
        print("--------------------")
