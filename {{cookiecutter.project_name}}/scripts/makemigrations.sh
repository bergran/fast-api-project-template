read -p "Enter name revision : " name

alembic revision --autogenerate -m "$name"