# scrum-reporting-frontend


## Program

### Add a program

curl -H "Content-Type: application/json" -X POST -d '{"programme_name":"xyz","programme_manager":"Walter White", "service_manager": "Jesse Pinkman"}' http://localhost:5000/add/programme

### Get all programs

curl  http://localhost:5000/get/programmes

### Add a project

curl -H "Content-Type: application/json" -X POST -d '{"project_name":"abc", "programme_id": "1", "product_owner": "Gus Fring", "scrum_master": "Saul Goodman"}' http://localhost:5000/add/project

### Get all programs

curl  http://localhost:5000/get/projects
