from django.shortcuts import render
import django.contrib.messages as messages
from submit_request.models import SaasRequest
from django.db.models import Q


# Get the search term from the GET request and search the database for it
def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        try:
            # search for the search term in the name, description, status, url, and level of subscription fields
            results = SaasRequest.objects.filter(
                Q(name__icontains=search_term)
                | Q(description__icontains=search_term)
                | Q(status__icontains=search_term)
                | Q(url__icontains=search_term)
                | Q(level_of_subscription__icontains=search_term)
            )
        except Exception as e:
            print(e)
            messages.error(
                request, "Something went wrong with the search. Please try again."
            )
        return render(request, "search.html", {"results": results})
    else:
        return render(request, "search.html", {})


def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key and display results
        saas_request = SaasRequest.objects.get(pk=pk)
        return render(request, "detail.html", {"saas_request": saas_request})