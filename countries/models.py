from django.db import models
from forex.models import Currency
from django.db.models import Count


class Country(models.Model):
    """
    Represents a country, such as the US, or Mexico.
    """

    name = models.CharField(max_length=255, unique=True)
    
    # The name of the country after the word "in".
    # For example, the "the" in "the United States of America"
    in_name = models.CharField(max_length=255, help_text="The name of the country after the word 'in'. Usefule for Autogeneration.")
    currency = models.ManyToManyField(Currency, help_text="Official currencies for this country. More than one currency is possible")
    symbol = models.CharField(help_text="ISO 3166-1 alpha-2 symbol", max_length=3, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'
        verbose_name = 'Country'
        ordering = ['name', ]

    def __unicode__(self):
        return u'%s' % (unicode(self.name),)


class Region(models.Model):
    """
    Represents a region, such as the Latin America, or Europe.
    """

    name = models.CharField(max_length=255, unique=True)
    country = models.ManyToManyField(Country)
    symbol = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'
        ordering = ['name', ]

    def __unicode__(self):
        return u'%s' % (unicode(self.name))


class City(models.Model):
    """
    Represents a city within a country
    """

    name = models.CharField(max_length=255)    
    symbol = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country)

    class Meta:
        verbose_name_plural = 'Cities'
        verbose_name = 'City'
        ordering = ['name', ]
        unique_together = (("name", "country"), )

    def __unicode__(self):
        return u'%s, %s' % (unicode(self.name), unicode(self.country.name))


class Government(models.Model):
    """
    Represents a government of a country, such as the
    'Government of Australia'.
    """

    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)

    class Meta:
        verbose_name_plural = 'Governments'
        verbose_name = 'Government'
        ordering = ['name', ]
        unique_together = (("name", "country"), )

    def __unicode__(self):
        return u'%s' % (unicode(self.name))
    
    
