from django.db import models

# Create your models here.
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = Q(title_icontains=query) | Q(description_icontains=query) | Q(producttag_title_icontains=query)
        return self.filter(lookups).distinct()

