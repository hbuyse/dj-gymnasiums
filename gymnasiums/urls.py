# coding=utf-8

"""urls for the dj-gymnasiums package."""


# Django
from django.urls import path

# Current django project
from gymnasiums import views

app_name = 'gymnasiums'
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
         name='update',
         ),
    path("<int:pk>/delete",
         view=views.GymnasiumDeleteView.as_view(),
         name='delete',
         )
]
