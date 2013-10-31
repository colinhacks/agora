from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'agora.views.home', {'template':'landing.html'}),
    url(r'^hello/$', 'agora.views.hello', {'template':'hello.html'}),
    url(r'^login/$', 'agora.views.login', {'template':'login.html'}),
    url(r'^post/$', 'postapp.views.create_post', {'template':'create_post.html'}),
    url(r'^logout/$', 'agora.views.logout'),
    url(r'^create_post/$', 'postapp.views.create_post'),
    url(r'^process_create_post/$', 'postapp.views.process_create_post'),
    url(r'^post/vote/$', 'postapp.views.vote'),

    #url(r'^agora/', include('agora.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),

    url(r'^post/(?P<pk>[0-9]+)$', 'agora.views.thread', {'template':'post_thread.html'}),

    url(r'^city/$', 'agora.views.city', {'template':'posts_for_town.html'}),
    url(r'^city/(?P<pk>[0-9]+)$', 'agora.views.allposts', {'template':'real_posts_for_town.html'}),
    url(r'^register/$', 'userapp.views.register', {'template':'create.html'}),


)
