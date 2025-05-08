


          
# THE AI CODERS - Flask Blog Platform

![AI Coders Blog](https://img.shields.io/badge/AI%20Coders-Blog%20Platform-6a3093)

A modern, responsive blog platform built with Flask, designed for AI coding enthusiasts. This platform features a sleek UI with a gradient color scheme, modern design elements, and full blog functionality.

## 📋 Features

- **Responsive Design**: Adapts seamlessly to all device sizes
- **Modern UI**: Gradient backgrounds, card-based layout, and smooth animations
- **Admin Dashboard**: Secure content management system
- **Blog Posts**: Create, edit, and delete posts with rich content
- **Contact Form**: Integrated with email notification system
- **User Authentication**: Secure login for administrators
- **File Upload**: Support for image uploads in posts
- **Pagination**: Smart pagination for blog posts

## 🛠️ Technologies Used

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: ORM for database operations
- **Flask-Mail**: For email functionality
- **Werkzeug**: For secure file uploads and utilities

### Frontend
- **Bootstrap 5**: For responsive layout and components
- **Font Awesome**: For icons
- **Custom CSS**: With variables, gradients, and animations
- **JavaScript**: For interactive elements like the navbar scroll behavior

### Database
- **MySQL**: Local database (configured for production deployment)

## 🚀 Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/ai-coders-blog.git
   cd ai-coders-blog
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the application
   - Update `config.json` with your database and email settings

5. Initialize the database
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
arpit/
├── config.json         # Configuration settings
├── main.py             # Application entry point
├── static/             # Static assets
│   ├── assets/         # Images and other assets
│   ├── css/            # CSS files
│   ├── js/             # JavaScript files
│   └── uploads/        # User uploaded files
├── templates/          # HTML templates
│   ├── about.html      # About page
│   ├── contact.html    # Contact form
│   ├── dashboard.html  # Admin dashboard
│   ├── edit.html       # Post editor
│   ├── index.html      # Homepage
│   ├── layout.html     # Base template
│   ├── login.html      # Login page
│   └── post.html       # Individual post view
└── the_ai_coders.sql   # Database schema
```

## 🔧 Configuration

The application uses a `config.json` file for configuration. Example structure:

```json
{
  "params": {
    "local_uri": "mysql://username:password@localhost/database_name",
    "prod_uri": "production_database_uri",
    "gmail-user": "your-email@gmail.com",
    "gmail-password": "your-app-password",
    "no_of_posts": 5,
    "admin_user": "admin_username",
    "admin_password": "admin_password",
    "upload_location": "static/uploads/",
    "fb_url": "https://facebook.com/yourpage",
    "tw_url": "https://twitter.com/yourhandle",
    "git_url": "https://github.com/yourusername"
  }
}
```

## 🎨 Design Features

- **Color Scheme**: Purple gradient with accent colors
- **Typography**: Poppins for body text, Raleway for headings
- **UI Elements**: 
  - Frosted glass effect cards
  - Gradient buttons with hover effects
  - Animated social media icons
  - Smart navbar that hides when scrolling down

## 📱 Responsive Behavior

The application is fully responsive with breakpoints at:
- 992px (Large devices)
- 768px (Medium devices)
- 576px (Small devices)

## 🔒 Security Features

- Password-protected admin dashboard
- Secure file upload handling
- Session-based authentication
- CSRF protection

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


© THE AI CODERS 2025 | A New Era of Coding
        
