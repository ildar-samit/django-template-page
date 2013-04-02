from django import template
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.views.generic.base import TemplateView


class TemplatePageMixin(object):
    """
    Mixin that determines ``template_name`` based on ``page_path`` from the URL.
    To be used together with ``TemplateView``.
    """
    template_dir = None

    def get_template_names(self):
        if self.template_dir is None:
            raise ImproperlyConfigured(
                "TemplatePageMixin requires a definition of 'template_dir'"
            )
        if 'page_path' not in self.kwargs:
            raise ImproperlyConfigured(
                "TemplatePageMixin requires 'page_path' to be in URL kwargs"
            )
        # Build the the ``template_name`` variable
        if self.template_name is None:
            page_path = self.kwargs['page_path']
            self.template_name = '{0}{1}.html'.format(self.template_dir, page_path)
            # Check if the template file exists. Raise 404 error if it doesn't.
            try:
                template.loader.get_template(self.template_name)
            except template.TemplateDoesNotExist:
                raise Http404
        return super(TemplatePageMixin, self).get_template_names()


class TemplatePageView(TemplatePageMixin, TemplateView):
    """
    This view can be subclassed instead of using a mixin, if desired.
    """
