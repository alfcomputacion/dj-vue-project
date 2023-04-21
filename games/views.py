import json
from django.db.models import Q
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.paginator import Paginator

from .models import GameScore
from django.views.generic import TemplateView, ListView
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class AnagramGameView(LoginRequiredMixin, TemplateView):
    template_name = 'games/anagram-game.html'


class MathGameView(LoginRequiredMixin, TemplateView):
    template_name = 'games/math-game.html'


def record_score(request):
    data = json.loads(request.body)

    user = request.user
    game = data["game"]
    score = data["score"]
    operation = data["operation"]
    max_number = data["max_number"]

    new_score = GameScore(user=user, game=game, score=score,
                          operation=operation, max_number=max_number)
    new_score.save()

    resopnse = {
        "success": True
    }

    return JsonResponse(resopnse)


# def show_score(request):
#     # sort =  json.loads(request.body)
#     # if sort['sort']:
#     #     data = GameScore.objects.filter(user=request.user & Q())

#     data = GameScore.objects.filter(user=request.user)
#     js_data = serializers.serialize('json', data)

#     return HttpResponse(js_data, content_type='application/json')

def show_score(request):
    post_data = json.loads(request.body)
    game = post_data['game']
    asc = post_data['asc']
    order = post_data['order']
    if asc:
        order = '-' + order

    per_page = 3

    reviews = GameScore.objects.filter(
        user=request.user, game=game
    ).order_by(order)

    paginator = Paginator(reviews, per_page)
    page_obj = paginator.get_page(post_data['page'])
    num_pages = page_obj.paginator.num_pages

    print(num_pages)
    data = page_obj.object_list.count()
    print(reviews.count())
    # js_data = serializers.serialize('json', data)
    js_data = [{"game": kw.game, "operation": kw.operation,
                "max_number": kw.max_number, "score": kw.score,
                "created": kw.created} for kw in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "total_records": reviews.count(),
            "num_pages": num_pages,


        },
        "data": js_data
    }
    return JsonResponse(payload)


def show_ledear_board(request):
    post_data = json.loads(request.body)
    # game = post_data['game']
    asc = post_data['asc']
    order = post_data['order']
    print(asc)
    if asc:
        order = '-' + order
    print(order)

    response = list(GameScore.objects.values(
        # 'user__username', 'score', 'operation', 'max_number', 'game', 'created').order_by('-score', '-created'))
        'user__username', 'score', 'operation', 'max_number', 'game', 'created').order_by(order, '-created'))

    return JsonResponse(response, safe=False)

    # data = CustomUser.objects.filter(user__username=request.user)
    # js_data = serializers.serialize('json', data)
    # return HttpResponse(js_data, content_type='application/json')


def get_user(LoginRequiredMixin, request):
    data = CustomUser.objects.all()
    js_data = serializers.serialize('json', data)
    return HttpResponse(js_data, content_type='application/json')


class GameScoreView(ListView):
    model = GameScore
    paginate_by = 5
    template_name = 'games/game-scores.html'

    def get_context_data(self, **kwargs):
        context = super(GameScoreView, self).get_context_data(**kwargs)

        context['anagram_scores'] = GameScore.objects.filter(
            game__exact='ANAGRAM').order_by('-score')[:5]

        context['math_scores'] = GameScore.objects.filter(
            game__exact='MATH').order_by('-score')[:5]
        return context


class LeaderBoardView(ListView):
    model = GameScore
    template_name = 'games/leader-board.html'
