from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('note/', views.note, name='note'),
    path('temp/<int:tag_id>', views.extract_tags, name='extract_tag'),
    path('detail/<int:note_id>', views.detail, name='detail')
    ]
