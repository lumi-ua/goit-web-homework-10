from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import QuoteForm, AuthorForm
from .models import Tag, Quote, Author

def main(request, page=1):
    per_page = 10
    quotes = Quote.objects.all()
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "app_quotes/index.html", context={'quotes': quotes_on_page})


def about_author(request, author_name):
    author = get_object_or_404(Author, fullname=author_name)
    return render(request, "app_quotes/about_author.html", context={"author": author})

@login_required
def quote(request):
    tags = Tag.objects.all()
    all_authors = Author.objects.all()
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            new_quote.author = Author.objects.get(id=request.POST.get("author"))
            new_quote.save()

            return redirect(to="app_quotes:main")
        else:
            return render(
                request,
                "app_quotes/quote.html",
                {"tags": tags, "all_authors": all_authors, "form": form},
            )

    return render(
        request,
        "app_quotes/quote.html",
        {"tags": tags, "all_authors": all_authors, "form": QuoteForm()},
    )


@login_required
def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            new_author.save()

            return redirect(to="app_quotes:main")
        else:
            return render(
                request,
                "app_quotes/author.html",
                {"form": form},
            )

    return render(
        request,
        "app_quotes/author.html",
        {"form": AuthorForm()},
    )
