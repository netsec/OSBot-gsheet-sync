from osbot_aws.apis.IAM import IAM
from osbot_aws.helpers.Create_Code_Build import Create_Code_Build

class Trigger_Build:

    def __init__(self):
        self.project_name = 'OSBot-gsheet-sync'
        self.account_id = IAM().account_id()
        self.api = Create_Code_Build(account_id=self.account_id, project_name=self.project_name)

    def trigger_task(self,event):
        task_name = event.get('task_name')
        file_id   = event.get('file_id')
        command   = event.get('command')

        if task_name == 'ping':
            return {'status': 'ok', 'data': 'pong'}

        if task_name and file_id and command:
            kvargs = {
                'projectName': self.project_name,
                'buildspecOverride': 'osbot_gsheet_sync/tasks/{0}/buildspec.yml'.format(task_name),
                'environmentVariablesOverride': [{'name': 'file_id', 'value': file_id, 'type': 'PLAINTEXT'},
                                                 {'name': 'command', 'value': command, 'type': 'PLAINTEXT'}]
                # 'sourceVersion'    : task_name
            }
            build_id = self.api.code_build.codebuild.start_build(**kvargs).get('build').get('arn')
            return {'status': 'ok', 'data': build_id}

        return {'status': 'error', 'data': 'required params not provided: task_name, file_id or command '}

