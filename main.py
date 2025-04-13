melody: List[str] = [
    "E D C D",          
    "E E E:8 R:8",      
    "D D D",           
    "E G G",            
    "E D C D",          
    "E E E:8 R:8",      
    "D D D",            
    "D C"              
]


for measure in melody:
    music.play_melody(measure, 80)
