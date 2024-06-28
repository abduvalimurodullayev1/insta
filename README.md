# InstaClone

InstaClone is a web application inspired by Instagram, built using Django and Django REST Framework (DRF). The application provides a platform for users to share photos, follow other users, and interact through likes and comments.

## Features

- **User Authentication**: Sign up, login, and manage user profiles.
- **Photo Sharing**: Upload, view, and delete photos.
- **Follow System**: Follow and unfollow other users.
- **Likes and Comments**: Like photos and leave comments.
- **Feed**: View a feed of photos from followed users.

## Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abduvalimurodullayev1/insta.git
    cd insta
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Configuration

1. **Environment Variables**:
    - Create a `.env` file in the root directory and add your environment-specific variables:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

2. **Settings**:
    - Update `settings.py` to use the environment variables from your `.env` file:
    ```python
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv()

    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG') == 'True'
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
    ```

## Usage

### Uploading and Managing Photos

1. **Upload a Photo**:
    - Use the API endpoint `POST /api/photos/` to upload a photo.
    - Provide the necessary details such as description and image file.

2. **View Photos**:
    - Use the API endpoint `GET /api/photos/` to view all photos.
    - Use the API endpoint `GET /api/photos/{id}/` to view a specific photo.

3. **Like and Comment on Photos**:
    - Use the API endpoint `POST /api/photos/{id}/like/` to like a photo.
    - Use the API endpoint `POST /api/photos/{id}/comment/` to comment on a photo.

### API Endpoints

- **POST /api/photos/**: Upload a new photo.
- **GET /api/photos/**: Retrieve all photos.
- **GET /api/photos/{id}/**: Retrieve a specific photo.
- **PUT /api/photos/{id}/**: Update an existing photo.
- **DELETE /api/photos/{id}/**: Delete a photo.
- **POST /api/photos/{id}/like/**: Like a photo.
- **POST /api/photos/{id}/comment/**: Comment on a photo.
- **POST /api/follow/**: Follow a
