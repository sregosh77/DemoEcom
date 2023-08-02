from django.urls import path
from.import views
app_name = 'app'

urlpatterns=[
             path('',views.allProdCat,name='allProdCat'),
             path('category/<slug:c_slug>/',views.allProdCat,name='products_by_category'),
             path('category/<slug:c_slug>/<slug:product_slug>/',views.proCatDetail,name='proDetail')
             ]
