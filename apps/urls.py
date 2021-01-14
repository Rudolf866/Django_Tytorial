from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from apps import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name='about'),
    path('create', views.create, name="create"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
