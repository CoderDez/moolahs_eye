from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError


class Budget(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"""Budget(name='{self.name}', limit={self.limit},
                 date_created='{self.date_created}', creator='{self.creator.username})'"""
    
    def get_absolute_url(self):
        return reverse('budgets-detail', kwargs = {'pk': self.pk})
    
    def total_item_costs(self):
        return sum(item.cost for item in self.item_set.all())

    def remaining_limit(self):
        used = self.total_item_costs()
        remaining = self.limit - used
        return remaining
    
    def clean(self):
        super().clean()
        if self.limit < 0:
            raise ValidationError('Budget limit cannot be negative.')
        if self.pk:
            remaining = self.remaining_limit()
            if remaining < 0:
                raise ValidationError('Total cost of items exceeds budget limit.')
            

        

class Item(models.Model):
    name = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} in {self.budget.name}"
    
    def __repr__(self) -> str:
        return f"""Item(name='{self.name}', limit={self.cost}, budget='{self.budget.name}')"""
    
    def clean(self):
        super().clean()
        if self.name:
            existing_names = [item.name for item in self.budget.item_set.exclude(pk=self.pk)]
            if self.name in existing_names:
                raise ValidationError(f'An item with name \'{self.name}\' already exists in \'{self.budget.name}\'.')
            
        if self.cost < 0:
            raise ValidationError('Item cost cannot be negative.')

        
