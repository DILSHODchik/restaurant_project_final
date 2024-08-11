from django.db import models
from django.utils.timezone import now
from django.urls import reverse
class MenuItem(models.Model):
    menuItemName = models.CharField(max_length = 30)
    menuItemDescription = models.CharField(max_length = 60)
    menuItemPrice = models.FloatField(default = 0)
    menuCategory = models.CharField(max_length = 55)
    menuItemCategory = models.ForeignKey('MenuItemCategory',on_delete = models.CASCADE, verbose_name = "Itemm Category")
    #imageUrl = models.URLField(max_length = 255, null = True, blank = True)
    #recipeUrl = models.URLField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return self.menuItemName
    
    def get_absolute_url(self):
        return reverse("menu-detail",kwargs = {'pk':self.pk})
    
    def get_recipe_url(self):
        return reverse("recipe-detail",kwargs = {'pk':self.pk})
    

class IngredientsInventory(models.Model):
    itemName = models.CharField(max_length = 30)
    itemPrice = models.FloatField(default = 0)
    quantity = models.FloatField(default = 0)
   
    def __str__(self):
        return self.itemName
    
    def get_absolute_url(self):
        return "/ingredient"
    
    
class MenuItemCategory(models.Model):
    nameCategory = models.CharField(max_length = 25)
    
    def __str__(self): 
        return self.nameCategory 


class RecipeRequirementInventory(models.Model):
    ingredient = models.ForeignKey('IngredientsInventory',on_delete = models.CASCADE,verbose_name = "Ingredients")
    menuItem = models.ForeignKey('MenuItem', on_delete = models.CASCADE, verbose_name = "Menu Itemss")
    ingredientQuantity = models.FloatField(default = 0)
    
    def __str__(self):
        return str(self.ingredient) + "for" + str(self.menuItem)
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs = {'pk':self.pk})
    
    
class PurchaseTimeInventory(models.Model):
    purchaseTime = models.DateTimeField(default = now)
    menu_item_id = models.ForeignKey('MenuItem',on_delete = models.CASCADE)
    
    def __str__(self):
        str(self.purchaseTime) + " Purchase"
        
    def get_absolute_url(self):
        return "/purchase"
        