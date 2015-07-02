from django.conf.urls import patterns, include, url
from group3 import views, views_prof

urlpatterns = patterns('',
    # prof only
    url(r'/prof/index/$',       views_prof.prof_index,  name='prof_index'),
    url(r'/prof/add/$',         views_prof.prof_add,    name='prof_add'),
    url(r'/prof/view/(\w+)/$',  views_prof.prof_view,   name='prof_view'),
    url(r'/prof/update/(\w+)/$',views_prof.prof_update, name='prof_update'),
    url(r'/prof/delete/(\w+)/$',views_prof.prof_delete, name='prof_delete'),
    #----------------------------------------------------------------------------
    url(r'/shiftProf/(\d+)/$', views.shiftProf, name='shiftProf'),
    url(r'/shiftSubject/(\d+)/$', views.shiftSubject, name='shiftSubject'),
    url(r'/shiftSection/(\d+)/$', views.shiftSection, name='shiftSection'),
    url(r'/updateProf/(\d+)/$', views.updateProf, name='updateProf'),
    url(r'/updateSubject/(\d+)/$', views.updateSubject, name='updateSubject'),
    url(r'/updateSection/(\d+)/$', views.updateSection, name='updateSection'),
    url(r'^prof2lang/$', views.prof2lang_index, name='prof2lang_index'),
    url(r'^prof2lang/(\d+)/$', views.prof2lang_view, name='prof2lang_view'),
    url(r'^prof2lang/add/(\d+)$', views.prof2lang_add, name='prof2lang_add'),
    url(r'^addProf/$', views.addProf, name='addProf'),
    url(r'^addSubject/$', views.addSubject, name='addSubject'),
    url(r'^addSection/$', views.addSection, name='addSection'),
    url(r'^testpdf/(\d+)/$', views.genpdf, name='genpdf'),
    url(r'^genallpdf/$', views.genallpdf, name='genallpdf'),
    url(r'^hourpdf/$', views.hourpdf, name='hourpdf'),
    url(r'^prof2lang/delete/(\d+)$', views.prof2lang_delete, name='prof2lang_delete'),
    url(r'^hourindex/$', views.hour_index, name='hour_index'),
)
