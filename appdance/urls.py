from django.urls import path,include
from. import views

urlpatterns = [
    # path('view',views.viewfunction,name='view'),
    # path('create',views.createfunction,name='create'),
    # path('delete/<int:id>',views.deletefunction,name='delete'),
    # path('update/<int:id>',views.updatefunction,name='update'),
    # path('updation/<int:id>',views.updationfunction,name='updation'),
    # path('show',views.showfunction,name='show'),
    path('data', views.datafunction,name='data'),
    path('data/<int:id>', views.datafunction,name='data'),
    

]
    
    
    
