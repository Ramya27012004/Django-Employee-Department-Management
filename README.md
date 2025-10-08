🧑‍💼 Django Employee Department Management
📘 Overview

This project is a simple Django application designed to manage Employee and Department details.
It demonstrates how to create models, perform database migrations, and insert data into related tables.

⚙️ Features

Created Employee and Department models using Django ORM.

Established a ForeignKey relationship between Employee and Department.

Inserted sample data into both tables.

Displayed Employee and Department details through Django admin.

Demonstrated CRUD operations (Create, Read, Update, Delete) in Django.

🧩 Models Used
Department Model

deptno – Department Number (Primary Key)

dname – Department Name

loc – Location

Employee Model

empno – Employee Number (Primary Key)

ename – Employee Name

job – Job Title

mgr – Manager (Self-referential Foreign Key)

hiredate – Date of Hiring

sal – Salary

comm – Commission

deptno – Foreign Key (linked to Department)

🛠️ Technologies Used

Python

Django

SQLite / PostgreSQL (depending on setup)

💡 What I Learned

During this project, I learned how to:

Create Django models and use different types of fields.

Connect models using ForeignKey relationships.

Apply changes to the database using migrations.

Add and manage data using Django Admin and ORM.

Perform CRUD operations (Create, Read, Update, Delete) on data.

Understand the Django project structure and how different parts work together.

Improve my skills in back-end development with Python and Django.
