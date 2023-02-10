from django.shortcuts import render
from django.http import HttpResponse
from . import util
from markdown2 import Markdown
markdowner= Markdown()
lists = [entry for entry in util.list_entries()]
print(lists)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, page):
    if page in lists:
        html = markdowner.convert(util.get_entry(page))
        return render(request, "encyclopedia/entry.html", {
            "page": page, "content":markdowner.convert(html)
        })
    else:
        return render(request, "encyclopedia/entry.html")