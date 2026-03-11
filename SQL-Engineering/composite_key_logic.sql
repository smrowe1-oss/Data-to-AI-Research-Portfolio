-- Implementation of Composite Primary Key for Data Integrity
-- Goal: Ensure unique records in a many-to-many junction table

ALTER TABLE [Order Details]
ADD CONSTRAINT PK_Order_Details PRIMARY KEY (OrderID, ProductID);

-- Verification Query
SELECT OrderID, ProductID, COUNT(*)
FROM [Order Details]
GROUP BY OrderID, ProductID
HAVING COUNT(*) > 1;
