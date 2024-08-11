from . import views
from django.urls import path, include
urlpatterns = [
    path('',views.home, name = 'home'),
    path('menu/', views.MenuItemList.as_view(), name = 'menu'),
    path('menu/detail/<int:pk>',views.MenuItemDetail.as_view(), name = 'menu-detail'),
    path('menu/create', views.MenuItemCreate.as_view(), name = 'menu-create'),
    path('menu/edit/<int:pk>', views.MenuItemUpdate.as_view(), name = 'menu-edit'),
    path('menu/delete/<int:pk>', views.MenuItemDelete.as_view(), name = 'menu-delete'),
    path('recipe/', views.RecipeRequirementList.as_view(), name = 'recipe'),
    path('recipe/detail/<int:pk>', views.RecipeRequirementDetail.as_view, name = 'recipe-detail'),
    path('recipe/create', views.RecipeRequirementCreate.as_view(), name = 'recipe-create'),
    path('recipe/edit/<int:pk>', views.RecipeRequirementUpdate.as_view(), name = 'recipe-edit'),
    path('recipe/delete/<int:pk>', views.RecipeRequirementDelete.as_view(), name = 'recipe-delete'),
    path('ingredient/', views.IngredientsInventoryList.as_view(), name = 'ingredient'),
    path('ingredient/create', views.IngredientsInventoryCreate.as_view(), name = 'ingredient-create'),
    path('ingredient/edit/<int:pk>', views.IngredientsInventoryUpdate.as_view(), name = 'ingredient-edit'),
    path('ingredient/delete/<int:pk>', views.IngredientsInventoryDelete.as_view(), name = 'ingredient-delete'),
    path('purchase',views.PurchaseList.as_view(), name = 'purchase'),
    path('purchase/create', views.PurchaseCreate.as_view(), name = 'purchase-create'),
    path('purchase/edit/<int:pk>', views.PurchaseUpdate.as_view(), name = 'purchase-edit'),
    path('purchase/delete/<int:pk>', views.PurchaseDelete.as_view(), name = 'purchase-delete'),
        
]
