import os

def check_document(file_path: str) -> dict:
    """
    Mock function to validate uploaded documents.
    """
    file_name = os.path.basename(file_path)
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()
    
    # Dummy mock results
    if ext in ['.pdf', '.png', '.jpg', '.jpeg']:
        return {
            'status': 'success',
            'valid': True,
            'document_name': file_name,
            'message': 'Document type is supported and signature verification passed (mocked).',
            'confidence_score': 0.95
        }
    else:
        return {
            'status': 'error',
            'valid': False,
            'document_name': file_name,
            'message': f'Unsupported document format {ext}. Only PDF and images are accepted.',
            'confidence_score': 0.0
        }
