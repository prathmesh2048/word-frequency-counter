from django.shortcuts import render
from .forms import Web_addressForm
from .models import Results,Web_address
from .test import start

def index(request):
    template = 'frequency_counter/index.html'
    form = Web_addressForm()

    context = {
        'form':form,
        }
    return render(request,template,context)

def results(request):
    template = 'frequency_counter/results.html'
    if request.method == 'POST':
        data = Web_addressForm(request.POST)
        if data.is_valid():
            web_url = data.cleaned_data['url']
            condition = len(Web_address.objects.filter(url=web_url))
         
            if condition >= 1:
                
                resp = Results.objects.filter(associated_url=Web_address.objects.get(url=web_url)).order_by('-frequency')
                    # context_data = str(resp).split(' ')
                note = 'Note -: The Results were already present in database'
    
            else:
                ###############    
                try:
                    Web_address(url=web_url).save()
                    result = start(web_url)
                    print(result)
                    for i in range(0,10):
                        res = Results()
                        res.associated_url = Web_address.objects.get(url=web_url)
                        res.word = result[i][0]
                        res.frequency = result[i][1]
                        res.save()
                    
                    resp = Results.objects.filter(associated_url=Web_address.objects.get(url=web_url)).order_by('-frequency')
                        # context_data = str(resp).split(' ')
                    note = 'Note-: Freshly obtained Results !'
                except:
                    resp = ''
                    note = 'Note-: Freshly obtained Results !'
                
            context = {
                'resp':resp,
                'note':note
                }
    return render(request,template,context)