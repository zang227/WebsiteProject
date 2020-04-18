from polls.models import Company, Association, Employee, Job, Applicant
from datetime import date


def insert_test_data():

    current = date.today()

    # then go into admin portal and manually set Foreign relationships!

    a1 = Applicant(applicant_name="Dani",applicant_last_name="Rodriguez",applicant_email="dani@hotmail.com",applicant_password="silly123",applicant_address="1654 Brightside Dr Baton Rouge LA 70820",applicant_resume="Education: Bachelor’s in Computer Science, Master’s Degree in Computer Science- Minor in Software Engineering, Ph.D in Computer Science. Skills: Object-Oriented JavaScript, CSS,  HTML5, Web-based languages, React.JS",application_status="Available",applicant_job=None)
    a2 = Applicant(applicant_name="Jose",applicant_last_name="Rodriguez",applicant_email="JD@yahoo.com",applicant_password="silly123",applicant_address="4532 Nicholson Dr Baton Rouge LA 70803",applicant_resume="Education: Bachelor’s in Computer Engineering, Master’s Degree in Computer Science- Minor in Software Engineering. Skills: BigData technology, Hadoop, and Spark, Java, C++, REST and RPC.",application_status="Available",applicant_job=None)
    a3 = Applicant(applicant_name="Sim",applicant_last_name="Thapa",applicant_email="ST@gmail.com",applicant_password="silly123",applicant_address="6734 Corporate Baton Rouge LA 70801",applicant_resume="Education: Bachelor’s in Computer Science. Skills: C#, XAML, Linq, SQL, ASP.NET, Xamarin, GIS, Mobile development.",application_status="Available",applicant_job=None)
    a4 = Applicant(applicant_name="Santi",applicant_last_name="Salas",applicant_email="st@hotmail.com",applicant_password="silly123",applicant_address="5432 Nicholson Dr Covington LA 6756",applicant_resume="Education: Bachelor’s in Computer Science and minor in Software Engineering. Skills: Typescript, ReactJS, GraphGL, python, Java.",application_status="Available",applicant_job=None)
    a5 = Applicant(applicant_name="Denisse",applicant_last_name="Saenz",applicant_email="DS@yahoo.com",applicant_password="silly123",applicant_address="1423 Burbank Dr Gonzalez LA 5674",applicant_resume="Education: Bachelor’s degree in Mechanical Engineering, Master’s degree in Mechanical Engineering. Skills: Process simulation software (Aspen Suite) and hydraulic modeling software (AFTFathom).",application_status="Available",applicant_job=None)
    b = Association(association_name="ROCA.sa",association_address="7556 Nicholson Dr, Baton Rouge LA 70803",association_description="ROCA.sa is an engineering association company.")
    c = Company(company_name="PDVSA",company_address="0001 PDVSA 7834 Brightside Rd, LA 9890",company_description="PDVSA is a US$14.3 billion technology, engineering, construction and manufacturing and financial services conglomerate. It addresses critical needs in key sectors including infrastructure, construction, hydrocarbon, power, defense and aerospace. A strong, customer-focused approach, conformance to global HSE standards and the constant quest for top-class quality have enabled the Company to sustain leadership in its major lines of business for over 75 years. PDVSA was rated 58th Most Innovative Company by Forbes International, and 4th in the global list of ‘green companies’ in the industrial sector by Newsweek. A survey by a leading HR consultancy affirmed its reputation as a people-focused company, leading to the award for the ‘Most Attractive Employer’ in the industrial sector.",company_association=None)
    d1 = Employee(employee_name="Dani",employee_last_name=" Rodriguez",employee_email="dani@hotmail.com",is_employer="False",employee_company=None)
    d2 = Employee(employee_name="Jose",employee_last_name="Rodriguez",employee_email="JD@yahoo.com",is_employer="False",employee_company=None)
    d3 = Employee(employee_name="Sim",employee_last_name="Thapa",employee_email="ST@gmail.com",is_employer="False",employee_company=None)
    d4 = Employee(employee_name="Santi",employee_last_name="Salas",employee_email="st@hotmail.com",is_employer="False",employee_company=None)
    d5 = Employee(employee_name="Denisse",employee_last_name="Saenz",employee_email="DS@yahoo.com",is_employer="False",employee_company=None)
    e1 = Job(job_title="Software Engineer",job_qualifications="Master's Degree in Computer Science or related field. Expert knowledge of one of the following programming languages: Java, C and C++. 5+ years of hands on experience in software development, including design, implementation, debugging, and support, building scalable system software and/or Services. Experience working with REST and RPC service patterns and other client/server interaction models.",job_date=current,job_status="Open",job_company=None)
    e2 = Job(job_title="Senior Developer",job_qualifications="Master’s or Ph.D in Computer Science. Development, Maintenance, and Troubleshooting in Google Ad Manager (formerly DFP). Development and Maintenance of Tools for enhanced trafficking, automation, and Creative previews. Develop, Debug next level Ad Products that serve on our any of our platforms, on- and off property. Collaborate with and execute major cross-platform executions as a team, or independently when needed. ",job_date=current,job_status="Open",job_company=None)
    e3 = Job(job_title="Software developer",job_qualifications="Bachelor in Computer Science. 2-8 years of experience. Good knowledge of C#, XAML, Linq, SQL. Knowledge of ASP.NET, Xamarin, GIS, Mobile development will be a bonus.",job_date=current,job_status="Open",job_company=None)
    e4 = Job(job_title="Full Stack Software Engineer",job_qualifications="Bachelor in Computer Science or Software Engineer related. Strong knowledge using Typescript. Strong experience in ReactJS. Some knowledge of graphQL. Some experience with Agile processes and methods.",job_date=current,job_status="Open",job_company=None)

    a1.save()
    a2.save()
    a3.save()
    a4.save()
    a5.save()
    b.save()
    c.save()
    d1.save()
    d2.save()
    d3.save()
    d4.save()
    d5.save()
    e1.save()
    e2.save()
    e3.save()
    e4.save()

    a1 = Applicant(applicant_name="Daniel",applicant_last_name="Rodriguez",applicant_email="daniel@hotmail.com",applicant_password="silly123",applicant_address="1654 Brightside Dr Baton Rouge LA 70820",applicant_resume="Education: Bachelor’s in civil engineering. Skills: ASCE 7, AISC Steel Construction Manual, AISC 360, ACI 318, IBC, NFPA Life Safety Code, OSHA laws & regulations.",application_status="Available",applicant_job=None)
    a2 = Applicant(applicant_name="Sebastian",applicant_last_name="Rodriguez",applicant_email="SRodriguez@yahoo.com",applicant_password="silly123",applicant_address="4532 Nicholson Dr Baton Rouge La 70803",applicant_resume="Education: Bachelor’s Computer Engineering minor in Software Engineering. Skills: Agile/SCRUM, scaled agile or similar methodologies, Strong leadership, project management, time management, and problem-solving skills, OOP, systems architecture, Java and related frameworks, modern JScript frameworks, microservices, relational and noSQL databases, CI/CD.",application_status="Available",applicant_job=None)
    a3 = Applicant(applicant_name="Samuel",applicant_last_name="Stephano",applicant_email="SS@gmail.com",applicant_password="silly123",applicant_address="6734 Corporate Baton Rouge LA 70801",applicant_resume="Education: Bachelor’s degree in Mechanical Engineering. Skills: Process simulation software (Aspen Suite) and hydraulic modeling software (AFTFathom).",application_status="Available",applicant_job=None)
    a4 = Applicant(applicant_name="Santiago",applicant_last_name="Ortiz",applicant_email="stortiz@hotmail.com",applicant_password="silly123",applicant_address="5432 Nicholson Dr Covington LA 67569",applicant_resume="Education: Bachelor’s degree in Chemical Engineering. Skills : Project management.",application_status="Available",applicant_job=None)
    a5 = Applicant(applicant_name="Julia",applicant_last_name="Mata",applicant_email="kt@yahoo.com",applicant_password="silly123",applicant_address="1423 Burbank Dr Gonzalez LA 5674",applicant_resume="Education: Bachelor’s in Computer Engineering. Skills: BigData technology, Hadoop, and Spark, C++, Java.",application_status="Available",applicant_job=None)
    c = Company(company_name="Petrobras",company_address="•	0002 Petrobras 2123 Highland Rd, LA 1237",company_description="Petrobras have been in operation since 2011, covering all aspects of work in the area of Mechanical installations including Plumbing services, Air conditioning, Ventilation and BMS systems. During this time Petrobras services have become specialists in planned preventative maintenance as well as installations. Our success is based on the continuous commitment that Alpha Mechanical services give to all our clients by continuously updating and developing our services, and importantly, in this time of rising costs – competitive pricing structure. Our consistency of work quality, experienced mechanical & electrical engineers, fast reliable 24 hour call out service, and preventative maintenance have also contributed towards the success to date of our company. We are committed to Health & Safety and all engineers are completely trained in this area. We also use an external company to monitor and audit our Health and safety practices.",company_association=None)
    d1 = Employee(employee_name="Daniel",employee_last_name="Rodriguez",employee_email="daniel@hotmail.com",is_employer="False",employee_company=None)
    d2 = Employee(employee_name="Sebastian",employee_last_name="Rodriguez",employee_email="SRodriguez@yahoo.com",is_employer="False",employee_company=None)
    d3 = Employee(employee_name="Samuel",employee_last_name="Stephano",employee_email="SS@gmail.com",is_employer="False",employee_company=None)
    d4 = Employee(employee_name="Santiago",employee_last_name="Ortiz",employee_email="stortiz@hotmail.com",is_employer="False",employee_company=None)
    d5 = Employee(employee_name="Julia",employee_last_name="Mata",employee_email="kt@yahoo.com",is_employer="False",employee_company=None)
    e1 = Job(job_title="Civil engineer",job_qualifications="BS degree in civil engineering. 7+ years of structural engineering experience, preferably in a heavy industrial or similar field. Master’s degree and PhD in civil engineering or related field can each be substituted for 1 year of experience. Working knowledge of structural analysis software, preferably RISA 3D Primary.",job_date=current,job_status="Open",job_company=None)
    e2 = Job(job_title="Director Engineering ",job_qualifications="Bachelor's degree in Computer Science or related field or equivalent work experience. Minimum of 12 years of overall engineering experience including a minimum of 8 years of management and leadership experience.",job_date=current,job_status="Open",job_company=None)
    e3 = Job(job_title="Project Engineer",job_qualifications="Degree in engineering is required. Strong knowledge of process equipment and their functions. Ability to read P&ID’s and instrument loops sheets. Proficiency in Microsoft applications, such as Word and Excel. This position requires an employee to be in an office environment as well as exposed to some outside elements; process and warehouse environment.",job_date=current,job_status="Open",job_company=None)
    e4 = Job(job_title="Process Engineer",job_qualifications="Bachelor's Degree in Chemical, Petroleum, or Mechanical Engineering. Minimum 3 years' applicable experience. Familiarity with the Process simulation software (Aspen Suite) and hydraulic modeling software (AFTFathom), as well as proficiency with basic programs such as Microsoft Excel.",job_date=current,job_status="Open",job_company=None)

    a1.save()
    a2.save()
    a3.save()
    a4.save()
    a5.save()
    c.save()
    d1.save()
    d2.save()
    d3.save()
    d4.save()
    d5.save()
    e1.save()
    e2.save()
    e3.save()
    e4.save()

    a1 = Applicant(applicant_name="Daniel",applicant_last_name="Caraballo",applicant_email="danielCaraba@hotmail.com",applicant_password="silly123",applicant_address="1654 Brightside Dr Baton Rouge LA 70820",applicant_resume="Education: Bachelor’s in civil engineering. Skills: design of structural steel and foundations for supporting equipment & pipe.",application_status="Available",applicant_job=None)
    a2 = Applicant(applicant_name="Dahne",applicant_last_name="D’alessandro",applicant_email="Dalessa@yahoo.com",applicant_password="silly123",applicant_address="4532 Nicholson Dr Baton Rouge La 70803",applicant_resume="Education: Bachelor’s in Mechanical engineering. Skills: Project Management.",application_status="Available",applicant_job=None)
    a3 = Applicant(applicant_name="Nathalie",applicant_last_name="Stephano",applicant_email="NS@gmail.com",applicant_password="silly123",applicant_address="6734 Corporate Baton Rouge LA 70801",applicant_resume="Education:Bachelor’s in Mechanical engineering. Skills: Project Management.",application_status="Available",applicant_job=None)
    c = Company(company_name="Ecopetrol",company_address="•	0003 Ecopetrol  2342 Nicholson Dr, LA 70830",company_description="Ecopetrol shares over half a century of industry-leading excellence with every client we meet. We offer general contracting, construction management, design-build, and preconstruction planning services for projects of all sizes—from a single office fit-up to water supply programs valued at over $300 million. Ecopetrol success over the years is due to its employees’ dedication to excellent work, customer service that exceeds expectations, and a safety program that has led to millions of zero-accident hours. Honesty and open communication have empowered Ecopetrol’s workforce since day one, and it shows in our work.",company_association=None)
    d1 = Employee(employee_name="Daniel",employee_last_name="Caraballo",employee_email="danielCaraba@hotmail.com",is_employer="False",employee_company=None)
    d2 = Employee(employee_name="Dahne",employee_last_name="D’alessandro",employee_email="Dalessa@yahoo.com",is_employer="False",employee_company=None)
    d3 = Employee(employee_name="Nathalie",employee_last_name="Stephano",employee_email="NS@gmail.com",is_employer="False",employee_company=None)
    e1 = Job(job_title="CIVIL ENGINEER",job_qualifications="BS in Civil Engineering. 3-5 years experience in design of structural steel and foundations for supporting equipment & pipe, 1+ years project management experience, ability to coordinate with consulting engineering and construction contractors.",job_date=current,job_status="Open",job_company=None)
    e2 = Job(job_title="Mechanical engineering intern",job_qualifications="BS in Mechanical Engineering. 3-5 years of experience. Position Summary Reporting directly to an assigned lead Engineer or Project Manager in an office or on a project construction work site, this is a temporary position providing on the job training. Duties provide meaningful work experience and business knowledge to college students in their chosen field.",job_date=current,job_status="Open",job_company=None)

    a1.save()
    a2.save()
    a3.save()
    c.save()
    d1.save()
    d2.save()
    d3.save()
    e1.save()
    e2.save()


def createJob(title, qual, jobdate, status, company):

    createjob = Job(job_title=title, job_qualifications=qual, job_date=jobdate, job_status=status, job_company=company)
    createjob.save()


def createAccount(firstName, lastName, email, password, address, resume, status, job, employer,company):
    a1 = Applicant(applicant_name=firstName, applicant_last_name=lastName,
                       applicant_email=email, applicant_password=password,
                       applicant_address=address,
                       applicant_resume=resume,
                       application_status=status, applicant_job=job)
    d3 = Employee(employee_name=firstName, employee_last_name=lastName, employee_email=email,
                      is_employer=employer, employee_company=company)
    a1.save()
    d3.save()
