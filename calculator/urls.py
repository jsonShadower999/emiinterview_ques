from django.urls import path 
from . import views 
from  .views  import submit_info,check_api,emi_calc

urlpatterns=[
    path('enroller_client/',submit_info,name='submit_info'),
    path('emi_info/',emi_calc,name='emi_calc'),
    
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('api/', include('myapp.urls')),
#     path('paynow/', paynow, name='paynow'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ]
