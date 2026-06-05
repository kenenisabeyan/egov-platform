# E-Government Platform - Backend API Documentation

## Overview

This is a comprehensive e-government platform backend built with Django REST Framework, featuring multi-tenant support, document management, and notification systems.

## Base URL

- Production: `https://api.example.com/api`
- Development: `http://localhost:8000/api`

## Authentication

All endpoints (except public ones) require JWT authentication.

### Getting a Token

```bash
POST /api/token/
{
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Using the Token

```bash
Authorization: Bearer <access_token>
```

### Refreshing the Token

```bash
POST /api/token/refresh/
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Endpoints

### Health Checks (No Auth Required)

```
GET /health/health/
GET /health/ready/
```

### Services (Public, No Auth)

List all active services with search/filter:

```
GET /api/services/?search=application&department=HR
```

Response:

```json
{
  "count": 10,
  "next": "http://localhost:8000/api/services/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "code": "APP001",
      "name": "Passport Application",
      "description": "Apply for a new passport",
      "department": "Ministry of Interior",
      "is_active": true,
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

Get service details:

```
GET /api/services/{id}/
```

### Applications (Auth Required)

Create a new application:

```
POST /api/applications/create/
{
  "service": 1,
  "full_name": "John Doe",
  "phone": "+1234567890",
  "remarks": "Additional notes"
}

Response: 201 Created
{
  "id": 1,
  "applicant": 2,
  "service": 1,
  "full_name": "John Doe",
  "phone": "+1234567890",
  "remarks": "Additional notes",
  "status": "pending",
  "submitted_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

List user's applications with filtering:

```
GET /api/applications/?status=pending&ordering=-submitted_at
```

Get application details:

```
GET /api/applications/{id}/
```

### Documents (Auth Required)

Upload a document:

```
POST /api/documents/upload/
Content-Type: multipart/form-data

{
  "application": 1,
  "document_type": "id",
  "file": <file>
}

Response: 201 Created
{
  "id": 1,
  "application": 1,
  "document_type": "id",
  "file": "https://minio.example.com/documents/abc123.pdf",
  "status": "pending",
  "verification_notes": "",
  "uploaded_at": "2024-01-15T11:00:00Z",
  "verified_at": null,
  "file_size": 2048576,
  "file_hash": "a1b2c3d4e5f6..."
}
```

List documents:

```
GET /api/documents/?application=1&status=verified
```

Get document details:

```
GET /api/documents/{id}/
```

### Notifications (Auth Required)

List user's notifications:

```
GET /api/notifications/?ordering=-created_at
```

Response:

```json
{
  "count": 5,
  "results": [
    {
      "id": 1,
      "user": 2,
      "application": 1,
      "title": "Application Received",
      "message": "Your application has been received",
      "notification_type": "application_received",
      "read": false,
      "read_at": null,
      "created_at": "2024-01-15T10:30:00Z",
      "data": {}
    }
  ]
}
```

Mark notification as read:

```
POST /api/notifications/{id}/mark_as_read/
Response: 200 OK
{
  "status": "Notification marked as read"
}
```

Mark all as read:

```
POST /api/notifications/mark_all_as_read/
Response: 200 OK
{
  "status": "All notifications marked as read"
}
```

Get unread count:

```
GET /api/notifications/unread_count/
Response: 200 OK
{
  "unread_count": 3
}
```

## Query Parameters

### Filtering

- `filterset_fields` - Exact match filters
- Example: `?status=pending&document_type=id`

### Search

- `search_fields` - Full-text search
- Example: `?search=john`

### Ordering

- `ordering` - Sort by fields (prefix with `-` for descending)
- Example: `?ordering=-created_at`

### Pagination

- `page` - Page number (default: 1)
- `limit` - Results per page (default: 20)
- Example: `?page=2&limit=50`

## Error Responses

### 400 Bad Request

```json
{
  "field_name": ["Error message"]
}
```

### 401 Unauthorized

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found

```json
{
  "detail": "Not found."
}
```

### 500 Internal Server Error

```json
{
  "detail": "Internal server error."
}
```

## Rate Limiting

Not currently implemented. Will be added in future versions.

## CORS

CORS is enabled for:

- http://localhost:3000 (development)
- http://localhost:8000 (development)
- https://yourdomain.com (production)

## WebSocket Support

Coming soon for real-time notifications.

## API Documentation

Interactive API documentation available at:

- Swagger UI: `/api/docs/`
- ReDoc: `/api/schema/` (JSON)

## Examples

### Complete Application Flow

1. **Get Services**

```bash
curl http://localhost:8000/api/services/
```

2. **Get Auth Token**

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"pass"}'
```

3. **Submit Application**

```bash
curl -X POST http://localhost:8000/api/applications/create/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"service":1,"full_name":"John","phone":"+1234"}'
```

4. **Upload Document**

```bash
curl -X POST http://localhost:8000/api/documents/upload/ \
  -H "Authorization: Bearer <token>" \
  -F "application=1" \
  -F "document_type=id" \
  -F "file=@/path/to/document.pdf"
```

5. **Check Notifications**

```bash
curl http://localhost:8000/api/notifications/ \
  -H "Authorization: Bearer <token>"
```

## WebHooks

Coming soon for external system integration.

## Versioning

Current API version: v1 (implicit)
Future versions will use `/api/v2/` prefix.

## Support

For issues and questions, visit: https://github.com/yourrepo/issues
