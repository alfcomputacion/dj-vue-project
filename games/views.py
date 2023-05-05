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


def show_score(request):
    user = str(request.user)
    post_data = json.loads(request.body)
    game = post_data['game']
    asc = post_data['asc']
    order = post_data['order']

    if asc:
        order = '-' + order

    per_page = 10

    scores = GameScore.objects.filter(
        user=request.user, game=game
    ).order_by(order)

    paginator = Paginator(scores, per_page)
    page_obj = paginator.get_page(post_data['page'])
    num_pages = page_obj.paginator.num_pages

    # print(num_pages)
    data = page_obj.object_list.count()
    # print(scores.count())
    # js_data = serializers.serialize('json', data)
    js_data = [{"game": kw.game, "operation": kw.operation,
                "max_number": kw.max_number, "score": kw.score,
                "created": kw.created} for kw in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "total_records": scores.count(),
            "num_pages": num_pages,
        },
        "user": user,
        "data": js_data,
    }
    return JsonResponse(payload)


def show_ledear_board(request):
    post_data = json.loads(request.body)
    game = post_data['game']
    asc = post_data['asc']
    order = post_data['order']

    search = post_data['search']

    user = str(request.user)
    # print(type(user))
    per_page = 10

    if asc:
        order = '-' + order

    scores = list(GameScore.objects.values(

        'user__avatar', 'user__username', 'score', 'operation', 'max_number', 'game', 'created').
        filter(Q(user__username__icontains=search) & Q(game=game)).order_by(order, '-created'))
    paginator = Paginator(scores, per_page)

    page_obj = paginator.get_page(post_data['page'])
    num_pages = page_obj.paginator.num_pages
    # print(page_obj.object_list)

    response = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            # "total_records": scores.count(),
            "num_pages": num_pages,
        },
        "user": user,
        "data": page_obj.object_list
    }
    return JsonResponse(response)

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

    # def get_context_data(self, **kwargs):
    #     context = super(GameScoreView, self).get_context_data(**kwargs)

    #     context['anagram_scores'] = GameScore.objects.filter(
    #         game__exact='ANAGRAM').order_by('-score')[:5]

    #     context['math_scores'] = GameScore.objects.filter(
    #         game__exact='MATH').order_by('-score')[:5]
    #     return context


class LeaderBoardView(ListView):
    model = GameScore
    template_name = 'games/leader-board.html'
