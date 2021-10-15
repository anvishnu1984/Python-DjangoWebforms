from django.shortcuts import render
from django.views.generic import  (TemplateView, ListView, CreateView, DetailView,FormView)
from .models import Environment
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from .forms import EnvironmentTagVersionsFormset
from  django.http import HttpResponseRedirect



class HomeView(TemplateView):
    template_name = 'home.html'

class EnvironmentDetailView(DetailView):
     model = Environment
     template_name = 'Environment_detail.html'




# Create your views here.
class  EnvironmentListView(ListView):
    model = Environment
    template_name = 'Environment_List.html'
    context_object_name = 'Environment_List'


class EnvironmentCreateView(CreateView):
    model = Environment
    template_name = 'Environment_Createtagversions.html'
    fields = ['name']


    def form_valid(self,form):
      messages.add_message(
          self.request,
          messages.SUCCESS,

           'The environment has been added'
      )
      return super().form_valid(form)


class EnvironmentTagversionsEditView(SingleObjectMixin,FormView):

    model = Environment
    template_name = 'Environment_TagVersion_Edit.html'

    def get(self,request, *args, **kwargs):
        self.object = self.get_object(queryset=Environment.objects.all())
        return super().get(request,*args,**kwargs)



    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Environment.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self,form_class=None):
        return EnvironmentTagVersionsFormset(**self.get_form_kwargs(), instance =self.object )

    def form_valid(self, form):
         form.save()

         return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('Environments:Environment_detail',kwargs={'pk': self.object.pk})
