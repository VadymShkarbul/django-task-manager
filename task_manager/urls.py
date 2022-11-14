from django.urls import path

from task_manager.views import (TaskListView,
                                TagListView,
                                TagCreateView,
                                TagUpdateView,
                                TagDeleteView,
                                TaskCreateView,
                                TaskUpdateView,
                                TaskDeleteView, done_undone
                                )

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/done_undone/<int:pk>/", done_undone, name="done_undone"),
]

app_name = "task_manager"
