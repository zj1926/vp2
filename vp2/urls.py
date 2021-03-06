from django.urls import path, re_path
from colorpk import views
from colorpk import static
from colorpk import controller

urlpatterns = [
    path('', views.latest),
    path('color/<int:id>', views.color_one),
    path('latest', views.latest),
    path('popular', views.popular),
    path('new', views.new_color),
    path('signin', views.signin),
    path('profile', views.profile),
    path('auth/<str:src>', views.auth),
    path('admin', views.admin),
    path('about', views.about),
    # path('statement', views.statement),

    path('like/<int:id>', controller.toggle_like),
    path('approve/<int:id>', controller.approve),
    path('sync', controller.sync_cache),
    path('create', controller.create_color),

    path('sitemap.xml', static.sendSitemap),

    re_path(r'/*', views.not_found),
]
