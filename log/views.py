import logging
import telebot
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny
from Event import settings

logger = logging.getLogger(__name__)
TOKEN = "7983847767:AAE1_ZnraRb3vSBJzMO_qRzCwE3rBMT3eV0"
TELEGRAM_ID = 7526654310
bot = telebot.TeleBot(TOKEN)


# ------------------------ Device Log ------------------------------
class DeviceLogEventView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        headers = dict(request.headers)
        data = request.data
        files = request.FILES
        ip = request.META.get("REMOTE_ADDR")
        print(f"headers {headers}\ndata: {data}\nfiles: {files}\n ip: {ip}")
        bot.send_message(chat_id=TELEGRAM_ID, text=str(data))

        for file_name, file in files.items():
            bot.send_document(chat_id=TELEGRAM_ID, document=file)

        return Response({"status": "received"})


# ------------------------------- Program Log ------------------------------
class ProgramLogEventView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        headers = dict(request.headers)
        data = request.data
        secret_key = request.META.get("REMOTE_ADDR")
        if secret_key != settings.DEVICE_SECRET_KEY:
            raise RuntimeError(status.HTTP_401_UNAUTHORIZED)

        print(f"headers {headers}\ndata: {data}\n")
        bot.send_message(chat_id=TELEGRAM_ID, text=str(data))










# ----------------------------------------------------------------------------------->
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
