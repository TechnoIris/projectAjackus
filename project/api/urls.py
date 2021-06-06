from django.conf.urls import url
 
from api import views
 
app_name = 'api'
 
urlpatterns = [
 
    # /modelforms/
    url(r'^$', views.IndexAuthor.as_view(), name='author'),
 
    # api/authorregistration
    url(r'^author/entry/$',views.AuthorEntry.as_view(),name='Authorcreate'),
 
    # modelforms/product/(?P<pk>[0-9]+)/delete
    url(r'', views.AuthorDelete.as_view(), name='author-delete'),
 
    #book create
    url(r'^$', views.IndexBook.as_view(), name='book'),

    #book_del
    url(r'^$', views.CreateBook.as_view(), name='AddBook'),

    #del book
    url(r'^$', views.DeleteBook.as_view(), name='DelBook'),

    #searchBook
    url(r'^$', views.SearchBook.as_view(), name='SearchBook')
]
