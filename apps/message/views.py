from rest_framework import generics
from rest_framework import permissions, response
from .models import TelegramMessage
from .serializers import TelegramMessageSerializer
from apps.bot.utils import send_message_to_telegram_bot


class TelegramMessageListView(generics.GenericAPIView):
    queryset = TelegramMessage.objects.all()
    serializer_class = TelegramMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = request.user
        message = request.data['message']
        status = send_message_to_telegram_bot(user.telegram_token, message)
        if status == 400:
            return response.Response('token not found', 400)
        
        serializer.save(user=user)
        return response.Response('сообщение отправлено успешно', 200)

    def get(self, request):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)