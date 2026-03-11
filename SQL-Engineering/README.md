# SQL Engineering: Relational Integrity & Schema Design

This directory contains technical implementations of advanced relational database patterns. The primary focus of these scripts is to ensure **Data Integrity**—the essential prerequisite for any reliable AI or Machine Learning model.

## 🏗️ Case Study: Implementing Composite Primary Keys
**Project:** Northwind Database Optimization (Order Details)

### 1. The Challenge: Many-to-Many Conflict
In the standard `Order Details` table, neither the `OrderID` nor the `ProductID` can serve as a Primary Key on its own:
* An **OrderID** repeats because one order can contain many products.
* A **ProductID** repeats because one product can be part of many orders.

Without a unique identifier, the database risks "Row Explosion" and data redundancy, which would compromise any downstream statistical analysis or AI training.

### 2. The Solution: Composite Key Logic
I architected a **Composite Primary Key** by combining `OrderID` and `ProductID`. 

**Implementation Strategy:**
```sql
-- Pattern: Adding a Composite Key to an existing junction table
ALTER TABLE [Order Details]
ADD CONSTRAINT PK_Order_Details PRIMARY KEY (OrderID, ProductID);
