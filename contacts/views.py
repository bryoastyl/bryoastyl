from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        entry_id = request.POST['entry_id']
        entry = request.POST['entry']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        cater_email = request.POST['cater_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                entry_id=entry_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this entry')
                return redirect('/entries/'+entry_id)

        contact = Contact(entry=entry, entry_id=entry_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email
        # send_mail(
        #   'Property entry Inquiry',
        #   'There has been an inquiry for ' + entry + '. Sign into the admin panel for more info',
        #   'bryo@gmail.com',
        #   [cater_email, 'techguyinfo@gmail.com'],
        #   fail_silently=False
        # )

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/entries/'+entry_id)
