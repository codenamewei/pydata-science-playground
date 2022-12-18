import os

class PlayingCard:
    
    def test(self):
        
        outdir = os.path.abspath(os.path.dirname(__file__))
        print(outdir)
        
        
pc = PlayingCard()

pc.test()