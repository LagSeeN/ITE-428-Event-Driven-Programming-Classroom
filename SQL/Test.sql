SELECT * FROM Products
WHERE UnitPrice > (SELECT avg(UnitPrice) FROM Products);

SELECT *,UnitPrice * UnitsInStock AS 'Value in Stock' FROM Products
WHERE  UnitPrice * UnitsInStock > 3000;


SELECT CategoryName, count(ProductId) As 'Count Product', sum(UnitPrice * UnitsInStock) As 'Sum  of Value' FROM Categories
LEFT OUTER JOIN Products
ON Categories.CategoryID = Products.CategoryId
GROUP By CategoryName
HAVING sum(UnitPrice * UnitsInStock) >  5000
ORDER By sum(UnitPrice * UnitsInStock);

SELECT Employees.FirstName||' '||Employees.LastName||' , '||Employees.TitleOfCourtesy As 'Name',count(OrderId) As 'Order' FROM Employees
LEFT OUTER JOIN Orders
ON Employees.EmployeeID = Orders.EmployeeId
GROUP By 1
ORDER By count(OrderId);

SELECT ProductName,UnitPrice,count(ProductId) FROM Products
WHERE UnitPrice >= 5 AND UnitPrice <= 10
ORDER By UnitPrice DESC;

SELECT Suppliers.CompanyName, Categories.CategoryName, count(ProductId), avg(UnitPrice) FROM Suppliers
INNER JOIN Categories,Products
ON Products.SupplierId = Suppliers.SupplierID AND Products.CategoryId = Categories.CategoryID
GROUP BY 1,2;