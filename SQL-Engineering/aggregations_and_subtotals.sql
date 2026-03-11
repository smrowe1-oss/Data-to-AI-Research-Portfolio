```sql
-- Calculating Subtotals using SQL Arithmetic
-- Generates a calculated field for research-ready datasets

SELECT
OrderID,
SUM(UnitPrice * Quantity) AS Subtotal
FROM [Order Details]
GROUP BY OrderID
ORDER BY Subtotal DESC;
