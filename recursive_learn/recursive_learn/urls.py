from django.contrib import admin
from django.urls import path, include

app_name = 'principal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('exercises/', include('exercises.urls')),
]

handler404 = "core.views.my_custom_page_not_found_view"
handler500 = "core.views.my_custom_error_view"
handler403 = "core.views.my_custom_permission_denied_view"
handler400 = "core.views.my_custom_bad_request_view"
