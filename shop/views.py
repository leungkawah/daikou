from django.shortcuts import render
from .models import GoodsInstance, Goods


def index(request):
    """View function for home page of site."""
    num_goods = Goods.objects.all().count()
    num_instances = GoodsInstance.objects.all().count()

    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1

    return render(
        request,
        "index.html",
        context={
            "num_goods": num_goods,
            "num_instances": num_instances,
            "num_visits": num_visits,
        },
    )
