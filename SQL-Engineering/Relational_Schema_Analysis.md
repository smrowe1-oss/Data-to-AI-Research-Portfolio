# Relational Database Architecture: Multi-Table Synthesis

This document outlines the structural logic required to join multiple relational tables while maintaining data integrity. In **Allied AI Research**, understanding these relationships is critical for preventing "Data Leakage" and ensuring accurate model training.

## 🏗️ Schema Overview: The Northwind Model
The following analysis focuses on the relationship between **Orders**, **Products**, and **Categories**. These represent the standard "Many-to-Many" and "One-to-Many" patterns found in clinical and commercial databases.

### 1. The Junction Table Logic
To connect `Orders` to `Products`, we utilize the `Order Details` table. 
* **Challenge:** One order can have many products; one product can be in many orders.
* **Solution:** The `Order Details` table acts as a bridge, where the **Composite Key** (`OrderID` + `ProductID`) ensures every line item is unique.



### 2. Multi-Table JOIN Implementation
To generate a comprehensive research dataset, we must "flatten" the relational structure using SQL Joins:

```sql
SELECT 
    o.OrderID,
    o.OrderDate,
    p.ProductName,
    c.CategoryName,
    (od.UnitPrice * od.Quantity) AS LineItemTotal
FROM Orders o
JOIN [Order Details] od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
JOIN Categories c ON p.CategoryID = c.CategoryID;
