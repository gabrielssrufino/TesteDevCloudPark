from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/home/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)

        if user and user.groups.filter(name='Tecnico').exists():
            messages.error(
                self.request,
                'Acesso negado! Técnicos devem acessar o <a href="https://example.com" class="alert-link">Portal para Técnicos</a>.',
                extra_tags='safe'
            )
            return self.form_invalid(form)

        return super().form_valid(form)