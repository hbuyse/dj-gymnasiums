# coding=utf-8

"""urls for the dj-gymnasiums package."""


from django.urls import path

from . import views


app_name = 'dj-gymnasiums'
urlpatterns = [
    path("",
         view=views.GymnasiumListView.as_view(),
         name='list',
         ),
    path("create",
         view=views.GymnasiumCreateView.as_view(),
         name='create',
         ),
    path("<int:pk>",
         view=views.GymnasiumDetailView.as_view(),
         name='detail',
         ),
    path("<int:pk>/update",
         view=views.GymnasiumUpdateView.as_view(),
         name='post-update',
         ),
    path("<int:pk>/delete",
         view=views.GymnasiumDeleteView.as_view(),
         name='post-delete',
         )
]