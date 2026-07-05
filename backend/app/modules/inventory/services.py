from uuid import UUID


def get_inventory_list():
    # Later: fetch from DB
    return [
        {
            "id": "1",
            "product": "Laptop",
            "quantity": 25,
        },
        {
            "id": "2",
            "product": "Mouse",
            "quantity": 100,
        },
    ]


def get_inventory_item(item_id: UUID):
    # Later: fetch from DB
    return {
        "id": str(item_id),
        "product": "Laptop",
        "quantity": 25,
        "warehouse": "Main Warehouse",
    }
