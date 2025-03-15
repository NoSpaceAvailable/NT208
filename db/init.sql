CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE productImages (
    id SERIAL PRIMARY KEY,
    productId INTEGER NOT NULL,
    url VARCHAR(255) NOT NULL,
    FOREIGN KEY (productId) REFERENCES products(id)
);

CREATE TABLE Transactions (
    
);

CREATE TABLE Orders (

);

CREATE TABLE Reviews (
    
);

CREATE TABLE Reputaions (
    
);