from django.urls import path

from .views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create",
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update",
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    # path(
    #     "cars/<int:pk>/toggle-assign/",
    #     toggle_assign_to_car,
    #     name="toggle-car-assign",
    # ),
    # path("drivers/", DriverListView.as_view(), name="driver-list"),
    # path(
    #     "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    # ),
    # path("drivers/", DriverListView.as_view(), name="driver-list"),
    # path(
    #     "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    # ),
    # path("drivers/create/", DriverCreateView.as_view(), name="driver-create"),
    # path(
    #     "drivers/<int:pk>/update/",
    #     DriverLicenseUpdateView.as_view(),
    #     name="driver-update",
    # ),
    # path(
    #     "drivers/<int:pk>/delete/",
    #     DriverDeleteView.as_view(),
    #     name="driver-delete",
    # ),
]

app_name = "agency"
