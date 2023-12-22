from django.db import models

class Currency(models.Model):
    """
    Represents a currency with its symbol and description.

    Fields:
    - symbol (CharField): The currency symbol (max length: 3).
    - desc (CharField): Description of the currency (max length: 32).
    """
    
    symbol = models.CharField(max_length=3, blank=False)
    desc = models.CharField(max_length=32)

    def __str__(self):
        return self.desc
    
    def __repr__(self):
        return f"Currency(symbol='{self.symbol}', desc='{self.desc}')"

