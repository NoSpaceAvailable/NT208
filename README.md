# Almacenar - Virtual Asset Marketplace Platform

Almacenar is an online marketplace designed for trading virtual assets, with a focus on items like CS:GO skins. The platform also supports merchandise sales and skin auctions. It utilizes Docker for a containerized environment, making setup and deployment more manageable.

## Project builders
Group 10:
- 23520197: Lê Quốc Cường
- 23521789: Hoàng Xuân Vinh
- 23521134: Ngô Trần Anh Ninh

## Workflow

![a](https://github.com/user-attachments/assets/5f5deed6-0884-4a9b-bf7e-a53edf5c33c0)

## Project Structure

```txt
.
├── README.md                       # This file: Overview and setup guide.
├── backend                         # Backend application (Flask)
│   ├── Dockerfile                  # Docker configuration for the backend.
│   ├── app                         # Core backend application logic.
│   │   ├── init.py                 # Initializes the Flask app, registers blueprints, and sets up CORS and limiter.
│   │   ├── global_config.py        # Centralized configuration (DB, JWT, OAuth, API keys, etc.).
│   │   ├── misc                    # Miscellaneous supporting files for the backend.
│   │   │   ├── featured.json       # Data for featured items on the platform.
│   │   │   ├── init.sql            # SQL script for initial database schema and data population (e.g., items).
│   │   │   ├── sitemap.xml         # Sitemap for SEO.
│   │   │   └── skin_data.json      # Detailed skin data, likely for pricing or attributes.
│   │   ├── models                  # SQLAlchemy ORM models for database tables.
│   │   │   ├── init.py             # Initializes database models and creates tables.
│   │   │   ├── Chatbot.py          # Model/logic for AI chatbot (AlmaBot).
│   │   │   ├── Database.py         # Database connection setup and session management.
│   │   │   ├── History.py          # Model for transaction/activity history.
│   │   │   ├── Items.py            # Model for marketable items (skins, etc.).
│   │   │   ├── Notifications.py    # Model for user notifications.
│   │   │   ├── User.py             # Model for user accounts and authentication.
│   │   │   ├── UserItems.py        # Model linking users to their items (inventory).
│   │   │   ├── UserProfile.py      # Model for extended user profile information.
│   │   │   ├── Wallet.py           # Model for user wallets and balances.
│   │   │   └── enumtypes           # Enum definitions for various model attributes.
│   │   │       ├── HistoryStatus.py
│   │   │       ├── HistoryType.py
│   │   │       ├── ItemCollection.py
│   │   │       ├── ItemExterior.py
│   │   │       ├── ItemKind.py
│   │   │       ├── ItemRarity.py
│   │   │       └── ItemType.py
│   │   ├── routes                  # API endpoint definitions (Flask Blueprints).
│   │   │   ├── auth.py             # Authentication routes (register, login, verify, OAuth).
│   │   │   ├── bot.py              # Chatbot interaction endpoint.
│   │   │   ├── healthcheck.py      # Health check and sitemap endpoints.
│   │   │   ├── notification.py     # User notification routes.
│   │   │   ├── products.py         # Product/item related routes (list, inventory, buy, sell).
│   │   │   ├── profile.py          # User profile management routes.
│   │   │   └── transactions.py     # Transaction and wallet management routes.
│   │   ├── services                # Business logic layer.
│   │   │   ├── auth_service.py     # Authentication logic.
│   │   │   ├── bot_service.py      # Chatbot service logic.
│   │   │   ├── history_service.py  # History logging service.
│   │   │   ├── mail_service.py     # Email sending service (e.g., for verification).
│   │   │   ├── notification_service.py # Notification management service.
│   │   │   ├── product_service.py          # Product and inventory management logic.
│   │   │   ├── profile_service.py          # User profile business logic.
│   │   │   ├── transaction_service.py      # Transaction and wallet business logic.
│   │   │   └── user_service.py     # User data retrieval service.
│   │   └── utils                   # Utility functions and helpers.
│   │       ├── cookie.py           # JWT token signing and verification.
│   │       ├── gemini.py           # Configuration for the Gemini model used by AlmaBot.
│   │       ├── logging.py          # Logging utility.
│   │       ├── momo                # MoMo payment gateway integration.
│   │       │   └── momo.py         # MoMo API interaction logic.
│   │       └── timing.py           # Time-related utility functions.
│   ├── requirements.txt            # Python dependencies for the backend.
│   └── run.py                      # Entry point to start the backend Flask server.
├── build.sh                        # Script to build and run the Docker containers.
├── docker-compose.yml              # Docker Compose configuration for multi-container setup (backend, db, nginx).
├── nginx                           # Nginx reverse proxy and frontend hosting.
│   ├── Dockerfile                  # Docker configuration for Nginx (specifics not provided, assumed to serve frontend).
│   └── frontend                    # Frontend application (Vue.js)
│       ├── index.html              # Main HTML file for the frontend.
│       ├── jsconfig.json           # JavaScript configuration (e.g., path aliases).
│       ├── package-lock.json       # Exact versions of frontend dependencies.
│       ├── package.json            # Frontend dependencies (Vue, Vue Router, TailwindCSS, Vite) and scripts.
│       ├── src                     # Frontend source code.
│       │   ├── App.vue             # Root Vue component (content not provided).
│       │   ├── assets              # Static assets (CSS).
│       │   │   ├── base.css        # Base CSS styles.
│       │   │   └── main.css        # Main CSS styles.
│       │   ├── components          # Vue components (AuthPage, NavBar, Footer, etc. - specifics from router.js).
│       │   ├── main.js             # Entry point for the Vue application, initializes Vue, router, Google Login.
│       │   ├── router              # Vue Router configuration.
│       │   │   └── router.js       # Defines application routes and corresponding components.
│       │   ├── services            # Frontend services.
│       │   │   └── notificationService.js     # Service for handling UI notifications.
│       │   └── store               # Vuex store (or similar state management).
│       │       └── auth.js         # Authentication state management (e.g., checking if user is authenticated).
│       └── vite.config.js          # Vite configuration for frontend development server and build.
└── up.sh                           # Script to run the Docker containers (without rebuilding).
```

## What The Project Does

This project is a web platform for users to buy and sell virtual items, primarily focused on CS:GO skins. Key features include:

* **User Authentication**: Secure registration and login, including Google OAuth2.
* **Virtual Item Marketplace**: Browse, buy, and sell items.
* **User Profiles**: Manage personal information, view inventory, and transaction history.
* **Wallet System**: Users have wallets to manage their funds for transactions. Supports deposits via MoMo payment gateway.
* **Inventory Management**: Users can view their items and list them for sale.
* **Transaction History**: Tracks user's financial activities and item trades.
* **AI Chatbot (AlmaBot)**: Provides assistance to users for shop-related queries.
* **Notifications**: Informs users about important events.

The backend is built with Flask (Python), and the frontend is a Vue.js application. Nginx serves as a reverse proxy and hosts the frontend. PostgreSQL is used as the database. The entire application is containerized using Docker.

## Role of Each File

*(Refer to the Project Structure section above for detailed file roles. Key configuration and entry point files are highlighted below)*

* **`docker-compose.yml`**: Defines and configures the services for the application (backend, database, nginx). It manages networking, volumes, and environment variables for these services.
* **`build.sh`**: A utility script that uses Docker Compose to build and start all defined services. This is the primary script for deploying the application.
* **`up.sh`**: A utility script that uses Docker Compose to start already built services. Useful for quickly bringing the application online without a full rebuild.
* **`backend/run.py`**: The main entry point for the Flask backend application.
* **`backend/app/__init__.py`**: Initializes the Flask application, loads configurations, sets up extensions (CORS, Limiter), and registers API blueprints.
* **`backend/app/global_config.py`**: Contains all critical configurations for the backend, including database credentials, JWT secrets, OAuth2 client details, API keys for external services (like AskYourDatabase for the chatbot and MoMo), and site URL settings.
* **`backend/app/models/Database.py`**: Handles the setup of the SQLAlchemy database engine and provides a way to get database sessions.
* **`backend/app/models/__init__.py`**: Initializes all SQLAlchemy models and creates the database tables based on these models. It also executes an initial SQL script (`init.sql`) to populate the database.
* **`backend/requirements.txt`**: Lists all Python dependencies required for the backend to function.
* **`nginx/frontend/package.json`**: Lists JavaScript dependencies and scripts (like `dev`, `build`, `preview`) for the Vue.js frontend.
* **`nginx/frontend/vite.config.js`**: Configuration file for Vite, the build tool and development server used for the frontend. It includes settings for plugins (Vue, TailwindCSS), path aliases, and the development server.
* **`nginx/frontend/src/main.js`**: The entry point for the Vue.js frontend application. It initializes the Vue app, sets up the router, and integrates plugins like `vue3-google-login`.
* **`nginx/frontend/src/router/router.js`**: Defines all the client-side routes for the frontend application, mapping URLs to specific Vue components.

## How to Build and Run the Project

### Prerequisites

* Docker and Docker Compose installed.
* Ensure necessary ports (e.g., 80 for Nginx, 5432 for PostgreSQL) are available on the host machine.

### Build and Run

1.  **Clone the repository.**
2.  **Navigate to the project root directory (`NT208`).**
3.  **Frontend Development Note**:
    Given the current structure where frontend files are under `nginx/frontend/`, if you are developing the frontend and intend to see live changes, you would typically run the Vite development server.
    * Navigate to `nginx/frontend/`.
    * Install dependencies: `npm install`
    * Start the dev server: `npm run dev`
    * The `vite.config.js` specifies `allowedHosts` which might need adjustment based on your setup if accessing from other devices.

4.  **Build and start all services using Docker Compose:**
    ```bash
    ./build.sh
    ```
    This command executes `docker compose up --build`, which will:
    * Build the Docker images for the `backend` and `nginx` services as defined in their respective `Dockerfiles`.
    * Pull the `postgres:13` image for the `db` service.
    * Create and start containers for all services.
    * The backend will connect to the PostgreSQL database.
    * Nginx will act as a reverse proxy and serve the frontend application.

5.  **Accessing the Application:**
    Once the containers are up and running, the application should be accessible via `http://localhost` (or the configured domain/IP).

### Running without Rebuilding

If the images are already built and you just want to start the containers:

```bash
./up.sh
```

This command executes docker compose up

## Stopping the Application

To stop the running containers:
```bash
docker compose down
```

## Test account for Momo
Card number:          9704 0000 0000 0018

Name:                 NGUYEN VAN A

Expiration date:      09/99

Phone:                0999999999

