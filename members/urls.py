from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user, name='log'),
    path('login/new/', views.new, name='newacc'),
    path('shop/', views.ligs, name='ligs'),
    path('bundle/', views.bundles, name='bundles'),
    path('checkout/bundle/<int:id>', views.delete_bundle, name='delete_bundle'),
    path('bundle/<str:image1>/<int:id>', views.bundlesopen, name='bundlesopen'),
    path('bundle/<str:image1>/<int:id>/<str:option>/', views.bundlesopen, name='bundlesopened'),
    path('bundle/<str:image1>/<int:id>/price/', views.bundlesprice, name='bundlesprice'),
    path('shop/<int:id>/', views.shops, name='shops'),
    path('shop/<str:image1>/<int:id>', views.opencart, name='opencart'),
    path('shop/carts/<int:id>', views.carts, name='carts'),
    path('shop/checkout', views.checkout, name='checkout'),
    path('shop/checkout/<int:id>/', views.delete_item, name='delete_item'),

]