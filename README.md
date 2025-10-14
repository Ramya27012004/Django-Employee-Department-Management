# 🧑‍💼 Django Employee Department Management

##  Overview
This is a simple Django application to manage **Employee** and **Department** details.  
It demonstrates how to create models, perform database migrations, insert data, and manage relationships between tables.

##  Features
- Created **Employee** and **Department** models using Django ORM  
- Established a **ForeignKey relationship** between Employee and Department  
- Inserted sample data into both tables  
- Displayed Employee and Department details using **Django Admin**  
- Implemented **CRUD operations** (Create, Read, Update, Delete)  
- Added functionality to fetch and filter data for display on web pages  

##  Models

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

##  How Data Display Works (Theory)
1. **Purpose of Views**  
   Views in Django handle application logic, fetch data from the database, and send it to templates for display on web pages.

2. **Displaying Departments**  
   - Fetch all department records from the database.  
   - Pass the data to a template to display a structured list of departments.  
   - **Use:** Allows users to view all departments in the system.

3. **Displaying Employees**  
   - Employee records can be fetched completely or filtered by specific criteria (e.g., by name or names starting with a letter).  
   - Filtered data is passed to a template for dynamic display.  
   - **Use:** Users can view employees dynamically based on different filters.

4. **Key Concepts Demonstrated**  
   - Fetching all records from a model  
   - Filtering records based on conditions  
   - Passing data to templates for rendering  
   - Dynamic display of database data on web pages  

##  Technologies Used
- Python  
- Django  
- SQLite / PostgreSQL (depending on setup)  

##  What I Learned
- How to create Django models and use different field types  
- How to connect models using **ForeignKey** relationships  
- How to apply changes to the database using migrations  
- How to add and manage data using **Django Admin** and ORM  
- How to perform **CRUD operations** on data  
- How data can be fetched, filtered, and displayed dynamically on web pages  
- Understanding Django project structure and interaction between components  
