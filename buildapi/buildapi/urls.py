"""buildapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstapp.api.views import NoteList, NoteDetails, NoteCreate, NoteUpdate, NoteDelete



#These are the urls used to access the endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', include("firstapp.urls")),
    path('api/notes/', NoteList.as_view()),
    path('api/notes/<int:pk>/', NoteDetails().as_view()),
    path("api/notes/create/", NoteCreate.as_view()),
    path("api/notes/update/<int:pk>", NoteUpdate.as_view()),
    path("api/notes/delete/<int:pk>", NoteDelete.as_view()),
]



from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)