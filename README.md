# 🧑‍💼 Django Employee Department Management

## 📘 Overview
This is a simple Django application to manage **Employee** and **Department** details.  
It demonstrates how to create models, perform database migrations, insert data, and manage relationships between tables.

## ⚙️ Features
- Created **Employee** and **Department** models using Django ORM  
- Established a **ForeignKey relationship** between Employee and Department  
- Inserted sample data into both tables  
- Displayed Employee and Department details using **Django Admin**  
- Implemented **CRUD operations** (Create, Read, Update, Delete)  

## 🧩 Models

### Department Model
- **deptno** – Department Number (Primary Key)  
- **dname** – Department Name  
- **loc** – Location  

### Employee Model
- **empno** – Employee Number (Primary Key)  
- **ename** – Employee Name  
- **job** – Job Title  
- **mgr** – Manager (Self-referential Foreign Key)  
- **hiredate** – Date of Hiring  
- **sal** – Salary  
- **comm** – Commission  
- **deptno** – Foreign Key (linked to Department)  

## 🛠️ Technologies Used
- Python  
- Django  
- SQLite / PostgreSQL (depending on setup)  

## 💡 What I Learned
- How to create Django models and use different field types  
- How to connect models using **ForeignKey** relationships  
- How to apply changes to the database using migrations  
- How to add and manage data using **Django Admin** and ORM  
- How to perform **CRUD operations** on data  
- Understand the Django project structure and how different components work together
