from change import create_change_request

def main(template_id, params):
    cr = create_change_request(template_id, params)
    print(cr)


if __name__ == "__main__":
    template_id = "xyz"
    params = {}
    params['Description'] = "Sample CR"
    # Add other parameters
    main(template_id, params)

