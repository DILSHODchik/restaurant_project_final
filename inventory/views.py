from django.shortcuts import render,redirect 
from .forms import MenuCategoryForm, MenuForm, IngredientForm, RecipeForm, PurchaseForm, RecipeFormSet
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import MenuItem, MenuItemCategory, IngredientsInventory, PurchaseTimeInventory, RecipeRequirementInventory
from django.http import HttpResponse, HttpRequest,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def home(request):
    return HttpResponse("Working on the project ... ")

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = "inventory/MenuItemCreate.html"
    form_class = MenuForm
    
class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/MenuItemList.html"
    

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = "inventory/MenuItemUpdate.html"
    form_class = MenuForm

class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = "inventory/MenuItemDelete.html"
    success_url = "/menu/"
    
    
class MenuItemDetail(DetailView):
    model = MenuItem
    template_name = "inventory/MenuDetail.html"


class IngredientsInventoryList(ListView):
    model = IngredientsInventory
    template_name = "inventory/IngredientList.html"
 
 
class IngredientsInventoryCreate(CreateView):
    model = IngredientsInventory
    template_name = "inventory/IngredientCreate.html"
    form_class = IngredientForm


class IngredientsInventoryUpdate(UpdateView):
    model = IngredientsInventory
    template_name = "inventory/IngredientUpdate.html"
    form_class = IngredientForm


class IngredientsInventoryDelete(DeleteView):
    model = IngredientsInventory
    template_name = "inventory/IngredientDelete.html"
    success_url = "/ingredient/"
    
#RecipeTime

class RecipeRequirementList(ListView):
    model = MenuItem
    template_name = "inventory/RecipeList.html"
    
class RecipeRequirementList(ListView):
    model = MenuItem
    template_name = "inventory/RecipeList.html"
    context_object_name = "recipe_item"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_avail'] = RecipeRequirementInventory.objects.all()

class RecipeRequirementDetail(DetailView):
    model = MenuItem
    template_name = "inventory/RecipeDetail.html"
    context_object_name = "recipe_item"
    def get_context_data(self,**kwargs):
        context = super(RecipeRequirementList, self).get_context_data(**kwargs)
        context["recipe_req_list"] = RecipeRequirementInventory.objects.filter(menuItem_id = self.object)
        context["recipe_ingredient_query"] = RecipeRequirementInventory.objects.select_related("ingredient")
        return context

class RecipeRequirementCreate(CreateView):
    model = RecipeRequirementInventory
    template_name = "inventory/RecipeCreate.html"
    form_class = RecipeForm
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = RecipeFormSet(queryset = RecipeRequirementInventory.objects.none())
        return context
    
    def post(self,request,*args, **kwargs):
        formset = RecipeFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)
    
    def form_valid(self,formset):
        instances = formset.save(commit = False)
        for instance in instances:
            instance.save()
        return HttpResponseRedirect('/recipe')
    
class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirementInventory
    template_name = "inventory/RecipeDelete.html"
    success_url = ""


class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirementInventory
    template_name = "inventory/RecipeUpdate.html"
    form_class = RecipeForm
    
#PurchaseTime

class PurchaseList(ListView):
    model = PurchaseTimeInventory
    template_name = "inventory/PurchaseList.html"
  
class PurchaseCreate(CreateView):
    model = PurchaseTimeInventory
    template_name = "inventory/PurchaseCreate.html" 
    form_class = PurchaseForm
    success_url = reverse_lazy('ingredient-list')
    
class PurchaseDelete(DeleteView):
    model = PurchaseTimeInventory
    template_name = "inventory/PurchaseDelete.html" 
    success_url = ""

class PurchaseUpdate(UpdateView):
    model = PurchaseTimeInventory
    template_name = "inventory/PurchaseUpdate.html" 
    form_class = PurchaseForm
    
     
    