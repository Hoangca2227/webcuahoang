# Chuyển Đổi Số Giáo Dục Tỉnh Hòa Bình

This is a Django-based website that replicates the UI of the official "Digital Transformation in Education for Hoa Binh Province" website.

## Features

- Modern, responsive UI that closely matches the original website
- Interactive circular services display
- Detailed information about each digital education service
- Built with Django and Python

## Requirements

- Python 3.9+
- Django 5.0.3+
- Pillow library for image processing

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/hoa-binh-education.git
   cd hoa-binh-education
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Load initial data:
   ```
   python manage.py loaddata education_portal/fixtures/initial_data.json
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Visit http://localhost:8000 in your browser

## Docker Installation

Alternatively, you can use Docker:

```
docker-compose up
```

## Structure

- `education_portal/`: Main Django app
- `static/`: Static files (CSS, JavaScript, images)
- `media/`: User-uploaded content
- `templates/`: Django HTML templates

## License

This project is for educational purposes only.
