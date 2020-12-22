SELECT * FROM Products
WHERE UnitPrice > (SELECT avg(UnitPrice) FROM Products);

SELECT *,UnitPrice * UnitsInStock AS 'Value in Stock' FROM Products
WHERE  UnitPrice * UnitsInStock > 3000;

SELECT CategoryName, count(DISTINCT ProductId) FROM Categories
LEFT OUTER JOIN Products
ON Categories.CategoryID = Products.CategoryId;