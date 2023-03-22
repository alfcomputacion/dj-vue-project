import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers
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
    data = GameScore.objects.filter(user=request.user)
    js_data = serializers.serialize('json', data)

    return HttpResponse(js_data, content_type='application/json')


def show_ledear_board(request):
    response = list(GameScore.objects.values(
        'user__username', 'score', 'operation', 'max_number', 'game', 'created').order_by('game', '-created'))
    return JsonResponse(response, safe=False)

    # data = CustomUser.objects.filter(user__username=request.user)
    # js_data = serializers.serialize('json', data)
    # return HttpResponse(js_data, content_type='application/json')


def get_user(request):
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
