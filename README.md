Project structure
=================

```text
project-root/
├── docker-compose.yml                           # Docker Compose configuration for all services
├── install.sh                                   # Script to initialize and start the project
├── nginx/
│   ├── Dockerfile                               # Dockerfile for Nginx
│   └── nginx.conf                               # Nginx configuration file
├── backend/
│   ├── Dockerfile                               # Dockerfile for Flask backend
│   ├── requirements.txt                         # Python dependencies for Flask
│   ├── app/
│   │   ├── __init__.py                          # Flask app initialization
│   │   ├── models/                              # Database models (SQLAlchemy)
│   │   │   ├── User.py                          # User model
│   │   │   ├── Product.py                       # Product model
│   │   │   ├── Transaction.py                   # Transaction model
│   │   │   └── Reputation.py                    # Reputation model
│   │   ├── routes/                              # API routes
│   │   │   ├── auth.py                          # Authentication routes (register, login, 2FA)
│   │   │   ├── products.py                      # Product-related routes (search, post, buy)
│   │   │   ├── transactions.py                  # Transaction routes (order history, escrow)
│   │   │   └── reputation.py                    # Reputation routes (ratings, comments)
│   │   ├── services/                            # Business logic
│   │   │   ├── auth_service.py                  # Handles authentication logic
│   │   │   ├── product_service.py               # Handles product-related logic
│   │   │   ├── transaction_service.py           # Handles transaction logic
│   │   │   └── reputation_service.py            # Handles reputation logic
│   │   ├── utils/                               # Utility functions
│   │   │   ├── deepseek.py                      # AI fraud detection logic
│   │   │   ├── blockchain.py                    # Blockchain integration for transactions
│   │   │   └── notifications.py                 # Real-time notification logic
│   │   └── config.py                            # Configuration settings (e.g., database, secrets)
│   └── run.py                                   # Entry point for Flask app
├── frontend/
│   ├── Dockerfile                               # Dockerfile for Vue.js frontend
│   ├── public/
│   │   ├── index.html                           # Base HTML file
│   │   └── favicon.ico                          # Favicon
│   ├── src/
│   │   ├── assets/
│   │   │   ├── logo.png                         # Logo image
│   │   │   └── styles.css                       # Global CSS styles
│   │   ├── components/
│   │   │   ├── NavBar.vue                       # Navigation bar component
│   │   │   ├── ProductCard.vue                  # Product card component
│   │   │   └── Rating.vue                       # Rating component for reviews
│   │   ├── views/
│   │   │   ├── Home.vue                         # Home page
│   │   │   ├── Profile.vue                      # User profile page
│   │   │   ├── ProductDetail.vue                # Product details page
│   │   │   └── Transactions.vue                 # Transaction history page
│   │   ├── router/
│   │   │   └── index.js                         # Vue Router configuration
│   │   ├── store/
│   │   │   ├── index.js                         # Vuex store initialization
│   │   │   ├── auth.js                          # Authentication state management
│   │   │   └── products.js                      # Product state management
│   │   ├── services/
│   │   │   ├── api.js                           # Axios instance for API calls
│   │   │   └── auth.js                          # Authentication service
│   │   ├── App.vue                              # Root Vue component
│   │   └── main.js                              # Entry point for Vue app
│   ├── index.html                               # Base HTML file
│   ├── package.json                             # Frontend dependencies and scripts
│   └── vite.config.js                           # Vite configuration
└── db/
    ├── init.sql                                 # SQL script to initialize the database
    └── data/                                    # Persistent PostgreSQL data (mounted volume)
```