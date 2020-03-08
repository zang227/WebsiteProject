/* Creating Tables */

CREATE TABLE Company (
	Company_ID INT NOT NULL,
	Company_Name TEXT,
	Company_Address TEXT,
	Company_Description TEXT,
	Employee_ID INT,
	Job_ID INT,
	PRIMARY KEY (Company_ID),
	FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID),
	FOREIGN KEY (Job_ID) REFERENCES Job(Job_ID)
);

CREATE TABLE Association (
	Association_ID INT NOT NULL,
	Association_Name TEXT,
	Association_Address TEXT,
	Association_Description TEXT,
	Company_ID INT,
	PRIMARY KEY (Association_ID),
	FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID)
);

CREATE TABLE Employee (
	Employee_ID INT NOT NULL,
	Employee_Name TEXT,
	Employee_Last_Name TEXT,
	Employee_Email TEXT,
	Employee_Address TEXT,
	Employee_Resume TEXT,
	Company_ID INT,
	PRIMARY KEY (Employee_ID),
	FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID)
);

CREATE TABLE Job (
	Job_ID INT NOT NULL,
	Job_Description TEXT,
	Job_Date TEXT,
	Job_Status TEXT,
	Company_ID INT,
	Applicant_ID INT,
	Search_Committee_ID INT,
	PRIMARY KEY (Job_ID),
	FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID),
	FOREIGN KEY (Applicant_ID) REFERENCES Applicant(Applicant_ID),
	FOREIGN Key (Search_Committee_ID) REFERENCES Search_Committee(Search_Committee_ID)
);

CREATE TABLE Applicant (
	Applicant_ID INT NOT NULL,
	Applicant_Name TEXT,
	Applicant_Last_Name TEXT,
	Applicant_Resume TEXT,
	Status_Of_Application INT,
	PRIMARY KEY (Applicant_ID)
);

CREATE TABLE Search_Committee (
	Search_Committee_ID INT NOT NULL,
	Employee_ID INT,
	Job_ID INT,
	PRIMARY KEY (Search_Committee_ID),
	FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID),
	FOREIGN KEY (Job_ID) REFERENCES Job(Job_ID)
);

/* Inserting Test Values Into Tables */

INSERT INTO Company (Company_ID, Company_Name, Company_Address, Company_Description, Employee_ID, Job_ID)
VALUES ('1', 'Company Name 1', 'Company Address 1', 'Company Description 1', '1', '1');

INSERT INTO Association (Association_ID, Association_Name, Association_Address, Association_Description, Company_ID)
VALUES ('1', 'Association Name 1', 'Association Address 1', 'Association Description 1', '1');

INSERT INTO Employee (Employee_ID, Employee_Name, Employee_Last_Name, Employee_Email, Employee_Address, Employee_Resume, Company_ID)
VALUES ('1', 'Timothy', 'Steudlein', 'Tsteud1@lsu.edu', 'Employee Address 1', 'Employee Resume 1', '1');

INSERT INTO Job (Job_ID, Job_Description, Job_Date, Job_Status, Company_ID, Applicant_ID, Search_Committee_ID)
VALUES ('1', 'Job Description 1', '3/8/2020', 'Job Status 1', '1', '1', '1');

INSERT INTO Applicant (Applicant_ID, Applicant_Name, Applicant_Last_Name, Applicant_Resume, Status_Of_Application)
VALUES ('1', 'Timothy', 'Steudlein', 'Applicant Resume 1', '0');

INSERT INTO Search_Committee (Search_Committee_ID, Employee_ID, Job_ID)
VALUES ('1', '1', '1');



