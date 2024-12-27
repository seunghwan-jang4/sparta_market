from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list_view, name='product_list'), # 상품 목록 페이지 연결.
    path('create/', views.product_create_view, name='product_create'),  # 상품 생성 페이지 연결.
    path('<int:pk>/', views.product_detail_view, name='product_detail'),  # 특정 상품 상세 페이지 연결.
    path('<int:pk>/update/', views.product_update_view, name='product_update'), # 상품 수정 페이지 연결.
    path('<int:pk>/delete/', views.product_delete_view, name='product_delete'), # 상품 삭제 페이지 연결.
    path('<int:pk>/like/', views.product_like_view, name='product_like'), # 상품 좋아요 및 취소 처리.
]


