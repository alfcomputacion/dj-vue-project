from django.urls import path
from .views import AnagramGameView, MathGameView, GameScoreView
app_name = 'games'
urlpatterns = [
    path('anagram-game/', AnagramGameView.as_view(), name='anagram-game'),
    path('math-game/', MathGameView.as_view(), name='math-game'),
    path('game-scores/', GameScoreView.as_view(), name='game-scores'),

]
