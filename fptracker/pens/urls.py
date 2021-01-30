from django.urls import path

from . import views

urlpatterns = [
    path('pens/add', views.edit_pen, name="add_pen"),
    path('pens/edit/<int:pen_id>', views.edit_pen, name="edit_pen"),
    path('pens/delete/<int:pen_id>', views.delete_pen, name="delete_pen"),
    path('inks/add', views.edit_ink, name="add_ink"),
    path('inks/edit/<int:ink_id>', views.edit_ink, name="edit_ink"),
    path('inks/delete/<int:ink_id>', views.delete_ink, name="delete_ink"),
    path('', views.index, name="index"),
]