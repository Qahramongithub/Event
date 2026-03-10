import json
import logging

import telebot
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)
TOKEN = "7983847767:AAE1_ZnraRb3vSBJzMO_qRzCwE3rBMT3eV0"
TELEGRAM_ID = 7526654310
bot = telebot.TeleBot(TOKEN)


class LogEventView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        json_data = request.data
        secret_key = request.headers.get("X-API-KEY")
        # if secret_key != settings.DEVICE_SECRET_KEY or not secret_key:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        event_data = json.loads(json_data)
        print(f"Json Data {json_data}")

        print(f"Event Data{event_data}")
        bot.send_message(chat_id=TELEGRAM_ID, text=json_data)

        return Response({"status": "ok"}, status=status.HTTP_200_OK)

#----------------------------------------------------------------------------------->
# class LogEventView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [AllowAny]
#
#     def post(self, request, format=None):
#         json_string = None
#         for k, v in request.data.items():
#             if k != "Picture" and "eventType" in str(v):
#                 json_string = v
#                 break
#
#         if not json_string:
#             return Response(
#                 {"error": "No valid event JSON found."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         try:
#             event_data = json.loads(json_string)
#         except Exception as e:
#             return Response({"error": f"Invalid JSON: {e}"}, status=status.HTTP_400_BAD_REQUEST)
#
#         bot.send_message(chat_id=TELEGRAM_ID, text=event_data)
#
#         return Response({"status": "ok"}, status=status.HTTP_200_OK)
