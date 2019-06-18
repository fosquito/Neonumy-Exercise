from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.ListImage.as_view(), name='image_list'),
    path('upload', views.CreateImage.as_view(), name='upload'),
    path('image/<int:pk>', views.DetailImage.as_view(), name='image_detail'),
    path('deleteimg/<int:pk>', views.DeleteImage.as_view(), name='image_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
