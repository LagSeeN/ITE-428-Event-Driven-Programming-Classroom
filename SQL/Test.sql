SELECT  *,UnitPrice-(SELECT avg(UnitPrice) FROM Products) AS 'More AVG' FROM Products WHERE UnitPrice > (SELECT avg(UnitPrice) FROM Products) GROUP By ProductId ORDER BY UnitPrice DESC;

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

SELECT OrdersDetails.OrderId,Orders.OrderDate,Orders.ShipName,Products.ProductName,OrdersDetails.UnitPrice*OrdersDetails.Quantity,Shippers.CompanyName FROM OrdersDetails
INNER JOIN Orders,Shippers,Products
ON OrdersDetails.OrderID = Orders.OrderId AND OrdersDetails.ProductId = Products.ProductID
WHERE OrdersDetails.OrderId = 10309;


-- sql 9

DROP VIEW IF EXISTS report_order;

CREATE VIEW IF NOT EXISTS report_order AS SELECT OrdersDetails.OrderId,Orders.OrderDate,Orders.ShipName,Products.ProductName,OrdersDetails.UnitPrice*OrdersDetails.Quantity AS "Price",Shippers.CompanyName FROM OrdersDetails
INNER JOIN Orders,Shippers,Products
ON OrdersDetails.OrderID = Orders.OrderId AND OrdersDetails.ProductId = Products.ProductID AND Orders.ShipVia = Shippers.ShipperID;

SELECT * FROM report_order
WHERE OrderId = 10309;

SELECT o.OrderDate, p.ProductName, od.UnitPrice * od.Quantity as 'Price', s.CompanyName, o.ShipName
FROM Orders o, OrdersDetails od, Shippers s, Products p
WHERE o.OrderId = 10309 AND o.OrderId = od.OrderId AND o.ShipVia = s.ShipperID AND od.ProductId = p.ProductId;
-------

SELECT Orders.ShipCountry, Count(Orders.OrderId) AS 'No. Order',sum(OrdersDetails.UnitPrice*OrdersDetails.Quantity) AS 'Net Price', sum(OrdersDetails.UnitPrice*OrdersDetails.Quantity)/Count(Orders.OrderId) AS 'Price/Order' FROM OrdersDetails
INNER JOIN Orders,Customers
ON OrdersDetails.OrderID = Orders.OrderId AND Orders.CustomerId = Customers.CustomerId
GROUP BY 1
ORDER BY 4 DESC;

SELECT Products.ProductId,Products.ProductName,count(OrdersDetails.OrderID) AS "Count" FROM Products
INNER JOIN OrdersDetails
ON OrdersDetails.ProductId = Products.ProductID
GROUP BY Products.ProductName
HAVING "Count" > 50;

INSERT INTO "main"."Customers" ("CustomerID", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax") VALUES ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders', 'Sales Representative', 'Obere Str. 57', 'Berlin', 'Western Europe', '12209', 'Germany', '030-0074321', '030-0076545');

SELECT EXISTS(SELECT * FROM Products WHERE ProductId = 2);

SELECT * FROM Products  WHERE ProductId = 2;

UPDATE Products
SET Discontinued = 1
WHERE ProductId = 1;