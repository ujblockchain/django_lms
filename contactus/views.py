from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import ContactForm
from .models import Contactus

def contactus(request): 
    # MANUAL METHOD OF WORKING WITH FORMS
    # if request.method == 'POST':
    #     full_name = request.POST['full_name']
    #     print(full_name)
    #     # manual validation
    #     if (full_name == "" or len(full_name) <= 6): 
    #         return render(request, "contactus/contact.html", {
    #             "has_error": True
    #         })
    #     return HttpResponseRedirect("message-sent")
        
    # return render(request, "contactus/contact.html")
    
    # DJANGO BUILT-IN FORMS FUNCTIONALITY 
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        
        if form.is_valid(): 
            
            if (request.FILES['screenshot']): 
                contact = Contactus(full_name=form.cleaned_data['full_name'], email=form.cleaned_data['email'], level=form.cleaned_data['level'], comment=form.cleaned_data['comment'], screenshot=request.FILES['screenshot'])
                contact.save()
                return HttpResponseRedirect("message-sent")
                
            
            contact = Contactus(full_name=form.cleaned_data['full_name'], email=form.cleaned_data['email'], level=form.cleaned_data['level'], comment=form.cleaned_data['comment'])
            contact.save()
            return HttpResponseRedirect("message-sent")
    else: 
        form = ContactForm()
        
    return render(request, "contactus/contact.html",{
        "form": form
    })


def messageSent(request):
    queries = Contactus.objects.all()
    
    return render(request, "contactus/success.html", {
        "queries": queries
    })
