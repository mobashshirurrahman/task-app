from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("task/", include('todolist_app.urls')),
    path("", include('todolist_app.urls'))  # empty also currently go to task
]
