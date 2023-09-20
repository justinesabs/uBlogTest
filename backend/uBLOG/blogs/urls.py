from django.urls import path
from. import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('create/', views.create_blog, name='create'),
    path('update/<slug>/', views.update_blog, name='update'),
    path('delete/<slug>/', views.delete_blog, name='delete'),
    path('<slug>', views.blog, name='blog'),
]