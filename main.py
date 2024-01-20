# visit website: https://api.npoint.io/97733ee8ec42a3ecb5ee
# visit website: https://api.npoint.io/ea1e3a670427d08fdb06

from json_editor_file import JsonEditor
from udemy_file import Udemy

user = Udemy(course_url="https://www.udemy.com/course/machinelearning/")
content = user.get_details()
print(content)

obj = JsonEditor(content)