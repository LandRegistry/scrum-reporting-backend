# scrum-reporting-frontend


## Programme

### Add a programme

**End Point**

/add/programme

**Example**

curl -H "Content-Type: application/json" -X POST -d '{"programme_name":"xyz","programme_manager":"Walter White", "service_manager": "Jesse Pinkman"}' http://localhost:5000/add/programme

**Response**

```
{
    "status": "ok"
}
```

### Get all programmes (and project information)

**End Point**

/get/programmes

**Example**

curl  http://localhost:5000/get/programmes

**Response**

```
[
    {
        "service_manager": "Jesse Pinkman",
        "name": "xyz",
        "programme_manager": "Walter White",
        "projects": [],
        "id": 2
    },
    {
        "service_manager": "Jesse Pinkman",
        "name": "zzz",
        "programme_manager": "Walter White",
        "projects": [
            {
                "name": "abc",
                "last_rag": "a",
                "product_owner": "Gustavo Fring",
                "scrum_master": "Saul Goodman",
                "last_end_date": "01-01-2015",
                "id": 1,
                "last_sprint": "4",
                "project_description": "desc",
                "delivery_manager": "Hank Schrader",
                "scrum_tool_link": "http://www.trello.com/...",
                "average_points": 15
            },
            {
                "name": "abc",
                "last_rag": "a",
                "product_owner": "Gustavo Fring",
                "scrum_master": "Saul Goodman",
                "last_end_date": "01-01-2015",
                "id": 2,
                "last_sprint": "4",
                "project_description": "desc",
                "delivery_manager": "Hank Schrader",
                "scrum_tool_link": "http://www.trello.com/...",
                "average_points": 15
            }
        ],
        "id": 1
    }
]
```


### Get specific programme (and project information)

**End Point**

/get/programme/<programme_id>

**Example**

curl  http://localhost:5000/get/programme/1

**Response**

```
{
    "service_manager": "Jesse Pinkman",
    "name": "zzz",
    "programme_manager": "Walter White",
    "projects": [
        {
            "name": "abc",
            "last_rag": "a",
            "product_owner": "Gustavo Fring",
            "scrum_master": "Saul Goodman",
            "last_end_date": "01-01-2015",
            "id": 1,
            "last_sprint": "4",
            "project_description": "desc",
            "delivery_manager": "Hank Schrader",
            "scrum_tool_link": "http://www.trello.com/...",
            "average_points": 15
        },
        {
            "name": "abc",
            "last_rag": "a",
            "product_owner": "Gustavo Fring",
            "scrum_master": "Saul Goodman",
            "last_end_date": "01-01-2015",
            "id": 2,
            "last_sprint": "4",
            "project_description": "desc",
            "delivery_manager": "Hank Schrader",
            "scrum_tool_link": "http://www.trello.com/...",
            "average_points": 15
        }
    ],
    "id": 1
}
```

### update programme

**End Point**

/update/programme/<programme_id>

**Example**

curl -H "Content-Type: application/json" -X POST -d '{"programme_name":"zzz","programme_manager":"Walter White", "service_manager": "Jesse Pinkman"}' http://localhost:5000/update/programme/1

**Response**

```
{
    "status": "updated"
}
```

### delete programme

**End Point**

/delete/programme/<programme_id>

**Example**

curl  http://localhost:5000/delete/programme/1

**Response**

```
{
    "status": "ok"
}
```

## Project

### Add a project

**End Point**

/add/project

**Example**

curl -H "Content-Type: application/json" -X POST -d '{"project_name":"abc", "programme_id": "1", "product_owner": "Gus Fring", "scrum_master": "Saul Goodman", "project_description": "desc"}' http://localhost:5000/add/project

**Response**

```
{
    "status": "ok"
}
```
### Get a project

**End Point**

/get/project/<project_id>

**Example**

curl  http://localhost:5000/get/projects/1

**Response**

```
{
    "scrum_master": "Saul Goodman",
    "programme_id": 1,
    "id": 1,
    "name": "abc",
    "product_owner": "Gus Fring",
    "project_description": "desc",
    "programme_manager": "dsads",
    "programme_name": "dsad",
    "service_manager": "adsa",
    "last_end_date": "01-01-2015",
    "last_sprint": "4",
    "last_rag": "a",
    "delivery_manager": "Hank Schrader",
    "scrum_tool_link": "http://www.trello.com/...",
    "average_points": 15,
    "sprint_array": [
        {
            "agreed_points": 300,
            "sprint_deliverables": "Sprint Deliverables",
            "started_points": 50,
            "sprint_dependencies": "Sprint Dependencies",
            "end_date": "some other date",
            "start_date": "some date",
            "sprint_days": 14,
            "sprint_risks": "Sprint Risks",
            "project_id": 1,
            "delivered_points": 180,
            "sprint_number": "4",
            "sprint_goal": "Sprint Goal",
            "sprint_rag": "a",
            "id": 1,
            "sprint_challenges": "Sprint Challenges",
            "sprint_issues": "Sprint Issues"
        }
    ]
}

```

### Update a project

**End Point**

/update/projects/<project_id>

**Example**

curl -H "Content-Type: application/json" -X POST -d '{"project_name":"abc", "programme_id": "1", "product_owner": "Gustavo Fring", "scrum_master": "Saul Goodman", "project_description": "desc", "delivery_manager": "Hank Schrader", "scrum_tool_link": "http://www.trello.com/..." }' http://localhost:5000/update/project/1

**Response**

```
{
    "status": "ok"
}
```


### delete project

**End Point**

/delete/project/<programme_id>

**Example**

curl  http://localhost:5000/delete/project/1

**Response**

```
{
    "status": "ok"
}
```


## Sprint

### Add a sprint

**End Point**

/add/sprint

**Example**

curl -H "Content-Type: application/json" -X POST -d '{"project_id":"1", "start_date": "some date", "end_date": "some other date", "sprint_number": "4", "sprint_rag": "a", "sprint_goal": "Sprint Goal", "sprint_deliverables": "Sprint Deliverables", "sprint_challenges": "Sprint Challenges", "agreed_points": "300", "delivered_points": "180", "started_points": "50", "sprint_issues": "Sprint Issues", "sprint_risks": "Sprint Risks", "sprint_dependencies": "Sprint Dependencies", "sprint_days": "14"  }' http://localhost:5000/add/sprint

**Response**

```
{
    "status": "ok",
    "id": "5"

}
```

### Update a sprint

**End Point**

/update/sprint/<sprint_id>

**Example**

curl -H "Content-Type: application/json" -X POST -d '{"project_id":"1", "start_date": "some date", "end_date": "some other date", "sprint_number": "4", "sprint_rag": "a", "sprint_goal": "Sprint Goal", "sprint_deliverables": "Sprint Deliverables", "sprint_challenges": "Sprint Challenges", "agreed_points": "400", "delivered_points": "180", "started_points": "50", "sprint_issues": "Sprint Issues", "sprint_risks": "Sprint Risks", "sprint_dependencies": "Sprint Dependencies", "sprint_days": "10"  }' http://localhost:5000/update/sprint/1


**Response**

```
{
    "status": "updated"
}
```

### Get project sprint data

**End Point**

/get/project/<project_id>/<sprint_id>

**Example**

curl http://172.16.42.66:5000/get/project/1/1

**Response**

```
{
    "scrum_master": "Saul Goodman",
    "burndown": [
        {
            "sprint_done": 20,
            "sprint_day": 1
        },
        {
            "sprint_done": 3,
            "sprint_day": 2
        },
        {
            "sprint_done": 3,
            "sprint_day": 3
        },
        {
            "sprint_done": 3,
            "sprint_day": 4
        },
        {
            "sprint_done": 3,
            "sprint_day": 5
        },
        {
            "sprint_done": 3,
            "sprint_day": 6
        },
        {
            "sprint_done": 3,
            "sprint_day": 7
        },
        {
            "sprint_done": 3,
            "sprint_day": 8
        },
        {
            "sprint_done": 3,
            "sprint_day": 9
        },
        {
            "sprint_done": 3,
            "sprint_day": 10
        },
        {
            "sprint_done": 3,
            "sprint_day": 11
        },
        {
            "sprint_done": 3,
            "sprint_day": 12
        },
        {
            "sprint_done": 3,
            "sprint_day": 13
        },
        {
            "sprint_done": 3,
            "sprint_day": 14
        }
    ],
    "agreed_points": 300,
    "sprint_deliverables": "Sprint Deliverables",
    "started_points": 50,
    "sprint_dependencies": "Sprint Dependencies",
    "end_date": "some other date",
    "start_date": "some date",
    "sprint_days": 14,
    "sprint_issues": "Sprint Issues",
    "sprint_risks": "Sprint Risks",
    "project_id": 1,
    "delivered_points": 180,
    "programme_id": 1,
    "sprint_number": "4",
    "name": "abc",
    "sprint_rag": "a",
    "product_owner": "Gus Fring",
    "sprint_goal": "Sprint Goal",
    "script_id": 1,
    "sprint_challenges": "Sprint Challenges",
    "project_description": "desc"
}
```


### Get project sprint data (using sprint_number)

**End Point**

/get/project/<project_id>/sprint_number/<sprint_number>

**Example**

curl http://172.16.42.66:5000/get/project/1/sprint_number/4

**Response**

```
{
    "scrum_master": "Saul Goodman",
    "burndown": [
        {
            "sprint_done": 20,
            "sprint_day": 1
        },
        {
            "sprint_done": 3,
            "sprint_day": 2
        },
        {
            "sprint_done": 3,
            "sprint_day": 3
        },
        {
            "sprint_done": 3,
            "sprint_day": 4
        },
        {
            "sprint_done": 3,
            "sprint_day": 5
        },
        {
            "sprint_done": 3,
            "sprint_day": 6
        },
        {
            "sprint_done": 3,
            "sprint_day": 7
        },
        {
            "sprint_done": 3,
            "sprint_day": 8
        },
        {
            "sprint_done": 3,
            "sprint_day": 9
        },
        {
            "sprint_done": 3,
            "sprint_day": 10
        },
        {
            "sprint_done": 3,
            "sprint_day": 11
        },
        {
            "sprint_done": 3,
            "sprint_day": 12
        },
        {
            "sprint_done": 3,
            "sprint_day": 13
        },
        {
            "sprint_done": 3,
            "sprint_day": 14
        }
    ],
    "agreed_points": 300,
    "sprint_deliverables": "Sprint Deliverables",
    "started_points": 50,
    "sprint_dependencies": "Sprint Dependencies",
    "end_date": "some other date",
    "start_date": "some date",
    "sprint_days": 14,
    "sprint_issues": "Sprint Issues",
    "sprint_risks": "Sprint Risks",
    "project_id": 1,
    "delivered_points": 180,
    "programme_id": 1,
    "sprint_number": "4",
    "name": "abc",
    "sprint_rag": "a",
    "product_owner": "Gus Fring",
    "sprint_goal": "Sprint Goal",
    "script_id": 1,
    "sprint_challenges": "Sprint Challenges",
    "project_description": "desc"
}
```


### delete sprint

**End Point**

/delete/sprint/<programme_id>

**Example**

curl  http://localhost:5000/delete/sprint/1

**Response**

```
{
    "status": "ok"
}
```


## Sprint Burn Down

### Update sprint burndown (use to also add initially)

**End Point**

/update/burn_down

**Example**

curl -H "Content-Type: application/json" -X POST -d '{"sprint_id": "1", "sprint_days": [{"sprint_day": "1", "sprint_done": "20"},{"sprint_day": "2","sprint_done": "3"},{"sprint_day": "3", "sprint_done": "3"},{ "sprint_day": "4","sprint_done": "3"},{"sprint_day": "5","sprint_done": "3"},{"sprint_day": "6","sprint_done": "3"},{"sprint_day": "7","sprint_done": "3"},{"sprint_day": "8","sprint_done": "3"},{"sprint_day": "9","sprint_done": "3"},{"sprint_day": "10","sprint_done": "3"},{"sprint_day": "11","sprint_done": "3"},{"sprint_day": "12","sprint_done": "3"},{"sprint_day": "13","sprint_done": "3"},{"sprint_day": "14","sprint_done": "3"}]}' http://localhost:5000/update/burn_down

**Response**

```
{
    "status": "ok"
}
```
