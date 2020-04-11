from change.main import ChangeManager


change_manager = ChangeManager()

def create_change_request(template_id, params):
    response = change_manager.create_cr(template_id=template_id, params=params)

    return response

