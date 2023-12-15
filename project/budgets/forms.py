from django.forms import inlineformset_factory, ModelForm
from django.forms.models import BaseInlineFormSet
from .models import Budget, Item
from django.core.exceptions import ValidationError


class BudgetItemFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        
        total_cost = sum(form.cleaned_data.get('cost', 0) for form in self.forms if form.cleaned_data.get('cost'))
        budget = self.instance
        remaining_limit = budget.limit - total_cost

        if remaining_limit < 0:
            raise ValidationError("Total cost of items exceeds budget limit.")


BudgetItemsFormset = inlineformset_factory(
    Budget, Item, 
    formset=BudgetItemFormSet,
    fields=('name', 'cost',),
    labels={'name': 'Name', 'cost': 'Cost'},
    extra=3,
    can_delete=True,
)

