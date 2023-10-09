from django.shortcuts import render
from django.utils import timezone
from app.convert_util.api_call import convert

from app.forms import ConversionForm
from app.models import Conversion


def home(request):
    return render(request, 'home.html')


def converter(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            currency = form.cleaned_data['from_currency']

            conversion = Conversion(
                date=timezone.now(),
                input=amount,
                output=convert(form.cleaned_data['from_currency'], form.cleaned_data['to_currency'], amount),
                rate=convert(form.cleaned_data['from_currency'], form.cleaned_data['to_currency'], 1),
                currency=currency,
                converted_currency=form.cleaned_data['to_currency']
            )

            result = convert(form.cleaned_data['from_currency'], form.cleaned_data['to_currency'], amount)
            conversion_date = conversion.date.astimezone(timezone.get_current_timezone()).strftime('%d/%m/%Y %H:%M')


            conversion.save()

            return render(request, 'converter.html', {'form': form, 'conversion': conversion, 'result': result, 'to': form.cleaned_data['to_currency'], 'conversion_date': conversion_date})
    else:
        form = ConversionForm()

    return render(request, 'converter.html', {'form': form})

