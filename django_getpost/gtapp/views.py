from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView

# Create your views here.
def MainFunc(requst):
    return render_to_response('index.html')

class CallView(TemplateView):
    template_name = "callget.html"

def InsertFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        return render_to_response('insert.html')
    elif request.method == 'POST':
        print('POST 요청 처리')
        #name = request.POST.get('name')
        name = request.POST['name']
        return render(request, 'list.html', {'name':name})
    else:
        print('Error')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        