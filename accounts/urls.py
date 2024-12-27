from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  # 회원가입 페이지 URL 연결.
    path('login/', views.login_view, name = 'login'),   # 로그인 페이지 URL 연결.
    path('logout/', views.logout_view, name = 'logout'), # 로그아웃 페이지 URL 연결.
    path('profile/<str:username>/', views.profile_view, name='profile'),    # 프로필 페이지 URL 연결.
    path('profile/<str:username>/edit', views.profile_edit, name='profile_edit'),   # 프로필 수정 페이지 URL 연결.
    path('follow/<str:username>', views.follow_view, name='follow'),    # 팔로우 및 언팔로우  URL 연결.
]
