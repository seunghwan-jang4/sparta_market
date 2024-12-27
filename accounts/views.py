from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProflieForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from products.models import Product

# 회원가입 기능
def signup_view(request):
    if request.method == "POST":  # POST 요청일 경우 회원가입.
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():  # 입력 데이터가 유효하다면,
            user = form.save()  # 유저를 생성하고 저장.
            login(request, user)  # 새로 생성된 유저로 로그인.
            return redirect('products:product_list')  # 상품 목록 페이지로 리디렉션.
    else:  # GET 요청일 경우 회원가입 폼 제공.
        form = SignupForm()
        
    return render(request, 'accounts/signup.html', {'form': form})  # 회원가입 페이지 렌더링.

# 로그인 기능
def login_view(request):
    if request.user.is_authenticated:   # 이미 로그인 상태면, 상품 목록 페이지로 리디렉션.
        return redirect('products:product_list')
    
    if request.metod == "post":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('products:product_list')
    else:
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {'form': form})

# 로그아웃 기능
@login_required
def logout_view(request):
    logout(request) 
    return redirect('accounts:login')  # 로그아웃 후 로그인 페이지로 리디렉션.

# 사용자 프로필 페이지
@login_required 
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    # 등록 물품
    my_products = Product.objects.filter(user=profile_user)
    # 찜한 물품
    liked_products = profile_user.liked_products.all()
    # 팔로잉 여부
    is_following = request.user.follows.filter(pk=profile_user.pk).exists()
    
    context = {
        'profile_user': profile_user,
        'my_products': my_products,
        'liked_products': liked_products,
        'is_following': is_following,
    }
    return render(request, 'accounts/profile.html', context)

# 프로필 수정
@login_required
def profile_edit(request, username):
    if request.user.username != username:
        return redirect('accounts:profile', username=username)

    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        form = ProflieForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', username=username)
    else:
        form = ProflieForm(instance=user)

    return render(request, 'accounts/profile_edit.html', {'form': form})

# 팔로우 및 언팔로우
def follow_view(request, username):
    target_user = get_object_or_404(User, username=username)
    if target_user != request.user:
        # 팔로우가 되어 있는 상태 -> 1
        if request.user.follows.filter(pk=target_user.pk).exists():
            # 취소하는 버튼 생성
            request.user.follows.remove(target_user)
        else:
            request.user.follows.add(target_user)
    return redirect('accounts:profile', username=username)