from django.shortcuts import render
from django.http import HttpResponse
from OrderManage.models import Article
from django.core.mail import send_mail
from django.conf import settings
from OrderManage.forms import ContactForm

# Create your views here.


def search_article(request):
    return render(request, "search_article.html")


def search(request):

    if request.GET["art"]:

        #message = "Searched Article: %r" % request.GET["art"]

        article = request.GET["art"]

        if len(article) > 20:
            message = "Text is very long"
        else:

            articles = Article.objects.filter(name__icontains=article)

            return render(request, "answer_search.html", {"articles": articles, "query": article})

    else:

        message = "You haven't entered anything"

    return HttpResponse(message)


def contact(request):
    if request.method == "POST":
        newform = ContactForm(request.POST)
        if newform.is_valid():
            info_form = newform.cleaned_data
            send_mail(info_form['subject'], info_form['message'], info_form.get(
                'email', 'agperalta80@gmail.com'), ['arielgabrielperalta.98@hotmail.com'],)
            return render(request, 'thanks.html')
    else:
        newform = ContactForm()
    return render(request, 'form_contact.html', {'form': newform})
