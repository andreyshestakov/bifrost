from ansible.plugins.callback import CallbackBase
from ansible import constants as C

class CallbackModule(CallbackBase):
    """
    This Ansible callback plugin writes file report_failed.txt with list of
    failed/unreacheble hosts after playbook finish.
    """
    CALLBACK_VERSION = 1.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'report_failed'
    CALLBACK_NEEDS_WHITELIST = True

    def v2_playbook_on_stats(self, stats):
        hosts = stats.processed.keys()
        failed_hosts = []
        for h in hosts:
            s = stats.summarize(h)
            if s['failures'] or s['unreachable']:
                failed_hosts.append(h)
        with open('report_failed.txt', 'w') as f:
            f.write(",".join(failed_hosts))
