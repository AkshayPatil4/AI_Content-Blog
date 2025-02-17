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
**Password:** `admin123`  

### Adding new Translations
- Click on Add translation in admin panel.
- Example:  add code for language (e.g. hi)  for HINDI.
- Add JSON data    {
  "English": "अंग्रेज़ी",
  "Arabic": "अरबी",
  "AI Blog": "एआई ब्लॉग",
  "Welcome to AI Blog": "एआई ब्लॉग में आपका स्वागत है",
  "All rights reserved.": "सर्वाधिकार सुरक्षित।",
  "Latest AI Articles": "नवीनतम एआई लेख",
  "The Future of AI": "एआई का भविष्य",
  "Artificial Intelligence is evolving rapidly and impacting various industries. From healthcare to finance, AI is transforming the way we work and live.": "कृत्रिम बुद्धिमत्ता तेजी से विकसित हो रही है और विभिन्न उद्योगों पर प्रभाव डाल रही है। स्वास्थ्य सेवा से लेकर वित्त तक, एआई हमारे काम करने और जीने के तरीके को बदल रहा है।",
  "AI in Healthcare": "स्वास्थ्य सेवा में एआई",
  "AI is being used to diagnose diseases, develop personalized treatments, and even assist in surgeries. The potential of AI in medicine is limitless.": "एआई का उपयोग बीमारियों का निदान करने, व्यक्तिगत उपचार विकसित करने और यहां तक कि सर्जरी में सहायता करने के लिए किया जा रहा है। चिकित्सा में एआई की संभावनाएं असीमित हैं।",
  "The Role of AI in Automation": "स्वचालन में एआई की भूमिका",
  "Automation powered by AI is revolutionizing industries by improving efficiency and reducing human effort in repetitive tasks.": "एआई द्वारा संचालित स्वचालन उद्योगों में क्रांति ला रहा है, जिससे दक्षता में सुधार हो रहा है और दोहराए जाने वाले कार्यों में मानव प्रयास कम हो रहा है।"
}
)
 and click send.

- Check for new language additions on  [http://127.0.0.1:8000/]  language dropdown.

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
