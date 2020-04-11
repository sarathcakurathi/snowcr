from change.main import ChangeManager


def create_change_request(env, template_name, params):
    change_manager = ChangeManager(env)
    response = change_manager.create_cr(template_name=template_name, params=params)

    return response

