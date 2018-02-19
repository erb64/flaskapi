task_routes = {
    "read one task": {
        "url": "/api/task/<string:username>",
        "method": "GET"
    },
    "create new task": {
        "url": "/api/task/add",
        "method": "POST"
    },
    "update task": {
        "url": "/api/task/<string:id>",
        "method": "PUT"
    },
    "delete task": {
        "url": "/api/task/<string:id>",
        "method": "DELETE"
    }
}