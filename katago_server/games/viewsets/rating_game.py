from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from katago_server.contrib.permission import ReadOnly

from katago_server.games.models import RatingGame
from katago_server.games.serializers import RatingGameCreateSerializer, RatingGameListSerializer


class RatingGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rating games to be uploaded or seen
    """

    queryset = RatingGame.objects.all()
    # TODO: that is most likely incorrect. We should allow creation and lecture (maybe with a rate limit) for unprivileged user and prevent editing
    permission_classes = [IsAdminUser | ReadOnly]

    # Used to get the proper serializer for the given action
    # so create still reference to an existing network
    # but display give nested details of the network
    def get_serializer_class(self):
        if self.action == "create":
            return RatingGameCreateSerializer
        return RatingGameListSerializer