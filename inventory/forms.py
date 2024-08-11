from django import forms 
from .models import MenuItem, IngredientsInventory, MenuItemCategory, RecipeRequirementInventory, PurchaseTimeInventory
from django.forms import modelformset_factory
class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
        
class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientsInventory
        fields = '__all__'

class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuItemCategory 
        fields = '__all__'

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirementInventory
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta: 
        model = PurchaseTimeInventory
        fields = '__all__'
        
RecipeFormSet = modelformset_factory(RecipeRequirementInventory,fields = '__all__',max_num = 20)