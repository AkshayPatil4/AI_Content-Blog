# AI Content Blog - Localization & REST API

## 📌 Overview

**AI Content Blog** is a Django-based application that supports multilingual content management with a REST API for handling translations. It is designed to be deployed on both bare metal and cloud environments using Docker.

## 🚀 Features

- **Django REST API** for managing translations dynamically
- **Internationalization (i18n) and localization** with language switching
- **Admin panel** for managing translations via UI
- **Dockerized setup** for easy deployment
- **CI/CD pipeline with GitHub Actions** for automated build, testing, and deployment simulation
- **For User stories** checkout projects section

## 📦 Running the Project (Using Docker)

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/AkshayPatil4/AI_Content-Blog.git
```

### 2️⃣ Build and Run the Docker Container

```sh
docker build -t my-app:latest .
docker run -d --name my-app -p 8000:8000 my-app:latest
```

This will start the Django application inside a Docker container.

### 3️⃣ Access the Application

- **Frontend & API UI:** [http://127.0.0.1:8000/]
- **Admin Panel (for managing translations):** [http://127.0.0.1:8000/admin/]

You can log in to the admin panel using the credentials:  
**Username:** `admin`  
**Password:** `admin`  

## 🏗 CI/CD Pipeline

The project includes a **GitHub Actions-based CI/CD pipeline** that:

- Builds the Docker image
- Runs tests inside a Docker container
- Simulates deployment for both bare metal and cloud environments

This ensures that the project is **production-ready at all times**.

## 📝 Notes

- The `.env` file is **not included** in the repository for security reasons.
- The project uses **Whitenoise** for serving static files in production.
- **Supports dynamic language addition** without database migrations.

## 📬 Need Help?

If you have any questions, feel free to reach out or **create an issue** in the repository.
