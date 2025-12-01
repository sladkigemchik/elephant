from django.shortcuts import render, redirect
from .models import Employee, Service, Post

def main(request):
    print("=" * 50)
    print("DEBUG: main view called")
    
    # Получаем ВСЕ записи без фильтрации
    all_posts = Post.objects.all()
    print(f"DEBUG: Все записи в базе: {all_posts.count()}")
    
    for post in all_posts:
        print(f"  - ID: {post.id}, Title: '{post.title}', Published: {post.is_published}")
    
    # Теперь с фильтром
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    print(f"DEBUG: Опубликованные записи: {posts.count()}")
    
    # Обработка формы
    if request.method == 'POST':
        print("DEBUG: POST запрос получен")
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        # Сохраняем запись
        post = Post(
            title=title,
            content=content,
            author=request.user if request.user.is_authenticated else None,
            is_published=True  # Убедитесь, что это True!
        )
        post.save()
        print(f"DEBUG: Запись сохранена. ID: {post.id}, Title: '{post.title}'")
        
        # Обновляем список записей после сохранения
        posts = Post.objects.filter(is_published=True).order_by('-created_at')
        print(f"DEBUG: Теперь опубликованных записей: {posts.count()}")
        
        return redirect('main')
    
    context = {
        'posts': posts,
        'services': Service.objects.filter(is_active=True),
        'employees': Employee.objects.filter(is_active=True),
    }
    
    print(f"DEBUG: Отправляем в шаблон {len(posts)} записей")
    print("=" * 50)
    return render(request, 'main.html', context)
def services(request):
    services_list = Service.objects.filter(is_active=True)
    return render(request, 'services.html', {'services': services_list})

def team(request):
    employees = Employee.objects.filter(is_active=True)
    return render(request, 'team.html', {'employees': employees})

def news(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'news.html', {'posts': posts})