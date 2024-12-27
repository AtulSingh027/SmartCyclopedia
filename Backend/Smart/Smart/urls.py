from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),         # Admin route
    path('apiSubject/', include('Learn.urls')),
    path('apiTopic/', include('Topic.urls')),
    path('apiChapter/', include('Chapter.urls')),     # API routes
]

# Serve media files only for paths starting with MEDIA_URL
if settings.DEBUG:  # Only for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
