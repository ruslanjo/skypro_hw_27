import json

from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from ads.models import Ads, Categories


class Index(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()

        res = []
        for category in categories:
            res.append(
                {'id': category.id,
                 'name': category.name}
            )
        return JsonResponse(res, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)
        new_category = Categories.objects.create(name=category_data['name'])
        return JsonResponse({'pk': new_category.id, 'name': new_category.name}, status=201, safe=False)


class CategoryView(DetailView):
    model = Categories
    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({'id': category.id, 'name': category.name})


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()

        res = []
        for ad in ads:
            res.append(
                {'id': ad.id,
                 'name': ad.name,
                 'author': ad.author,
                 'price': ad.price,
                 'description': ad.description,
                 'address': ad.address,
                 'is_published': ad.is_published}
            )
        return JsonResponse(res, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        new_ad = Ads.objects.create(
            name=ad_data.get('name'),
            author=ad_data.get('author'),
            price=ad_data.get('price'),
            description=ad_data.get('description'),
            address=ad_data.get('address'),
            is_published=ad_data.get('is_published')
        )
        return HttpResponse(status=201)


class AdView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse(
            {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }
                            )
