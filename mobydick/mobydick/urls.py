from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse



# subclass TemplateView to replicate direct_to_template
class DirectTemplateView(TemplateView):
    extra_context = None
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value
        return context


def hello(request):
   return HttpResponse('hello world!')

def chapter(request, chapter):
	return render_to_response('%s-front-matter.md' % chapter)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mobydick.views.home', name='home'),
    # url(r'^mobydick/', include('mobydick.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

   	url(r'^$', hello),
   # url(r'^chapter/000', DirectTemplateView.as_view(template_name='000-front-matter.md', extra_context={'title':'foobar'})),
	url(r'^chapter/(?P<chapter>\d{3})$', chapter),
)

