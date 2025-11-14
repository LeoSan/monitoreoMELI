version: '3.8'

services:
  # Django Application
  django:
    build: .
    container_name: proyecto_django
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
    env_file:
      - .env
    depends_on:
      - postgres
    networks:
      - proyecto_network

  # PostgreSQL Database
  postgres:
    image: postgres:15
    container_name: proyecto_postgres
    environment:
      POSTGRES_DB: proyecto_db
      POSTGRES_USER: django_user
      POSTGRES_PASSWORD: django_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - proyecto_network

  # pgAdmin para gestionar PostgreSQL
  pgadmin:
    image: dpage/pgadmin4
    container_name: proyecto_pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    depends_on:
      - postgres
    networks:
      - proyecto_network

volumes:
  postgres_data:

networks:
  proyecto_network:
    driver: bridge