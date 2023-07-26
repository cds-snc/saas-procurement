from django import template
import subprocess
import datetime

register = template.Library()

# A custom template tag to display when the application was last updated and the git sha.
@register.simple_tag
def version():
    # get commit sha
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()

    # get the time and format it locally
    time = subprocess.check_output(['git', 'log', '-1', '--format=%cd']).decode('utf-8').strip()
    parsed_time = datetime.datetime.strptime(time, '%a %b %d %H:%M:%S %Y %z')
    formatted_time = parsed_time.strftime('%a %b %d %H:%M:%S %Y')

    # return the formatted time and git sha
    return f"{formatted_time}, Git SHA: {commit}"