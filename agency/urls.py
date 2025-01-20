from django.urls import path

from .views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
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
    # path("cars/", CarListView.as_view(), name="car-list"),
    # path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    # path("cars/create/", CarCreateView.as_view(), name="car-create"),
    # path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    # path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
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
