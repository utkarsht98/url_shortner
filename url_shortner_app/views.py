from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import UrlInfo
from .url_operations_support import generate_unique_id, generate_short_url


class UrlOperations(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def post(self, request):
        """
        :param request: Contains a long url of string type
        """
        long_url = request.data.get("longUrl")
        if long_url is None:
            return Response({"error": "Missing longUrl in requests parameter"}, status=status.HTTP_400_BAD_REQUEST)

        url = UrlInfo.objects.filter(long_url=long_url).first()

        if url:
            response_data = {"message": "Short URL already present!",
                             "shortUrl": url.short_url}
            return Response(response_data, status=status.HTTP_200_OK)

        unique_id = generate_unique_id()
        is_unique_id_present = UrlInfo.objects.filter(url_id=unique_id).exists()

        if is_unique_id_present:
            return Response({"error": "Unable to generate unique short url. Please try again!"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        short_url = generate_short_url(unique_id)

        # Instantiate the UrlInfo model
        url_info = UrlInfo(url_id=unique_id, short_url=short_url, long_url=long_url)

        url_info.save()

        response_data = {
            "message": "URL Successfully generated"
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        short_url = request.data.get("shortUrl")

        if short_url is None:
            return Response({"error": "Missing shortUrl in requests parameter"}, status=status.HTTP_400_BAD_REQUEST)

        url = UrlInfo.objects.filter(short_url=short_url).first()
        if url is None:
            return Response({"message": "Given short url does not point to any url"}, status=status.HTTP_200_OK)
        response_data = {
            "message": "Long url found!!",
            "longUrl": url.long_url
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def patch(self, request):
        short_url = request.data.get('shortUrl')
        long_url = request.data.get('longUrl')

        if short_url is None:
            return Response({"error": "Missing shorturl in requests parameter"}, status=status.HTTP_400_BAD_REQUEST)

        url = UrlInfo.objects.filter(short_url=short_url)
        if not url:
            return Response({"message": "Short url doesn't exists!"}, status=status.HTTP_400_BAD_REQUEST)
        if url.first().long_url == long_url:
            return Response({"message": "Long url already updated!"}, status=status.HTTP_200_OK)

        # Perform update operation
        url.update(long_url=long_url)
        updated_long_url = UrlInfo.objects.filter(short_url=short_url).first().long_url

        if updated_long_url != long_url:
            response_data = {
                "message": "Short url not updated. Please try again!"
            }
        else:
            response_data = {
                "message": "Short url updated!",
                "longUrl": updated_long_url
            }
        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request):
        pass
