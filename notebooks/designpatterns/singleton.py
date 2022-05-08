
"""Singleton method use getInstance() instead of constructor"""

class Singleton:
   __instance = None
   temp = 1
   
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton! Use getInstance()")
      else:
         Singleton.__instance = self
            
            
if __name__ == "__main__":
    s1 = Singleton.getInstance()
    print(s1)
    print(s1.temp)
    
    s1.temp += 1
    

    s2 = Singleton.getInstance()
    print(s2)
    print(s2.temp)
    
    s2.temp = 100

    s3 = Singleton.getInstance()
    print(s3)
    print(s3.temp)