
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('roster/', include('school_roster.urls')),
    path('grades/', include('grades.urls'))
]
