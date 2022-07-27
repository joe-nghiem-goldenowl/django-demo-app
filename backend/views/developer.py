from ..models import Project, Developer
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from ..forms import developer
from django.utils.translation import gettext_lazy as _
from ..utils.decorators import track_bugs
# Handle Developer Request
class DeveloperCreateView(CreateView):
    form_class = developer.DeveloperForm
    template_name = 'backend/developer_form.html'
    success_url = '/'

    @track_bugs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = _("Add")
        context['form_heading'] = _("Add developer")
        return context

class DeveloperUpdateView(UpdateView):
    form_class = developer.DeveloperForm
    template_name = 'backend/developer_form.html'
    model = Developer
    success_url = '/'

    @track_bugs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = _("Update")
        context['form_heading'] = _("Update developer")
        return context
