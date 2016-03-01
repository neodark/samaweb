# generate deployment samaweb/settings.py
def get_line_number(filename, search_phrase):
    _f = open(filename,'r')
    line_num = 0
    found_line_num = -1
    for line in _f.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
            found_line_num = line_num
    _f.close()
    return found_line_num

line_to_add = get_line_number('samaweb/samaweb/deployment_settings.py','TEMPLATE_DEBUG')

f = open("samaweb/samaweb/deployment_settings.py", "r")
contents = f.readlines()
f.close()

f = open("settings_data_to_insert.txt", "r")
contents_to_insert = f.readlines()
f.close()

s=""
final_contents_to_add = s.join(contents_to_insert)
contents.insert(line_to_add, final_contents_to_add)

f = open("samaweb/samaweb/settings.py", "w")
contents = "".join(contents)
f.write(contents)
f.close()

# generate RUN
from shutil import copyfile
copyfile("deployment_RUN", "samaweb/RUN")
import os
os.system("chmod ug+x samaweb/RUN")
os.system("chmod o-r samaweb/RUN")

# generate samaweb.pid
from shutil import copyfile
copyfile("deployment_samaweb_pid", "samaweb/samaweb.pid")
