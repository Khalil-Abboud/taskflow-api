
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
# from django.db.models import Q
# Create your views here.

# @api_view(['GET'])
# def health_check(request):
#     return Response({'status':'ok'})

# @api_view(['GET','POST'])
# def task_list (request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         status = request.GET.get('status')
#         priority = request.GET.get('priority')
#         search = request.GET.get('search')
#         ordering = request.GET.get('ordering')
#         if status:
#             tasks = tasks.filter(status=status)
#         if priority:
#             tasks = tasks.filter(priority=priority)
#         if search:
#             tasks = tasks.filter(Q(title__icontains=search)|Q(description__icontains=search))
#         if ordering:
#             tasks =tasks.order_by(ordering)
#         page = request.GET.get('page',1)
#         page_size = 5
#         start = (int(page)-1)*page_size
#         end = start+page_size
#         paginated_tasks = tasks[start:end]
#         serializer = TaskSerializer(paginated_tasks, many=True)
#         return Response({
#             'count':tasks.count(),
#             'page':int(page),
#             'results':serializer.data
#         })
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
# @api_view(['GET','PATCH','DELETE'])
# def task_detail(request,pk):
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response({'error':'Task not found'})
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = TaskSerializer(task, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method == "DELETE":
#         task.delete()
#         return Response({'message':'Task deleted'})

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer