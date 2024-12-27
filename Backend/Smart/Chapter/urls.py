from django.urls import path
from Chapter import views

urlpatterns = [ # No parameter
    path('Chapterspage/<int:cpk>/', views.Chapterspage),  # With parameter
    path('Chaptersget', views.Chaptersget),
]

# Serve media files only for paths startin,g with MEDIA_URL

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:  # Only for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
