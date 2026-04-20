from datetime import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import BlogModelForm, CommentModelForm
from .models import BlogPost, Comment , ContactMessage


def home(request):
    latest_blogs = BlogPost.objects.order_by("-date_published")[:3]

    context = {
        "latest_blogs": latest_blogs,
        "title": "Главная страница",
        "site_description": "Добро пожаловать в наш блог! Здесь вы найдете свежие новости и статьи."
    }
    return render(request, "blog/home.html", context)


def index(request):
    blogs = BlogPost.objects.all()


    search = request.GET.get("search")
    if search:
        blogs = blogs.filter(title__icontains=search)


    date = request.GET.get("date")
    if date:
        try:
            blogs = blogs.filter(date_published__date=date)
        except ValueError:
            pass


    sort = request.GET.get("sort") or "-date_published"
    blogs = blogs.order_by(sort)


    no_results_by_date = False
    if date and blogs.count() == 0:
        no_results_by_date = True


    paginator = Paginator(blogs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/blog_list.html", {
        "page_obj": page_obj,
        "search": search or "",
        "sort": sort,
        "date": date or "",
        "no_results_by_date": no_results_by_date,
    })


def detail(request, pk):
    try:
        blog = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return render(
            request,
            "blog/blog_detail.html",
            {"exception": "Такого блога не существует"},
        )

    blogs = BlogPost.objects.all()
    title = blog.title

    count = str(request.GET.get("post"))
    comments = Comment.objects.filter(blog=blog).order_by("-date_published")


    if count == "prev":
        if blog.id == blogs.first().id:
            return redirect("blog:blog_detail", pk=blogs.last().id)
        prev_blog = blogs.filter(id__lt=blog.id).last()
        return redirect("blog:blog_detail", pk=prev_blog.id)


    if count == "next":
        if blog.id == blogs.last().id:
            return redirect("blog:blog_detail", pk=blogs.first().id)
        next_blog = blogs.filter(id__gt=blog.id).first()
        return redirect("blog:blog_detail", pk=next_blog.id)

    context = {"blog": blog, "title": title, "comments": comments}

    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.date_published = datetime.now()
            new_comment.blog = blog
            new_comment.save()
            return redirect("blog:blog_detail", pk=pk)
    else:
        form = CommentModelForm()

    context["form"] = form

    return render(request, "blog/blog_detail.html", context)



def is_owner(func):
    def wrapper(request, *args, **kwargs):
        blog_id = kwargs["pk"]
        if blog_id:
            blog = BlogPost.objects.get(pk=blog_id)
            if blog.author == request.user or request.user.is_superuser:
                return func(request, *args, **kwargs)
        return redirect("blog:index")
    return wrapper


@permission_required("blog.add_blogpost")
@login_required
def create_blog(request):
    title = "Создание блога"
    action = "Создать"

    if request.method == "POST":
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.date_published = datetime.now()
            new_blog.save()
            return redirect("blog:index")
    else:
        form = BlogModelForm()

    return render(
        request,
        "blog/create_update_blog.html",
        {"title": title, "form": form, "action": action},
    )


@is_owner
@login_required
def update_blog(request, pk):
    action = "Обновить"
    blog = BlogPost.objects.get(pk=pk)
    title = f"Редактирование {blog.title}"

    if request.method == "POST":
        form = BlogModelForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blog:blog_detail", pk=pk)
    else:
        form = BlogModelForm(instance=blog)

    return render(
        request,
        "blog/create_update_blog.html",
        {"title": title, "form": form, "action": action},
    )


@is_owner
@login_required
def delete_blog(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    blog.delete()
    return redirect("blog:index")



def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Сообщение отправлено!")
        return redirect("blog:contacts")

    return render(request, "blog/contacts.html")
