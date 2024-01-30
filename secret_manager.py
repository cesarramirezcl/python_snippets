import json
from google.cloud import secretmanager
from google.cloud import _helpers

class SecretManager:
    def __init__(self, project_id=None):
        self.client = secretmanager.SecretManagerServiceClient()
        self.project_id = project_id if project_id else _helpers._determine_default_project()

    def get_secret_data(self, secret_id, version_id):
        secret_detail = f"projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}"
        response = self.client.access_secret_version(request={"name": secret_detail})
        raw_secret = response.payload.data.decode("UTF-8")
        return json.loads(raw_secret[raw_secret.index("{")::])
