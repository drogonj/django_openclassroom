from django.shortcuts import render
from listings.models import Band, Contact
from listings.forms import ContactUsForm, BandForm, ContactForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})

def band_detail(request, band_id):
    try:
        band = Band.objects.get(id=band_id)
        return render(request, 'listings/band_detail.html',
                       {'band': band})
    except ObjectDoesNotExist:
        raise Http404("Object Does Not Exist")

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band_detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html',
                  {'form': form})

def band_edit(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band_detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_edit.html',
                  {'form': form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band_list')
    return render(request, 'listings/band_delete.html',
                  {'band': band})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'listings/contact_list.html',
                  {'contacts': contacts})

def contact_detail(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
        return render(request, 'listings/contact_detail.html',
                      {'contact': contact})
    except ObjectDoesNotExist:
        raise Http404("Object Does Not Exist")

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', contact.id)
    else:
        form = ContactForm()
    return render(request, 'listings/contact_create.html',
                  {'form': form})

def contact_edit(request, contact_id):
    contact = Contact.objects.get(id=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if (form.is_valid()):
            form.save()
            return redirect('contact_detail', contact_id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'listings/contact_edit.html',
                  {"form": form})

def contact_delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'listings/contact_delete.html',
                  {"contact": contact})

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email_sent')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact_us.html',
                  {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def about(request):
    return render(request, 'listings/about_us.html')
