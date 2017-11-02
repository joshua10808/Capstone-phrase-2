import json
from pprint import pprint

path ='..\\Scrapy_Code\\seekinfo.json'

with open(path,'r') as data_file: 
    data = json.load(data_file) # load in line?
    leng = len(data)
    i = 0
    a = 0

    check = []

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


    #Analysis
    check.append("Analysis")
    check.append("Business Intelligence")
    check.append("Business Analyst")
    check.append("Technical Analyst")
    check.append("Systems Analyst")
    check.append("Support Analyst")
    check.append("Application Analyst")

    #CIO/Management
    check.append("Chief Information Officer")
    check.append("Business Development Manager")
    check.append("Technology Lead")
    check.append("Policy Officer")
    check.append("Chief Technology Officer")

    #Database
    check.append("Database Administrator")
    check.append("Data Warehouse")
    check.append("Database Developer")
    check.append("SQL")
    check.append("Data Management")
    check.append("Database Engineer")


    #Design 
    check.append("Designer")
    check.append("User Experience Designer")
    check.append("Design Engineer")
    check.append("Graphic Designer")

    #Game 
    check.append("Game")
    check.append("Games Developer")
    check.append("Games Designer")
    check.append("Games Illustrator")
    check.append("Games Artist")
    check.append("Artist")

    #Hardware Specalist
    check.append("Hardware Engineer")
    check.append("Embedded Systems Engineer")
    check.append("Electronics Engineer")
    check.append("Electronics Technician")

    #Work Experience
    check.append("Internship")
    check.append("Work Experience")
    check.append("Student Program")

    #Consulting
    check.append("Consultant")
    check.append("Technical Consultant")
    check.append("Senior Consultant")
    check.append("ERP Consultant")
    check.append("Infrastructure Consultant")
    check.append("SAP Consultant")

    #IT Support
    check.append("Desktop Support")
    check.append("Support Technician")
    check.append("Application Support Specialist")
    check.append("Help Desk Support")
    check.append("IT Support")
    check.append("Service Desk Analyst")

    #Networking
    check.append("Network Designer")
    check.append("Network Engineer")
    check.append("Network Administrator")
    check.append("Field Network Technician")
    check.append("Radio Communications")
    check.append("Telecommunications")
    check.append("Infrastructure Engineer")
    check.append("Network Architect")

    #Programming
    check.append("Java Developer")
    check.append("Embedded Software Engineer")
    check.append("Software Developer")
    check.append("Senior Developer")
    check.append("Full Stack Engineer")
    check.append("Software Engineer")
    check.append("Applications Developer")
    check.append("C# Developer")
    check.append("C++ Developer")
    check.append("Programmer")

    #Project Management
    check.append("ICT Project Manager")
    check.append("Senior ERP Project Manager")
    check.append("Project Coordinator")
    check.append("Program Delivery Lead")
    check.append("Site Supervisor")
    check.append("Deployment Officer")

    #Sales
    
    check.append("Sales Manager")
    check.append("Field Sales Representative")
    check.append("Sales Administrator")
    check.append("Sales Specialists")
    check.append("Sales Solutions Specialist")

    #Security
    
    check.append("Security Management Officer")
    check.append("Information Security Analyst")
    check.append("Cyber Security Engineer")
    check.append("Information Security Specialist")
    check.append("Security Advisor")
    check.append("Information Security Manager")

    #System  Administration
 
    check.append("Systems Administrator")
    check.append("Systems Manager")
    check.append("Platform Manager")
    check.append("SharePoint Administrator")
    check.append("Systems Engineer")

    #Teachers

    check.append("Teacher")
    check.append("Lecturer")
    check.append("ICT Trainer")
    check.append("Telecommunications Trainer")
    check.append("Software Development Trainer")

    #Testers
    check.append("Test Lead")
    check.append("Test Manager")
    check.append("Test Analyst")
    check.append("Test Engineer")    
    check.append("Performance Tester")
    check.append("Test Co-ordinator")
    check.append("Software Tester")
    check.append("Automation Tester")

    #Cloud
    check.append("Cloud Engineer")
    check.append("Storage & Virtualisation")
    check.append("Cloud Services Administrator")
    check.append("Azure Cloud Engineer")
    check.append("VMware Engineer")

    #Web Development 

    check.append("Web Developer")
    check.append("Web App Developer")
    check.append("Web Designer")
    check.append("Front End Web Developer")
    check.append("Fullstack Web Developer")
    check.append("Web UI Developer")
    


    for i in range(leng):
        jobName = data[i]['job_name']      # two check 
        out = data[i]['outline']


        for a in check: #wrong

            if a in out :

                if a <= 6 :
                    data[i]['skill'] = 'Analysis'
                    anaCount += 1  
                elif a >=7  and a <=11 :  
                    skills = 'CIO Management'
                    cioCount += 1 
                elif a >=12  and a <=17 : 
                    skills = 'Database'
                    dataCount += 1
                elif a >=18  and a <=21 : 
                    skills = 'Design'
                    desCount += 1
                elif a >=22  and a <=27 : 
                    skills = 'Game'
                    gameCount += 1
                elif a >=28  and a <=31 : 
                    skills = 'Hardware Specalist'
                    hardCount += 1
                elif a >=32  and a <=34 : 
                    skills = 'Work Experience'
                    workCount += 1
                elif a >=35  and a <=40 : 
                    skills = 'Consulting'
                    conCount += 1
                elif a >=41  and a <=46 : 
                    skills = 'IT Support'
                    itsCount += 1
                elif a >=47  and a <=54 : 
                    skills = 'Networking'
                    netCount += 1
                elif a >=55  and a <=64 : 
                    skills = 'Programming'
                    progCount += 1
                elif a >=65  and a <=70 : 
                    skills = 'Project Management'
                    pmCount += 1
                elif a >=71 and a <=75 : 
                    skills = 'Sales'
                    saleCount += 1
                elif a >=76 and a <=81 :
                    skills = 'Security'
                    secCount += 1
                elif a >=82 and a <=86 :
                    skills = 'System  Administration'
                    saCount += 1
                elif a >=87 and a <=91 :
                    skills = 'Teachers'
                    teaCount += 1
                elif a >=92 and a <=99 :
                    skills = 'Testers'
                    testCount += 1
                elif a >=100 and a <=104 :
                    skills = 'Cloud'
                    cloudCount += 1
                elif a >=105 and a <=110 :
                    skills ='Web Development'             
                    webCount += 1

            else :
                skills ='others' 
                otherCount += 1

    pprint(leng)    
    pprint(anaCount)
    pprint(otherCount)



with open('job_withURL.json', 'w') as f:
    f.write(json.dumps(data) + '\n')