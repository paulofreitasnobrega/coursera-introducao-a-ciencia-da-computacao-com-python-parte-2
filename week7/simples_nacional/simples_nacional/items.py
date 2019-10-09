"""Agenda de prazos e providências do simples nacioanl."""
# -*- coding: utf-8 -*-

# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class SimplesNacionalCalendar(Item):
    """Agenda de prazos e providências do simples nacioanl."""

    title = Field()
    date_update = Field()
    deadlines = Field()
    providences = Field()
    note = Field()
