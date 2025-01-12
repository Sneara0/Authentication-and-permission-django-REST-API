from django.urls import path
from myapp import views

urlpatterns =  [
   
       path('myapi/', views.BlogList.as_view()),
       path('snedetail/<int:pk>/', views.apiDetail.as_view()),
       path('gav/', views.contactList.as_view()),
   
    
   
      
       
    
]