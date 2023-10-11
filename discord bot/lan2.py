import libtmux
from libtmux import Pane, Session, Window, exc
server = libtmux.Server()
Session= server.new_session(session_name="bot", detach=True)
Window=Session.new_window(attach=False,window_name='test_window')
pane = Window.split_window(attach=False)
pane.send_keys('python3 cryptoshop.py', enter=False)
pane.enter()