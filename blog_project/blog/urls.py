from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.index, name="index"),
    url(r'^posts/$',views.show_all_posts, name="posts"),
     url(r'^posts/(?P<blog_id>[0-9]+)/$', views.blog_post, name="blog"),
     url(r'^add_blog/$',views.add_post,name="add_blog"),
     url(r'^delete/(?P<blog_id>[0-9]+)/$',views.delete_post,name="delete_post"),
      url(r'^register/$', views.register, name="register"),
     url(r'^logout/$', views.user_logout, name="logout"),

)
