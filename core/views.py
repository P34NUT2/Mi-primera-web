from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    #asi se hace una funcion o metod con buenas practicas siempre pasando el args y el kwargs
    #def get(self, request, *args, **kwargs):
        #return render(request, self.template_name, {'title':"Proyecto Producto diguital"})
        
class SamplePageView(TemplateView):
    template_name =  "core/sample.html"
 
class HowItWorksView(TemplateView):
    template_name = 'core/how_it_works.html'

class FAQView(TemplateView):
    template_name = 'core/faq.html'