from django.db import models

class Currency(models.Model):
    symbol = models.CharField(max_length=3, blank=False)
    desc = models.CharField(max_length=32)

    def __str__(self):
        return self.desc
    
    def __repr__(self):
        return f"Currency(symbol='{self.symbol}', desc='{self.desc}')"

