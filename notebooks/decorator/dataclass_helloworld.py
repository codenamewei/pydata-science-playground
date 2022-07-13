from dataclasses import dataclass

@dataclass
class Cafe:
    name : str
    location: str
    drinks_type: int
        
        
if __name__ == "__main__":
    
    
    cafe = Cafe(name = "Coffee Bean", location = "Seoul", drinks_type = 20)
    
    
    print(cafe)