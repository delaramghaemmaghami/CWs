from django.shortcuts import render
from django.contrib import messages
from .models import ContactList, ContactForm


def home_page(req):
    messages.success(req, "hiiiiiiiiiiiiii")
    return render(req, "pages/home.html", {'test': 'the test text'})

def about_page(req):
    return render(req, "pages/about.html")


def contact_page(req):
    if req.method == "POST":
        t = req.POST.get('title')
        e = req.POST.get('email')
        n = req.POST.get('name')
        m = req.POST.get('msg')
        c_form = ContactForm(title= t, email= e, name= n, message= m)   
        print(t, e, n)
        c_form.save()
        
    
    result =ContactList.objects.all()[0]    
        
    contact_data = {
        #'phone' : '+98 912 1234567',
        #'email' : "61@maktab.com",
        #'addr' : '4th Floor, No. 12, Khovardin Blvd, Shahak Gharb, Tehran, 0022446688, IRAN',
        #'tel': "@MyTelegramAccount",
        'res': result
    }
    print(result)
    print(type(result))
    return render(req, "pages/contact.html", contact_data)
