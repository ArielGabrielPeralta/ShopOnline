from django.shortcuts import render
from django.http import HttpResponse
from OrderManage.models import Article

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
        return render(request, "thanks.html")

    return render(request, "contact.html")
