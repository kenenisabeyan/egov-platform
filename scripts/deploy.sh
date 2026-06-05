#!/bin/bash
set -e

echo "🚀 Deploying e-Gov Platform..."

if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com | sh
    sudo usermod -aG docker $USER
    echo "Reboot or re-login to apply Docker group"
fi

if ! command -v docker-compose &> /dev/null && ! command -v "docker" &> /dev/null; then
    echo "Docker is required but not installed. Please install Docker Desktop or Docker Engine first."
    exit 1
fi

COMPOSE_CMD=""
if command -v docker-compose &> /dev/null; then
    COMPOSE_CMD="docker-compose"
elif command -v docker &> /dev/null; then
    COMPOSE_CMD="docker compose"
else
    echo "No Docker Compose CLI available."
    exit 1
fi

if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Edit .env with your secrets then run this script again."
    exit 1
fi

$COMPOSE_CMD pull
$COMPOSE_CMD up -d --build

echo "⏳ Waiting for Ollama to pull model (first time may take minutes)..."
$COMPOSE_CMD exec -T ollama ollama pull llama3

$COMPOSE_CMD exec -T backend python manage.py migrate_schemas --shared
$COMPOSE_CMD exec -T backend python manage.py create_tenant_schemas
$COMPOSE_CMD exec -T backend python manage.py collectstatic --noinput

echo "✅ Platform running at https://$(grep ALLOWED_HOSTS .env | cut -d '=' -f2 | head -1)"