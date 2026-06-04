#!/bin/bash
set -e

echo "🚀 Deploying e-Gov Platform..."

if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com | sh
    sudo usermod -aG docker $USER
    echo "Reboot or re-login to apply Docker group"
fi

if ! command -v docker-compose &> /dev/null; then
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Edit .env with your secrets then run this script again."
    exit 1
fi

docker-compose pull
docker-compose up -d --build

echo "⏳ Waiting for Ollama to pull model (first time may take minutes)..."
docker-compose exec -T ollama ollama pull llama3

docker-compose exec -T backend python manage.py migrate_schemas --shared
docker-compose exec -T backend python manage.py create_tenant_schemas
docker-compose exec -T backend python manage.py collectstatic --noinput

echo "✅ Platform running at https://$(grep ALLOWED_HOSTS .env | cut -d '=' -f2 | head -1)"