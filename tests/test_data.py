TEST_CUSTOMERS = [
    {
        "customer": "ABC Technologies",
        "budget": "₹10 lakh",
        "concern": "Security",
        "competitor": "Microsoft"
    },
    {
        "customer": "XYZ Solutions",
        "budget": "₹25 lakh",
        "concern": "Integration",
        "competitor": "Salesforce"
    },
    {
        "customer": "PQR Industries",
        "budget": "₹15 lakh",
        "concern": "Cost",
        "competitor": "Oracle"
    }
]


def get_customer(name):
    for customer in TEST_CUSTOMERS:
        if customer["customer"] == name:
            return customer

    return None
def test_customer_exists():
    customer = get_customer("ABC Technologies")
    assert customer is not None
