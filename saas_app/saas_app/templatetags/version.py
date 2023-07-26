from django import template
import subprocess
import datetime
import os

register = template.Library()


# A custom template tag to display when the application was last updated and the git sha.
@register.simple_tag
def version():
    # set the commit and time to unknown
    commit = time = "Unknown"
    print(os.getenv("GIT_SHA"))

    # get commit sha
    if (os.getenv("ENVIRONMENT") == "dev"):
         # the the commit 
        commit = (
            subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        )

        # get the time and format it locally
        date_time = (
            subprocess.check_output(["git", "log", "-1", "--format=%cd"])
            .decode("utf-8")
            .strip()
        )
        parsed_date_time = datetime.datetime.strptime(date_time, "%a %b %d %H:%M:%S %Y %z")
        formatted_date_time = parsed_date_time.strftime("%a %b %d %H:%M:%S %Y")
    else:

        commit = os.getenv("GIT_SHA")
        formatted_date_time = os.getenv("BUILD_DATE")
    
    # return the formatted time and git sha
    return f"{formatted_date_time}, Git SHA: {commit}"
