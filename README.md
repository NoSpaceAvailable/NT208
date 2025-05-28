Project structure
=================

**Note for dev: Dev frontend thì nếu chạy build.sh trực tiếp, docker sẽ báo vite not found. Lí do là vì docker-compose.yml đang thực hiện volumn ./frontend:/app/frontend. Vì vậy khi dev frontend cần install dependencies trong package.json của frontend trước rồi mới ./build.sh**

```text
.
├── README.md                       # Overview of the virtual asset marketplace platform and setup guide
├── TODO.md                         # Pending tasks and feature roadmap for the platform
├── backend                         # Backend logic for the virtual asset marketplace
│   ├── Dockerfile                  # Docker configuration to containerize the backend
│   ├── app                         # Core application logic
│   │   ├── __init__.py             # Initializes the backend application module
│   │   ├── global_config.py        # Centralized configuration for global settings (e.g., API keys, secrets)
│   │   ├── models                  # Database models for the platform
│   │   │   ├── Chatbot.py          # Model for AI chatbot functionality and support
│   │   │   ├── Database.py         # Handles database connections and ORM setup
│   │   │   ├── Product.py          # Model for virtual assets (e.g., game items, accounts, CD-Keys)
│   │   │   ├── Reputation.py       # Model for user reputation and rating system
│   │   │   ├── Transaction.py      # Model for buy/sell transactions and escrow system
│   │   │   ├── User.py             # Model for user accounts and authentication
│   │   │   ├── UserProfile.py      # Model for user profile data (e.g., avatars, personal info)
│   │   │   └── __init__.py         # Initializes the models module
│   │   ├── routes                  # API endpoints for the platform
│   │   │   ├── auth.py             # Handles user authentication (register, login, 2FA)
│   │   │   ├── bot.py              # Endpoints for AI chatbot interactions
│   │   │   ├── healthcheck.py      # Health check endpoint for monitoring
│   │   │   ├── products.py         # Endpoints for product listings, search, and details
│   │   │   ├── reputation.py       # Endpoints for reputation and rating system
│   │   │   └── transactions.py     # Endpoints for buy/sell transactions and escrow
│   │   ├── services                # Business logic and service layer
│   │   │   ├── auth_service.py     # Handles authentication logic (email, Google, Facebook)
│   │   │   ├── bot_service.py      # Logic for AI chatbot and fraud detection
│   │   │   ├── mail_service.py     # Handles email notifications and verification
│   │   │   ├── product_service.py  # Logic for product listings, auctions, and filtering
│   │   │   ├── reputation_service.py       # Logic for reputation scoring and fraud prevention
│   │   │   └── transaction_service.py      # Logic for transactions, escrow, and blockchain integration
│   │   └── utils                   # Utility functions and helpers
│   │       ├── blockchain.py       # Handles blockchain integration for secure transactions
│   │       ├── cookie.py           # Manages user cookies and sessions
│   │       ├── deepseek.py         # Integration with Deepseek for advanced analytics
│   │       ├── logging.py          # Centralized logging configuration
│   │       └── notifications.py    # Handles real-time notifications (orders, messages)
│   ├── requirements.txt            # Python dependencies for the backend
│   └── run.py                      # Entry point to start the backend server
├── build.sh                        # Script to build and deploy the platform
├── db                              # Database-related files
│   └── data                        # Directory for storing database data [error opening dir]
├── docker-compose.yml              # Docker Compose configuration for multi-container setup (backend, frontend, nginx)
├── frontend                        # Frontend code for the marketplace platform
│   ├── Dockerfile                  # Docker configuration to containerize the frontend
│   ├── README.md                   # Frontend setup and development guide
│   ├── dist                        # Compiled frontend assets for production
│   │   ├── assets                  # Compiled CSS, JS, and other assets
│   │   ├── favicon.ico             # Favicon for the platform
│   │   └── index.html              # Main HTML file for the production build
│   ├── frontend                    # Duplicate frontend folder (likely unnecessary)
│   ├── index.html                  # Main HTML file for development
│   ├── jsconfig.json               # JavaScript configuration for the frontend
│   ├── package-lock.json           # Lock file for npm dependencies
│   ├── package.json                # Frontend dependencies and scripts
│   ├── public                      # Static public assets
│   │   └── favicon.ico             # Favicon for the platform
│   ├── src                         # Frontend source code
│   │   ├── App.vue                 # Root Vue component for the application
│   │   ├── assets                  # Static assets (CSS, images, etc.)
│   │   │   ├── base.css            # Base CSS styles for the platform
│   │   │   ├── logo.svg            # Platform logo
│   │   │   └── main.css            # Main CSS styles for the platform
│   │   ├── components              # Vue components for the platform
│   │   │   ├── 404.vue             # 404 error page component
│   │   │   ├── AuthPage.vue        # Authentication page (login, register, 2FA)
│   │   │   ├── Footer.vue          # Footer component for the platform
│   │   │   ├── MainPage.vue        # Main landing page component
│   │   │   ├── NavBar.vue          # Navigation bar component
│   │   │   ├── VerifyPage.vue      # Account verification page component
│   │   │   └── icons               # Icon components for social media and UI
│   │   │       ├── IconDiscord.vue     # Discord icon component
│   │   │       ├── IconFacebook.vue    # Facebook icon component
│   │   │       ├── IconInstagram.vue   # Instagram icon component
│   │   │       ├── IconTiktok.vue      # TikTok icon component
│   │   │       └── IconX.vue           # X (Twitter) icon component
│   │   ├── main.js                 # Entry point for the frontend application
│   │   ├── router                  # Vue router configuration
│   │   │   └── router.js           # Defines routes for the platform (e.g., products, auth)
│   │   ├── services                # Frontend services for API calls and state management
│   │   │   ├── api.js              # Handles API communication with the backend
│   │   │   └── auth.js             # Manages authentication state and tokens
│   │   └── store                   # Vuex store for global state management
│   │       ├── auth.js             # Manages authentication state (e.g., logged-in user)
│   │       ├── index.js            # Main Vuex store configuration
│   │       └── products.js         # Manages product-related state (e.g., listings, auctions)
│   └── vite.config.js              # Vite configuration for frontend development
└── nginx                           # Nginx configuration for reverse proxy and load balancing
    ├── Dockerfile                  # Docker configuration for Nginx
    └── nginx.conf                  # Nginx configuration file for routing and SSL
```

Credit card for testing:
- Card number: 5200 0000 0000 1096
- Expiration date: 05/55
- CVV: 333
- Name: Nguyen Van A
