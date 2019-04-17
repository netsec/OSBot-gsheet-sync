from osbot_gsheet_sync.Trigger_Build import Trigger_Build


def run(event, context):
    return Trigger_Build().trigger_task(event)