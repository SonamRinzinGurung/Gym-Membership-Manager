from .forms import SearchForm

def inject_form(request):
    return {'searchform': SearchForm()}