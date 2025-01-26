server:
	@echo "Starting server..."
	cd src && python manage.py migrate && python manage.py runserver