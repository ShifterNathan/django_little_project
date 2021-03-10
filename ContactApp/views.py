from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.



def contact(request):
    contact_form=ContactForm # Instantiating the var

    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")

            email=EmailMessage("Message from Django",
            "User: {} Address: {} Message:\n\n {}".format(name,email,content),
            "",["alternplayer00@gmail.com"],reply_to=[email])

            try: 
                email.send()
                return redirect("/contact/?valid")

            except:
                return redirect("/contact/?notvalid")

            

    return render(request, "contact_template/contact.html", {'form': contact_form})
