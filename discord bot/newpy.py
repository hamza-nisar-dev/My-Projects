import libtmux
from libtmux import Pane, Session, Window, exc
with open('lan2.py', 'r') as input:
    output = open('example.py', 'w')
    output.write(input.read())
    output.close()

with open('example.py', 'r') as file:
    data = file.readlines()
data[1] = "Here is my modified Line 2\n"
  
with open('example.py', 'w') as file:
    file.writelines(data)
server = libtmux.Server()
Session= server.new_session(session_name="bot", detach=True)
Window=Session.new_window(attach=False,window_name='test_window')
pane = Window.split_window(attach=False)
pane.send_keys('python3 cryptoshop.py', enter=False)
pane.enter()