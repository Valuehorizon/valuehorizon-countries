from django.db import models
from forex.models import Currency
from django.db.models import Count


class Country(models.Model):
    """
    Represents a country, such as the US, or Mexico.
    """

    name = models.CharField(max_length=255, unique=True, help_text="Official Country name")
    common_name = models.CharField(max_length=255, blank=True, null=True, help_text="Common Country name")
    in_name = models.CharField(max_length=255, help_text="The name of the country after the word 'in'. Useful for Autogeneration.")
    currency = models.ManyToManyField(Currency, help_text="Official currencies for this country. More than one currency is possible")
    symbol_alpha2_code = models.CharField(help_text="ISO 3166-1 alpha-2 symbol", max_length=2, unique=True)
    symbol_alpha3_code = models.CharField(help_text="ISO 3166-1 alpha-3 symbol", max_length=3, blank=True, null=True)
    
    ISO_STATUS_CHOICES = (
        (u'EXR', u'Exceptionally reserved'),
        (u'FRU', u'Formerly used'),
        (u'INR', u'Indeterminately reserved'),
        (u'OFF', u'Officially assigned'),
        (u'TRR', u'Transitionally reserved'),
        (u'UND', u'Unassigned'),
    )
    iso_status = models.CharField(max_length = 3, choices = ISO_STATUS_CHOICES, default="UND")    

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
    
    
