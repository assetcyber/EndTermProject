from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('filling', views.filling, name = 'fill'),
    path('recordings', views.recordings, name = 'recordings'),
    path('update/<int:pk>', views.filling_UpdateView.as_view(), name = 'filling_update'),
    path('delete/<int:pk>', views.filling_DeleteView.as_view(), name = 'filling_delete'),
    path('zona', views.zona, name = 'zona'),
    path('dopcontent', views.dopcontent, name = 'dopcontent'),
    path('iitu', views.iitu, name='iitu'),
    path('iitu2', views.iitu2, name='iitu2'),
    path('iitu3', views.iitu3, name='iitu3'),
    path('iitu4', views.iitu4, name='iitu4'),
    path('dopcontent/fill', views.dopcontent_fill, name='dopcontent_fill'),
    path('post/<slug:post_slug>', views.show_post, name = 'post'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('sendler', views.sendler, name = 'sendler'),
]
