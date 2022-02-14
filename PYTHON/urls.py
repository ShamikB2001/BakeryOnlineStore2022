from django.urls import path
from.import views
urlpatterns = [
	path('uploaddata',views.uploaddata),
	path('uld',views.uld),
	path('showalldata',views.showalldata),
	path('delete/<int:id>',views.delete),
	path('edit/<int:id>',views.edit),
	path('edc/<int:id>',views.edc),
	path('vieworder/<int:id>',views.vieworder),
	path('vld/<int:id>',views.vld),
	path('administrator',views.administrator),
	path('adminlog',views.adminlog),
	path('createaccount',views.createaccount),
	path('cre',views.cre),
	path('loginpage',views.loginpage),
	path('log2',views.log2),
	path('customerorder/<int:id>',views.customerorder),
	path('cto/<int:id>',views.cto),
	path('ceo',views.ceo),
	path('showcustomerorder',views.showcustomerorder),
	path('finalorder',views.finalorder),
]