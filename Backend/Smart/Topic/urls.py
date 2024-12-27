from django.urls import path
from Topic import views

urlpatterns = [
    # API routes
    path('Topicspage/<int:tpk>/', views.Topicspage, name="topic-page"),
    path('Topicsget', views.Topicsget, name="topic-add"),
]

# Serve media files only for paths startin,g with MEDIA_URL

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:  # Only for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
