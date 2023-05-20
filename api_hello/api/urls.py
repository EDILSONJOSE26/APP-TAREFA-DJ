from django.urls import path
from . import views

from api.views import TarefasDeletarAtualizar, CriarTarefas, UserSignup
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatters = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserSignup.as_view()),
    path('tarefas', CriarTarefas.as_view(), name='CriarTarefas'),
    path('tarefas/<int:pk>', TarefasDeletarAtualizar.as_view(),
         name='TarefasDeletarAtualizar')
]


