from django.urls import path
from accounts import views as AccountsViews

urlpatterns = [
    
    path('register/', AccountsViews.register_view, name='register'),
    path('login/', AccountsViews.login_view, name='login'),
    path('logout/', AccountsViews.logout_view, name='logout')

]
