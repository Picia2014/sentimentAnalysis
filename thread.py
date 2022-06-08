import threading

class myThread (threading.Thread):
   def __init__(self, threadID, name, method):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.method = method

   def run(self):
      self.method()

