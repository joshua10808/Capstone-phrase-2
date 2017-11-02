import json
from pprint import pprint

# path = 'C:\\Users\\Joshua\\Documents\\QUT Work\\Semester 4 LAST ONE\\IFB399 Capstone Project (Phase 2)\\py Test grouping\\url.json'
path = '..\\Scrapy_Code\\seekinfo.json'

with open(path,'r') as data_file: 
	data = json.load(data_file) # load in line?
	leng = len(data)
	i = 0

	trying = "Test Analyst" # not in the list SUCESSSSSSSS

	# NEED TO CHANGE THE SEQUENCE
	#Analysis
	anaA = "Business Intelligence"
	anaB = "Business Analyst"
	anaC = "Technical Analyst"
	anaD = "Systems Analyst"
	anaE = "Support Analyst"
	anaF = "Application Analyst"

	#CIO/Management
	cioA = "Chief Information Officer"
	cioB = "Business Development Manager"
	cioC = "Technology Lead"
	cioD = "Policy Officer"
	cioE = "Chief Technology Officer"

	#Database
	dataA = "Database Administrator"
	dataB = "Data Warehouse"
	dataC = "Database Developer"
	dataD = "SQL"
	dataE = "Data Management"
	dataF = "Database Engineer"

	#Design 
	desA = "Designer"
	desB = "User Experience Designer"
	desC = "Design Engineer"
	desD = "Graphic Designer"

	#Game 
	gameA = "Game"
	gameB = "Games Developer"
	gameC = "Games Designer"
	gameD = "Games Illustrator"
	gameE = "Games Artist"
	gameF = "Artist"

	#Hardware Specalist
	hardA = "Hardware Engineer"
	hardB = "Embedded Systems Engineer"
	hardC = "Electronics Engineer"
	hardD = "Electronics Technician"

	#Work Experience
	workA = "Internship"
	workB = "Work Experience"
	workC = "Student Program";

	#Consulting
	conA = "Consultant";
	conB = "Technical Consultant";
	conC = "Senior Consultant";
	conD = "ERP Consultant";
	conE = "Infrastructure Consultant";
	conF = "SAP Consultant";

	#IT Support
	itsA = "Desktop Support";
	itsB = "Support Technician";
	itsC = "Application Support Specialist";
	itsD = "Help Desk Support";
	itsE = "IT Support";
	itsF = "Service Desk Analyst";

	#Networking
	netA = "Network Designer";
	netB = "Network Engineer";
	netC = "Network Administrator";
	netD = "Field Network Technician";
	netE = "Radio Communications";
	netF = "Telecommunications";
	netG = "Infrastructure Engineer";
	netH = "Network Architect";

	#Programming
	progA = "Java Developer";
	progB = "Embedded Software Engineer";
	progC = "Software Developer";
	progD = "Senior Developer";
	progE = "Full Stack Engineer";
	progF = "Software Engineer";
	progG = "Applications Developer";
	progH = "C# Developer";
	progI = "C++ Developer";
	progJ = "Programmer";

	#Project Management
	pmA = "ICT Project Manager";
	pmB = "Senior ERP Project Manager";
	pmC = "Project Coordinator";
	pmD = "Program Delivery Lead";
	pmE = "Site Supervisor";
	pmF = "Deployment Officer";

	#Sales
	saleA = "Sales Solutions Specialist";
	saleB = "Sales Manager";
	saleC = "Field Sales Representative";
	saleD = "Sales Administrator";
	saleE = "Sales Specialists";

	#Security
	secA = "Information Security Manager";
	secB = "Security Management Officer";
	secC = "Information Security Analyst";
	secD = "Cyber Security Engineer";
	secE = "Security Technical Consultant";
	secF = "Information Security Specialist";
	secG = "Security Advisor";

	#System  Administration
	saA = "Systems Engineer";
	saB = "Systems Administrator";
	saC = "Systems Manager";
	saD = "Platform Manager";
	saE = "SharePoint Administrator";

	#Teachers
	teaA = "Software Development Trainer";
	teaB = "Teacher";
	teaC = "Lecturer";
	teaD = "ICT Trainer";
	teaE = "Telecommunications Trainer";

	#Testers
	testA = "Automation Tester";
	testB = "Test Lead";
	testC = "Test Manager";
	testD = "Test Analyst";
	testE = "Test Engineer";	
	testF = "Performance Tester";
	testG = "Test Co-ordinator";
	testH = "Software Tester";

	#Cloud
	cloudA = "VMware Engineer";
	cloudB = "Cloud Engineer";
	cloudC = "Storage & Virtualisation";
	cloudD = "Cloud Services Administrator";
	cloudE = "Azure Cloud Engineer";

	#Web Development 
	webA = "Web UI Developer";
	webB = "Web Developer";
	webC = "Web App Developer";
	webD = "Web Designer";
	webE = "Front End Web Developer";
	webF = "Fullstack Web Developer";

	# art= "artificial intelligence";
	# itf = "IT fundamentals"; 
	# itc = "IT consulting";   
	# sm = "social media";                     
	# ea = "enterprise architecture";
	# es = "enterprise systems";
	# game = "game";
	# hardware = "hardware";                   
	# pm = "project management";
	# security = "security";
	# cloud = "cloud Computing";
	# database = "database";
	# networking = "networking";
	# design = "design";
	# business = "business";
	# modeling = "modeling";
	# programming = "programming";


	anaCount = 0
	cioCount = 0
	dataCount = 0
	desCount = 0
	hardCount = 0
	gameCount = 0
	workCount = 0
	conCount = 0
	itsCount = 0
	netCount = 0
	progCount = 0
	pmCount = 0
	saleCount = 0
	secCount = 0
	saCount = 0
	teaCount = 0
	testCount = 0
	cloudCount = 0
	webCount = 0
	otherCount = 0

	for i in range(leng):
		outline = data[i]['job_name'] 			# may change into look in description
		out = data[i]['outline']
		if anaA in outline :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaB in outline :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaC in outline :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaD in outline :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaE in outline :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaF in outline :
			data[i]['skill'] = 'Analysis'
			anaCount += 1						#End Analysis

		elif cioA in outline :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioB in outline :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioC in outline :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioD in outline :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioE in outline :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1						#End CIO Management

		elif dataA in outline :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataB in outline :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataC in outline :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataD in outline :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataE in outline :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataF in outline :
			data[i]['skill'] = 'Database'
			dataCount	+= 1					#End Database

		elif desA in outline :
			data[i]['skill'] = 'Design'
			desCount += 1
		elif desB in outline :
			data[i]['skill'] = 'Design'
			desCount += 1
		elif desC in outline :
			data[i]['skill'] = 'Design'
			desCount += 1
		elif desD in outline :
			data[i]['skill'] = 'Design'
			desCount += 1 						#End Design

		elif gameA in outline :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameB in outline :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameC in outline :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameD in outline :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameE in outline :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameF in outline :
			data[i]['skill'] = 'Game'
			gameCount	+= 1					#End Game

		elif hardA in outline :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1
		elif hardB in outline :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1
		elif hardC in outline :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1
		elif hardD in outline :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1					#End Hardware Specalist

		elif workA in outline :
			data[i]['skill'] = 'Work Experience'
			workCount	+= 1	
		elif workB in outline :
			data[i]['skill'] = 'Work Experience'
			workCount	+= 1	
		elif workC in outline :
			data[i]['skill'] = 'Work Experience'
			workCount	+= 1					#End Work Experience

		elif conA in outline :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conB in outline :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conC in outline :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conD in outline :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conE in outline :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conF in outline :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1					#End Consulting

		elif itsA in outline :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsB in outline :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsC in outline :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsD in outline :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsE in outline :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsF in outline :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1					#End IT Support

		elif netA in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netB in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netC in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netD in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netE in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netF in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netG in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netH in outline :
			data[i]['skill'] = 'Networking'
			netCount	+= 1					#End Networking

		elif progA in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progB in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progC in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progD in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progE in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progF in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progG in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progH in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progI in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progJ in outline :
			data[i]['skill'] = 'Programming'
			progCount	+= 1					#End Programming

		elif pmA in outline :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmB in outline :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmC in outline :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmD in outline :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmF in outline :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1						#End Project Management

		elif saleA in outline :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleB in outline :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleC in outline :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleD in outline :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleE in outline :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1					#End Sales

		elif secA in outline :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secB in outline :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secC in outline :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secD in outline :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secE in outline :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secF in outline :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secG in outline :
			data[i]['skill'] = 'Security'
			secCount += 1						#End Security

		elif saA in outline :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saB in outline :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saC in outline :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saD in outline :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saE in outline :
			data[i]['skill'] = 'System  Administration'
			saCount += 1						#End System  Administration


		elif teaA in outline :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaB in outline :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaC in outline :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaD in outline :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaE in outline :
			data[i]['skill'] = 'Teachers'
			teaCount += 1						#End Teachers



		elif testA in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testB in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testC in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testD in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testE in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testF in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testG in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testH in outline :
			data[i]['skill'] = 'Testers'
			testCount += 1						#End Testers

		elif cloudA in outline :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudB in outline :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudC in outline :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudD in outline :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudE in outline :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1						#End Cloud

		elif webA in outline :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webB in outline :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webC in outline :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webD in outline :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webE in outline :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webF in outline :
			data[i]['skill'] = 'Web Development'
			webCount += 1						#End Web Development 


		# Break from Job Title
		elif anaA in out :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaB in out :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaC in out :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaD in out :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaE in out :
			data[i]['skill'] = 'Analysis'
			anaCount += 1
		elif anaF in out :
			data[i]['skill'] = 'Analysis'
			anaCount += 1						#End Analysis

		elif cioA in out :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioB in out :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioC in out :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioD in out :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1
		elif cioE in out :
			data[i]['skill'] = 'CIO Management'
			cioCount += 1						#End CIO Management

		elif dataA in out :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataB in out :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataC in out :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataD in out :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataE in out :
			data[i]['skill'] = 'Database'
			dataCount += 1
		elif dataF in out :
			data[i]['skill'] = 'Database'
			dataCount	+= 1					#End Database

		elif desA in out :
			data[i]['skill'] = 'Design'
			desCount += 1
		elif desB in out :
			data[i]['skill'] = 'Design'
			desCount += 1
		elif desC in out :
			data[i]['skill'] = 'Design'
			desCount += 1
		elif desD in out :
			data[i]['skill'] = 'Design'
			desCount += 1 						#End Design

		elif gameA in out :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameB in out :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameC in out :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameD in out :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameE in out :
			data[i]['skill'] = 'Game'
			gameCount	+= 1
		elif gameF in out :
			data[i]['skill'] = 'Game'
			gameCount	+= 1					#End Game

		elif hardA in out :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1
		elif hardB in out :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1
		elif hardC in out :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1
		elif hardD in out :
			data[i]['skill'] = 'Hardware Specalist'
			hardCount	+= 1					#End Hardware Specalist

		elif workA in out :
			data[i]['skill'] = 'Work Experience'
			workCount	+= 1	
		elif workB in out :
			data[i]['skill'] = 'Work Experience'
			workCount	+= 1	
		elif workC in out :
			data[i]['skill'] = 'Work Experience'
			workCount	+= 1					#End Work Experience

		elif conA in out :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conB in out :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conC in out :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conD in out :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conE in out :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1	
		elif conF in out :
			data[i]['skill'] = 'Consulting'
			conCount	+= 1					#End Consulting

		elif itsA in out :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsB in out :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsC in out :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsD in out :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsE in out :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1
		elif itsF in out :
			data[i]['skill'] = 'IT Support'
			itsCount	+= 1					#End IT Support

		elif netA in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netB in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netC in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netD in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netE in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netF in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netG in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1
		elif netH in out :
			data[i]['skill'] = 'Networking'
			netCount	+= 1					#End Networking

		elif progA in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progB in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progC in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progD in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progE in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progF in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progG in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progH in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progI in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1
		elif progJ in out :
			data[i]['skill'] = 'Programming'
			progCount	+= 1					#End Programming

		elif pmA in out :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmB in out :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmC in out :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmD in out :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1	
		elif pmF in outline :
			data[i]['skill'] = 'Project Management'
			pmCount	+= 1						#End Project Management

		elif saleA in out :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleB in out :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleC in out :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleD in out :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1
		elif saleE in out :
			data[i]['skill'] = 'Sales'
			saleCount	+= 1					#End Sales

		elif secA in out :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secB in out :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secC in out :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secD in out :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secE in out :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secF in out :
			data[i]['skill'] = 'Security'
			secCount += 1	
		elif secG in out :
			data[i]['skill'] = 'Security'
			secCount += 1						#End Security

		elif saA in out :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saB in out :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saC in out :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saD in out :
			data[i]['skill'] = 'System  Administration'
			saCount += 1
		elif saE in out :
			data[i]['skill'] = 'System  Administration'
			saCount += 1						#End System  Administration


		elif teaA in out :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaB in out :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaC in out :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaD in out :
			data[i]['skill'] = 'Teachers'
			teaCount += 1
		elif teaE in out :
			data[i]['skill'] = 'Teachers'
			teaCount += 1						#End Teachers



		elif testA in out :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testB in out :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testC in out :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testD in out :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testE in out :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testF in out :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testG in out :
			data[i]['skill'] = 'Testers'
			testCount += 1	
		elif testH in out :
			data[i]['skill'] = 'Testers'
			testCount += 1						#End Testers

		elif cloudA in out :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudB in out :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudC in out :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudD in out :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1	
		elif cloudE in out :
			data[i]['skill'] = 'Cloud'
			cloudCount += 1						#End Cloud

		elif webA in out :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webB in out :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webC in out :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webD in out :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webE in out :
			data[i]['skill'] = 'Web Development'
			webCount += 1
		elif webF in out :
			data[i]['skill'] = 'Web Development'
			webCount += 1						#End Web Development 

		else :  #Deafult
			data[i]['skill'] = 'others'
			otherCount += 1


		pprint(data[i]['skill'])
	pprint(leng)	
	pprint(anaCount)
	pprint(otherCount)



with open('job_withURL.json', 'w') as f:
    f.write(json.dumps(data) + '\n') # write the new data into the json




	    #f.seek(0)        # <--- should reset file position to the beginning.
	    #json.dump(json_data, f, indent=4)
	    #f.truncate()     # remove remaining part



    #for thing in new_things:
    	#i.write(json.dumps(thing) + '\n')

