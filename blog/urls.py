from django.urls import path
from . import views 

urlpatterns = [
    path('',views.PostListView.as_view(),name='blog-home' ),
    path('post/<int:pk>/',views.PostDetailsView.as_view(),name='post-details' ),
    path('about/',views.about,name='blog-about' ),

]
