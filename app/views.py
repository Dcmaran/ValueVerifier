from django.shortcuts import render
from app.forms import ConversionForm

def home(request):
    return render(request, 'home.html')

def converter(request):
    return render(request, 'converter.html')

def form(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            # TODO: Insert sqlite
    else:
        form = ConversionForm()

    return render(request, 'template.html', {'form': form})