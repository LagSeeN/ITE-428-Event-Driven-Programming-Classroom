-- ดนุพล อินทรานุรักษ์ 

--1
SELECT ProductName,UnitPrice,UnitsInStock FROM Products;

--2
SELECT ProductName,UnitPrice AS Price,UnitsInStock FROM Products;

--3
SELECT ProductName,UnitPrice AS Price,UnitsInStock, UnitPrice * UnitsInStock AS ValueInStock FROM Products;

--4
SELECT upper(ProductName),UnitPrice AS Price,UnitsInStock, UnitPrice * UnitsInStock AS ValueInStock FROM Products;

--5
SELECT upper(ProductName),UnitPrice AS Price,UnitsInStock, UnitPrice * UnitsInStock AS ValueInStock FROM Products
ORDER BY ValueInStock DESC;

--6
SELECT upper(ProductName),UnitPrice AS Price,UnitsInStock, UnitPrice * UnitsInStock AS ValueInStock FROM Products
WHERE ValueInStock >= 3000
ORDER BY ValueInStock DESC;

--7
SELECT upper(ProductName),UnitPrice AS Price,UnitsInStock, UnitPrice * UnitsInStock AS ValueInStock FROM Products
WHERE ValueInStock >= 3000 AND Price < 100
ORDER BY ValueInStock DESC;

--8
SELECT upper(ProductName),UnitPrice AS Price,UnitsInStock, UnitPrice * UnitsInStock AS ValueInStock FROM Products
WHERE UnitsInStock IN (0,10,20)
ORDER BY UnitsInStock DESC,ProductName ASC;

--9
SELECT upper(ProductName),UnitPrice AS Price,UnitsInStock, UnitPrice * UnitsInStock AS ValueInStock FROM Products
WHERE UnitsInStock >= 10 AND UnitsInStock <=20
ORDER BY UnitsInStock DESC,ProductName ASC;

--10
SELECT CompanyName,ContactName,Country,City,Fax FROM Suppliers;

--11
SELECT CompanyName,ContactName,Country,City,Fax FROM Suppliers
WHERE Country IN ('USA');

--12
SELECT CompanyName,ContactName,Country,City,Fax FROM Suppliers
WHERE Country IN ('USA') AND Fax IS NULL;

--13
SELECT CompanyName,ContactName,Country,City,Fax FROM Suppliers
WHERE Country LIKE 's%';

--14
SELECT CompanyName,ContactName,Country,City,Fax FROM Suppliers
WHERE Country LIKE '%a';

--15
SELECT CompanyName,ContactName,Country,City,Fax FROM Suppliers
WHERE Country LIKE '%an%';

--16
SELECT CompanyName,ContactName,Country,City,Fax FROM Suppliers
WHERE Country LIKE '__an%';

--17
SELECT CompanyName,Country,City FROM Customers
WHERE Country LIKE '%land';

--18
SELECT TitleOfCourtesy,FirstName,LastName,BirthDate FROM Employees;

--19
SELECT TitleOfCourtesy|| ' ' || FirstName || ' ' || LastName AS Emp, BirthDate FROM Employees;

--20
SELECT TitleOfCourtesy|| ' ' || FirstName || ' ' || LastName AS Emp, BirthDate FROM Employees
ORDER BY BirthDate DESC;

--21
SELECT TitleOfCourtesy|| ' ' || FirstName || ' ' || LastName AS Emp, BirthDate FROM Employees
WHERE BirthDate LIKE ('1995%')
ORDER BY BirthDate;

--22
SELECT TitleOfCourtesy|| ' ' || FirstName || ' ' || LastName AS Emp, BirthDate FROM Employees
WHERE BirthDate LIKE ('____-01%')
ORDER BY BirthDate;

--23
SELECT ProductName,CompanyName AS SupplierCompanyname FROM Products
LEFT OUTER JOIN Suppliers
ON Suppliers.SupplierId = Products.SupplierId;

--24
SELECT ProductName,CompanyName AS SupplierCompanyname,CategoryName FROM Products
LEFT OUTER JOIN Suppliers,Categories
ON Suppliers.SupplierId = Products.SupplierId AND Categories.CategoryID = Products.CategoryId;

--25
SELECT OrderId,OrderDate,Customers.CompanyName AS Customers, Employees.TitleOfCourtesy|| ' ' || Employees.FirstName || ' ' || Employees.LastName AS Employee,Shippers.CompanyName AS Shipper FROM Orders
LEFT OUTER JOIN Customers,Shippers,Employees
ON Orders.CustomerId = Customers.CustomerId AND Orders.ShipVia = Shippers.ShipperID AND Orders.EmployeeId = Employees.EmployeeID;

--26
SELECT count(ProductId) AS NoOfProduct, sum(UnitPrice) AS SumOfUnitprice, max(UnitPrice)AS MaxOfUnitprice,min(UnitPrice)AS MinOfUnitprice,avg(UnitPrice)AS AverageOfUnitprice FROM Products;