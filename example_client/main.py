import sys

sys.path.insert(0, r'../common')
from util import *

logging.basicConfig()
logger = logging.getLogger('schedule')


class SafeScheduler(Scheduler):
    def __init__(self, reschedule_on_failure=True):
        self.reschedule_on_failure = reschedule_on_failure
        Scheduler.__init__(self)

    def _run_job(self, job):
        try:
            Scheduler._run_job(self, job)
        except Exception:
            attr = CONFIG["gmail"]
            tb = format_exc()
            logger.error(tb)

            msg = MIMEMultipart()
            msg["Subject"] = "Message from JobScheduler [" + getTime() + "]"
            msg.attach(MIMEText(tb))
            
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(attr["username"], attr["password"])
            server.sendmail(attr["fromaddr"], attr["toaddrs"], msg.as_string())
            server.quit()
            
            job.last_run = datetime.datetime.now()
            job._schedule_next_run()
