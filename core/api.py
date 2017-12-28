"""Api endpoints for retrieving images and their grades."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EyeLidKeyGradeList(APIView):
    """API endpoint for requesting lists of eyelid s3 keys and grades.

    Returned list:
    {
        'bucket_name': ...,
        's3_keys': [k_1, k_2, ...k_n]
        'grades': [(k_1 grades...), (k_2 grades...) ...]
    }

    Each image can have 0 or more corresponding grades.
    """

    def get(self, request, format=None):
        """Get a list of all the images and their gradies."""

        # TODO: return actual data.
        dummy_data = {
            'images': [1, 2, 3, 4]
        }

        return Response(dummy_data, status=status.HTTP_200_OK)
