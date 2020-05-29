# from django.shortcuts import render
# from django.views.generic import View
# from .models import Post

# # Create your views here.
# class AddRegister(View):
#     def get(self,request):
#     	posts= Post.objects.all()
#     	printf(posts)
#         # return addRegDef(request.GET['name'],request.GET['comment'],request.GET['upVote'],
#         # request.GET['downVote'])
#     # def post(self,request):	
#     #     return addRegDef(request.POST['name'],request.POST['comment'],request.POST['upVote'],
#     #     request.POST['downVote'])


# from django.shortcuts import render
# from .models import Post

# def post_list(request):
#     posts = Post.objects.all()
#     printf(posts)

from rest_framework import viewsets

from .serializers import PostSerializer,CommentSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('name')
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.values('name', 'comment')
    serializer_class = CommentSerializer
