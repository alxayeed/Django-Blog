from django.urls import path
from . import views 

urlpatterns = [
    path('',views.PostListView.as_view(),name='blog-home' ),
    path('post/<int:pk>/',views.PostDetailsView.as_view(),name='post-details' ),
    path('post/new/',views.PostCreateView.as_view(),name='create-post' ),#app/model_form.html
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post-update' ),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post-delete' ),
    path('about/',views.about,name='blog-about' ),

]
