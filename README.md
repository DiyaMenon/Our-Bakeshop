# 🍰 Bakery Management System

Welcome to the Bakery Management System! This Python application, built with `tkinter` and `mysql.connector`, helps manage product inventory for a bakery.

---

## ✨ Features

* **Add New Products**: Easily insert new bakery products into the database with details like product code, name, category, price, quantity/weight, description, and an image path.
* **Update Products**: Modify existing product information by searching for a product code and updating its details.
* **Delete Products**: Remove products from the database.
* **Display Products**: View product details, with options to display all products or filter by category (Cakes, Cupcakes, Cookies, Brownies, Other Desserts).
* **Admin Login**: Secure access to management functionalities via an administrator login.

---

## 🛠️ Technologies Used

* **Python 3**: The core programming language.
* **Tkinter**: For building the graphical user interface.
* **MySQL Connector**: To interact with the MySQL database.
* **Pillow (PIL)**: For image handling within the Tkinter application (though the image loading part seems commented out in the provided snippet, it's generally used for image manipulation).

---

## 🚀 Getting Started

To run this project locally, follow these steps:

### Prerequisites

Make sure you have the following installed:

* Python 3.x
* MySQL Server

You'll also need to install the required Python libraries:

```bash
pip install tkinter
pip install mysql-connector-python
pip install Pillow
```
---

## 🚀 Getting Started

To run this project locally, follow these steps:

### Database Setup

1.  **Connect to MySQL**: Ensure your MySQL server is running.
2.  **Create Database**: The provided commented-out code suggests creating a database named `bakery`. If you haven't already, run the following SQL command in your MySQL client:

    ```sql
    CREATE DATABASE bakery;
    ```
3.  **Create Tables**: The project requires several tables. The commented-out Python functions (`createtableproduct`, `createtableemployee`, `createtableorders`, `createtablecustomer`, `createtableusers`, `imgtable`) are intended for this purpose. You can either uncomment and run these functions once, or manually create the tables in your `bakery` database. Here are the SQL schemas based on your code:

    ```sql
    -- product table
    CREATE TABLE product (
        pcode INT PRIMARY KEY,
        pname VARCHAR(30) NOT NULL,
        category VARCHAR(30),
        price FLOAT,
        qty_weight FLOAT,
        descp VARCHAR(250),
        imgpath VARCHAR(250) -- Added based on your insertrec function
    );

    -- employee table (if used in other parts of the project)
    CREATE TABLE employee (
        empno INT PRIMARY KEY,
        ename CHAR(20) NOT NULL,
        sal FLOAT,
        job CHAR(20),
        doj DATE
    );

    -- orders table (if used in other parts of the project)
    CREATE TABLE orders (
        orderno INT PRIMARY KEY,
        details VARCHAR(50) NOT NULL,
        billamt FLOAT,
        delvdate DATE,
        cid INT
    );

    -- customer table (if used in other parts of the project)
    CREATE TABLE customer (
        cid INT PRIMARY KEY,
        cnam VARCHAR(30),
        cphno VARCHAR(10),
        cadrs VARCHAR(50),
        bookeditems VARCHAR(40)
    );

    -- users table (potential for login/registration - your schema was commented out but might be for 'customer' or a separate 'users' table)
    -- Based on your createtableusers:
    CREATE TABLE users (
        fname VARCHAR(45),
        lname VARCHAR(45),
        contact VARCHAR(45),
        email VARCHAR(45) PRIMARY KEY,
        securityQ VARCHAR(45),
        securityA VARCHAR(45),
        password VARCHAR(45)
    );

    -- img table (your create table query for img was commented out and incorrect based on usage, so I've removed it for now.
    -- If you intend to store images in the DB, you'll need to re-evaluate its schema and usage with 'BLOB' type,
    -- or if you're just storing paths, then 'imgpath' in the product table is sufficient.)
    ```
    **Note**: Ensure your MySQL user (`root` in your code) has the necessary permissions and the password (`icecream123`) is correctly set.

### Running the Application

1.  **Save the code**: Save your Python code (e.g., `bakery_app.py`).
2.  **Run the script**: Open a terminal or command prompt, navigate to the directory where you saved the file, and run:
    ```bash
    python bakery_app.py
    ```
3.  **Admin Login**: Use the following credentials to access the admin panel:
    * **Username**: `admindiya` or `admins`
    * **Password**: `ourbakeshop27`

---

## 📂 Project Structure

* `bakery_app.py`: Contains the main application logic, GUI, and database interactions.
* `*.png`: Image files used for the GUI background and buttons (e.g., `newproductbg.png`, `updateimg.png`, `deleteprdt.png`, `displaymenu.png`, `adminpagefunc.png`, `adlog.png`). Make sure these images are in the same directory as your Python script.

---

## 🤝 Contributing

Feel free to fork the repository and contribute to this project. Any improvements or new features are welcome!

---
