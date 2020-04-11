from change import create_change_request

def main(env, template_name, params):
    cr = create_change_request(env, template_name, params)
    print(cr)


if __name__ == "__main__":
    template_name = "xyz"
    env = "dev"
    params = {}
    params['Description'] = "Sample CR"
    # Add other parameters
    main(env, template_name, params)

