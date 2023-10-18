from django.urls import path, include
from accounts.views import signup, user_login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('recipes/', include('recipes.urls')),
    path('login/', user_login, name='user_login'),
]
