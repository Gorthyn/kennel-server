DATABASE = {
    "animals": [
        {
            "id": 1,
            "name": "Snickers",
            "species": "Dog",
            "locationId": 1,
            "customerId": 4,
            "status": "Admitted"
        },
        {
            "id": 2,
            "name": "Roman",
            "species": "Dog",
            "locationId": 1,
            "customerId": 2,
            "status": "Admitted"
        },
        {
            "id": 3,
            "name": "Blue",
            "species": "Cat",
            "locationId": 2,
            "customerId": 1,
            "status": "Admitted"
        }
    ],
    "customers": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        },
        {
            "id": 2,
            "name": "Bob Guess"
        }
    ],
    "employees": [
        {
            "id": 1,
            "name": "Jenna Solis"
        },
        {
            "id": 2,
            "name": "Matthew Anmar"
        }
    ],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]
}



def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]


def retrieve(resource, id):
    """For GET requests to a single resource"""
    requested_resource = None
    for item in DATABASE[resource]:
        if item["id"] == id:
            requested_resource = item

    return requested_resource

def create(resource, post_body):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]
    new_id = max_id + 1
    post_body["id"] = new_id
    DATABASE[resource].append(post_body)

    return post_body


def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            DATABASE[resource][index] = post_body
            break


def delete(resource, id):
    """For DELETE requests to a single resource"""
    resource_index = None
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            resource_index = index

        if resource_index is not None:
            DATABASE[resource][index].pop(resource_index)
