from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import mixins, GenericViewSet


class CoreCreate(mixins.CreateModelMixin, GenericViewSet):
    authentication_classes = (IsAuthenticated,)


class CoreList(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = (IsAuthenticated,)


class CoreRetrieve(mixins.RetrieveModelMixin, GenericViewSet):
    authentication_classes = (IsAuthenticated,)


class CoreUpdate(mixins.UpdateModelMixin, GenericViewSet):
    authentication_classes = (IsAuthenticated,)


class CoreDestroy(mixins.DestroyModelMixin, GenericViewSet):
    authentication_classes = (IsAuthenticated,)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
