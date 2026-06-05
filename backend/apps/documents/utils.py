import hashlib
import mimetypes
from pathlib import Path
from django.core.files.uploadedfile import UploadedFile


def validate_document_file(file: UploadedFile) -> dict:
    """Validate document file - size, type, and integrity."""
    ALLOWED_MIMETYPES = {
        'application/pdf': 'pdf',
        'image/jpeg': 'jpg',
        'image/png': 'png',
        'image/x-windows-bmp': 'bmp',
        'application/msword': 'doc',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
    }
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

    mimetype = mimetypes.guess_type(file.name)[0] or 'application/octet-stream'
    file_ext = Path(file.name).suffix.lower()

    errors = []
    if file.size > MAX_FILE_SIZE:
        errors.append(f'File size exceeds maximum allowed (10MB). Received: {file.size / 1024 / 1024:.2f}MB')
    if mimetype not in ALLOWED_MIMETYPES:
        errors.append(f'File type not allowed: {mimetype}')

    if errors:
        return {'valid': False, 'errors': errors, 'file_hash': None}

    # Calculate file hash
    file_hash = hashlib.sha256()
    for chunk in file.chunks():
        file_hash.update(chunk)
    file_hash_hex = file_hash.hexdigest()

    return {
        'valid': True,
        'errors': [],
        'file_hash': file_hash_hex,
        'file_size': file.size,
        'mimetype': mimetype,
    }


def extract_document_metadata(file_path: str) -> dict:
    """Extract metadata from document."""
    path = Path(file_path)
    try:
        size = path.stat().st_size
        ext = path.suffix.lower()
        return {
            'size': size,
            'extension': ext,
            'exists': path.exists(),
        }
    except Exception as e:
        return {'error': str(e)}
