from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class ContactsView(TemplateView):
    template_name = 'contacts.html'


