====================
Django Template Page
====================

Provides a view mixin and a view that work similar to ``django.views.generic.base.TemplateView``, but determine ``template_name`` based on ``page_path`` from the URL.

* Template-driven; does not require a trip to the database
* Very easy to write a view that extends the provided view (for example, to add permission checks)

Usage
=====

``urls.py``::

    from django.conf.urls import patterns, include, url

    from .views import PublicTemplatePageView


    urlpatterns = patterns('',
        url(r'^pages/(?P<page_path>.+)$', PublicTemplatePageView.as_view()),
    )

``views.py``::

    from template_page.views import TemplatePageView


    class PublicTemplatePageView(TemplatePageView):
        template_dir = 'publicsite/template_pages/'

Then the ``publicsite/template_pages/`` directory must contain a template file for each page that shouldn't raise a 404 Page Not Found error. For example, the URL ``/pages/hello/world`` would look for a template named ``publicsite/template_pages/hello/world.html``
