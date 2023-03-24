from django.urls import path
from .views import AnagramGameView, MathGameView, GameScoreView, LeaderBoardView
app_name = 'games'
urlpatterns = [
    path('anagram-game/', AnagramGameView.as_view(), name='anagram-game'),
    path('math-game/', MathGameView.as_view(), name='math-game'),
    path('game-scores/math/', GameScoreView.as_view(), name='math-scores'),
    path('game-scores/anagram/', GameScoreView.as_view(), name='anagram-scores'),
    path('leader-board/math/', LeaderBoardView.as_view(), name='leader-board-math'),
    path('leader-board/anagram/', LeaderBoardView.as_view(),
         name='leader-board-anagram'),
]
