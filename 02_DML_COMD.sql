CREATE TABLE Supplier(
  SID INT PRIMARY KEY,
  Sname VARCHAR(20),
  Branch VARCHAR(20),
  City VARCHAR(20),      
  Phone INTEGER NOT NULL 
  );
DESC Supplier;
INSERT INTO Supplier VALUE
(01,"ROUSHAN AKHTAR","BCA","JHK",89695),
(02,"VANDANA","MBA","BLR",90069),
(03,"MEENRA","BBA","BHR",789654),
(04,"NIKHIL","BHM","MCA",894567);

SELECT * FROM Supplier;
SELECT Sname,Phone FROM Supplier;
SELECT Sname, City FROM Supplier WHERE Branch="BCA";
SELECT Sname,City FROM Supplier WHERE Sname LIKE "%r%";

DELETE FROM Supplier WHERE SID=03;

UPDATE Supplier SET City="BCA";
SELECT * FROM Supplier;
