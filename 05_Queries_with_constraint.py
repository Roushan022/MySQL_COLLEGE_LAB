CREATE TABLE Supplier (
    SID INT PRIMARY KEY,
    Sname VARCHAR(50) NOT NULL,
    Branch VARCHAR(10),
    CITY VARCHAR(10),
    PHONE VARCHAR(15)
);
-- DESC Supplier

-- unique constraint
CREATE TABLE Part(
PID INT PRIMARY KEY,
Pnmae VARCHAR(50) NOT NULL,
Color VARCHAR(20),
Price DECIMAL(10,2)
);
-- DESC Part;

-- foreign KEY 
CREATE TABLE Supplies(
SID INT NOT NULL,
PID INT NOT NULL,
QTY INT NOT NULL,
date_supp DATE NOT NULL,
PRIMARY KEY (SID, PID, date_supp),
FOREIGN KEY (SID) references Supplier(SID),
FOREIGN KEY (PID) references Part(PID)
);

-- DESC Supplies;

CREATE TABLE Supplier_Check(
    SID INT PRIMARY KEY,
    Sname VARCHAR(50) NOT NULL,
    Branch VARCHAR(10),
    CITY VARCHAR(10),
    PHONE VARCHAR(15),
    --only allowed this thing sto be insert in it 
    CHECK (Branch IN ('NORTH','SOUTH','EAST','WEST')),
    CHECK (PHONE IS NULL OR PHONE REGEXP '^[0-9]{10}$')
    );
DESC Supplier_Check;

-- defualt values
CREATE TABLE Supplier_Default(
 SID INT PRIMARY KEY,
 Sname VARCHAR(50) NOT NULL,
 branch VARCHAR(10) DEFAULT 'NORTH',
 city VARCHAR(30) DEFAULT 'Unknown',
 PHONE VARCHAR(10) DEFAULT '000000000'
 );
 DESC Supplier_Default;
