from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .ollama_client import ask_llama3
from .document_checker import check_document
from django.core.files.storage import default_storage

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    message = request.data.get('message')
    conversation = request.data.get('conversation', [])
    context = request.data.get('context', '')
    if not message:
        return Response({'error': 'No message'}, status=400)
    
    prompt = f"Previous conversation: {conversation}\nCitizen asks: {message}\nContext: {context}\nAnswer politely, concisely, in the same language."
    reply = ask_llama3(prompt)
    return Response({'reply': reply})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_uploaded_document(request):
    file = request.FILES.get('document')
    if not file:
        return Response({'error': 'No file'}, status=400)
    file_path = default_storage.save(f'temp/{file.name}', file)
    result = check_document(file_path)
    default_storage.delete(file_path)
    return Response(result)