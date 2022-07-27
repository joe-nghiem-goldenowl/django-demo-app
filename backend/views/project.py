from django.shortcuts import redirect
from ..models import Project, Developer
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from ..forms import project
from django.utils.translation import gettext_lazy as _
from ..utils.decorators import track_bugs
# Handle Project Request
class ProjectListView(ListView):
    model = Project
    paginate_by = 10

    @track_bugs
    def get_queryset(self):
        query_data = self.request.GET
        from_date, to_date = query_data.get('from'), query_data.get('to')
        name = query_data.get('name')
        currency_unit = query_data.get('currency')

        queryset = Project.objects.all()
        if from_date and to_date:
            queryset = queryset.filter(date_start__gte = from_date, date_end__lte = to_date)

        if name:
            queryset = queryset.filter(name__icontains = name)

        if currency_unit:
            if currency_unit == 'VND':
                from json import loads
                from decimal import Decimal
                currency = {}
                with open('currency_rate.json', 'r') as f:
                    currency_json = f.read()
                    currency = loads(currency_json)
                    f.close()

                rate = currency['rate']
                for item in queryset:
                    item.cost = round(item.cost * Decimal(rate), 2)
        else:
            currency_unit = 'USD'
        
        for item in queryset:
            item.cost = ' '.join([str(item.cost), currency_unit])
        
        return queryset
    
    @track_bugs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_content'] = self.request.GET.dict()
        return context

class ProjectUpdateView(UpdateView):
    form_class = project.ProjectForm
    template_name = 'backend/project_form.html'
    model = Project
    success_url = '/'

    @track_bugs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = _("Update")
        context['form_heading'] = _("Update project")
        return context

class ProjectCreateView(CreateView):
    form_class = project.ProjectForm
    template_name = 'backend/project_form.html'
    success_url = '/'

    @track_bugs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = _("Create")
        context['form_heading'] = _("Create project")
        return context

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/'