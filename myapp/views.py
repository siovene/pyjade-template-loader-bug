from django.views.generic.base import TemplateView

class MyView(TemplateView):
  template_name = 'my_template.html'

  def get_context_data(self):
    return {
      'exclude': '',
      'names': ['Alice'],
    }
