from test_data import TEST_CUSTOMERS


def check_customer_data(customer_data, recalled_data):
    """
    Compare expected customer information
    with the information returned by the system.
    """

    results = {}

    for key, expected_value in customer_data.items():

        actual_value = recalled_data.get(key)

        if actual_value == expected_value:
            results[key] = "PASS"
        else:
            results[key] = {
                "status": "FAIL",
                "expected": expected_value,
                "actual": actual_value
            }

    return results


# Example test
if __name__ == "__main__":

    expected = TEST_CUSTOMERS[0]

    # This is an example of what the system might return.
    # Later replace this with the actual Hindsight result.
    recalled = {
        "customer": "ABC Technologies",
        "budget": "₹10 lakh",
        "concern": "Security",
        "competitor": "Microsoft"
    }

    results = check_customer_data(expected, recalled)

    print("Memory Test Result")
    print("------------------")

    for key, result in results.items():
        print(key, ":", result)