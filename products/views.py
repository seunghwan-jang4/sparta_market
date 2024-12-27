from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product

# 전체 상품 리스트
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})

# 로그인된 사용자만 상품 추가 가능
@login_required
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
        
    return render(request, 'products/product_form.html', {'form':form})

# 로그인된 사용자만 상품의 상세정보 확인 가능
@login_required
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    return render(request, 'products/product_detail.html', {'product':product, 'user': request.user})

# 로그인된 사용자만 자신의 상품 수정 가능
@login_required
def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.user != request.user:
        return redirect('products:product_detail', pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', pk=pk)
    else:
        form = ProductForm(instance=product, initial={'hashtags_str':' '.join(ht.name for ht in product.hashtags.all())})
    return render(request, 'products/product_form.html', {'form':form, 'product':product})

# 로그인된 사용자만 자신의 상품 삭제 가능
@login_required
def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.user != request.user:
        return redirect('products:product_detail', pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('products:product_list')
    return render(request, 'products/product_detail.html', {'product':product})

# 로그인된 사용자만 상품에 좋아요 혹은 취소 가능
@login_required
def product_like_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user in product.likes.all():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)
    return redirect('products:product_detail', pk=pk)