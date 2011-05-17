from django.db import models
from decimal import Decimal
import settings

class Currency(models.Model):
    name   = models.CharField(max_length=16)
    code   = models.CharField(max_length=3) 

    class Meta:
        unique_together = (('name','code'), )

    def __unicode__(self):
        return unicode(self.name)

class Continent(models.Model):
    name   = models.CharField(max_length=16)
    code   = models.CharField(max_length=2) 

    class Meta:
        unique_together = (('name','code'), )

    def __unicode__(self):
        return unicode(self.name)

class Country(models.Model):
    name            = models.CharField(max_length=64, unique=True)
    full_name       = models.CharField(max_length=64)
    currency        = models.ForeignKey('Currency', null=True)
    iso_2           = models.CharField(max_length=2, null=True)
    iso_3           = models.CharField(max_length=3, null=True)
    latitude        = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal("0.0"))
    longitude       = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal("0.0"))
    continent       = models.ForeignKey('Continent', null=True)

    def __unicode__(self):
        if hasattr(settings, 'MAX_COUNTRY_NAME_LENGTH'):
            if len(self.name) > settings.MAX_COUNTRY_NAME_LENGTH:
                return self.name[:settings.MAX_COUNTRY_NAME_LENGTH] + '...'
        return unicode(self.name)

class City(models.Model):
    name = models.CharField(max_length=64)
    country     = models.ForeignKey('Country', null=True)
    state       = models.ForeignKey('State', null=True)
    latitude    = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal("0.0"))
    longitude   = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal("0.0"))

    def __unicode__(self):
        return unicode(self.name)

class State(models.Model):
    name = models.CharField(max_length=64)
    country     = models.ForeignKey('Country', related_name="state_country", null=True)
    latitude    = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal("0.0"))
    longitude   = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal("0.0"))
    code        = models.CharField(max_length=2)

    def __unicode__(self):
        return unicode(self.name)

