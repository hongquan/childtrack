from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Child, Activity


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        user = self.request.user
        if user.is_authenticated():
            children = Child.objects.filter(parent=user)
            ctx['children'] = children
        return ctx
