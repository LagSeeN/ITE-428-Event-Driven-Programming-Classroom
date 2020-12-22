SELECT * FROM Products
WHERE UnitPrice > (SELECT avg(UnitPrice) FROM Products);