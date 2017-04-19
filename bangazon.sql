DELETE FROM Employees;
DELETE FROM Departments;
DELETE FROM Computers;
DELETE FROM TrainingPrograms;
DELETE FROM EmployeeTraining;
DELETE FROM Customers;
DELETE FROM Products;
DELETE FROM ProductType;
DELETE FROM PaymentType;
DELETE FROM Orders;


DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments; 
DROP TABLE IF EXISTS Computers;
DROP TABLE IF EXISTS TrainingPrograms; 
DROP TABLE IF EXISTS EmployeeTraining;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS ProductType; 
DROP TABLE IF EXISTS PaymentType;
DROP TABLE IF EXISTS Orders;

CREATE TABLE Employees(
	EmployeeId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FullName TEXT NOT NULL,
	IsSupervisor INTEGER NOT NULL,
	DepartmentId INTEGER NOT NULL,
	ComputerId INTEGER NOT NULL,
	FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId),
	FOREIGN KEY (ComputerId) REFERENCES Computers(ComputerId)
);

CREATE TABLE Departments(
	DepartmentId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL,
	Budget INTEGER NOT NULL
);

CREATE TABLE Computers(
	ComputerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	PurchaseDate INTEGER NOT NULL,
	DecommissionDate INTEGER NOT NULL
);

CREATE TABLE TrainingPrograms(
	ProgramId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL,
	MaxAttendees INTEGER NOT NULL,
	StartDate INTEGER NOT NULL,
	EndDate INTEGER NOT NULL
);

CREATE TABLE EmployeeTraining(
	EmployeeTrainingId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	EmployeeId INTEGER NOT NULL,
	ProgramId INTEGER NOT NULL,
	FOREIGN KEY (EmployeeId) REFERENCES Employees(EmployeeId),
	FOREIGN KEY (ProgramId) REFERENCES TrainingPrograms(ProgramId)
);

CREATE TABLE Customers(
	CustomerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	AccountCreated INTEGER NOT NULL,
	IsInactive INTEGER 
);

CREATE TABLE Products(
	ProductId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ProductTypeId INTEGER NOT NULL,
	Price INTEGER NOT NULL,
	Title TEXT NOT NULL,
	Description TEXT NOT NULL,
	FOREIGN KEY (ProductTypeId) REFERENCES ProductType(ProductTypeId)
);

CREATE TABLE Orders(
	CustomerId INTEGER NOT NULL,
	ProductId INTEGER NOT NULL,
	PaymentTypeId INTEGER NOT NULL,
	FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
	FOREIGN KEY (ProductId) REFERENCES Products(ProductId)
);

CREATE TABLE PaymentType(
	PaymentTypeId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	AccountNumber INTEGER NOT NULL
);

CREATE TABLE ProductType(
	ProductTypeId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL
);

INSERT INTO Employees(FullName, IsSupervisor, DepartmentId, ComputerId) VALUES ('Harper', 1, 1, 1);
INSERT INTO Employees(FullName, IsSupervisor, DepartmentId, ComputerId) VALUES ('Steve', 1, 2, 1);
INSERT INTO Departments(Name, Budget) VALUES ('Human Resources', 400000);
INSERT INTO Departments(Name, Budget) VALUES ('IT', 350000);

--the stuff after the select builds the columns, the from takes one table and matches it with the table in the left join, the things after the ON must match. In other words, the table attribute must be shared between the tables
SELECT Employees.FullName, Departments.Name FROM Departments LEFT JOIN Employees ON Employees.DepartmentId= Departments.DepartmentId;



