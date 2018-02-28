user_routes = {
    "read one user": {
        "url": "/api/user/<string:username>",
        "method": "GET"
    },
    "create new user": {
        "url": "/api/user/add",
        "method": "POST"
    },
    "update user info": {
        "url": "/api/user/<string:username>",
        "method": "PUT"
    },
    "delete user": {
        "url": "/api/user/<string:username>",
        "method": "DELETE"
    }
}