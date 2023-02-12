from django.shortcuts import render
<<<<<<< HEAD

from . import util
=======
from django.http import HttpResponse
from . import util
from markdown2 import Markdown
markdowner= Markdown()
lists = [entry for entry in util.list_entries()]
print(lists)
>>>>>>> 3001f176ee11bec3f7527c1400ac85204b8577a7


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
<<<<<<< HEAD

def test(request):
    return render(request, "encyclopedia/test.html")
=======
def entry(request, page):
    if page in lists:
        html = markdowner.convert(util.get_entry(page))
        return render(request, "encyclopedia/entry.html", {
            "page": page, "content":markdowner.convert(html)
        })
    else:
        return render(request, "encyclopedia/entry.html")
>>>>>>> 3001f176ee11bec3f7527c1400ac85204b8577a7
