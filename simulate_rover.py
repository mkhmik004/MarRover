import sys,re,math,argparse,turtle
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('file',
        help='Path to txt file'
        )
    parser.add_argument('--graphical', 
        help='visualise rover with turtle; selecte colour',
        choices=[
    "red", "blue", "green", "yellow", "cyan", "magenta",
    "black", "white", "gray", "orange", "purple", "brown",
    "pink", "darkgreen", "lightblue"]
,default='black')
    
    args=parser.parse_args()
    
    if args.file:
        try:
            with open(args.file,'r',errors='ignore') as instructions:
                instructions=instructions.read().lower().strip().split('\n')
        except:
            sys.exit("File not found")    
#dict to store my state
        state = []
        degrees = 0
        cordinates = [0,0]
        counter = 0
        print(f'I\'m at ({cordinates[0]}, {cordinates[1]}) facing {degrees} degrees')
#loop through each line, match keywords then add to state dict
        for instruction in instructions:
            
            if re.match(r'(turn|move) (\d+) (degrees|meters) (clockwise|counterclockwise|forward|backward)',instruction) and 0<=int(re.search(r'\d+', instruction).group())<=360:
                value = re.search(r'\d+', instruction)
                key = re.search(r"clockwise|counterclockwise|forward|backward",instruction)
                state.append([key.group(),value.group()])
            elif not instruction:
                continue
            else:
                state.append(None)
        for action in state:
            counter+=1
            if action==None:
                sys.exit(f"I've encountered an instruction I don't understand, aborting (instruction {counter})")
            else:
                if action[0] in ['forward','backward']:
                    print(f'Moving {action[1]} meters {action[0]} (instruction {counter})')
                      #trigonometry to culculate movements
                    if action[0]=='forward':
                        cordinates[0] += math.sin(math.radians(degrees)) * int(action[1])
                        cordinates[1] +=  math.cos(math.radians(degrees)) * int(action[1])
                    elif action[0]=='backward':
                        cordinates[0] += (-1) * math.sin(math.radians(degrees)) * int(action[1])
                        cordinates[1] += (-1) * math.cos(math.radians(degrees)) * int(action[1])
                        
                elif action[0] in ['clockwise','counterclockwise']:
                    print(f"Turning {action[1]} degrees {action[0]} (instruction {counter})")
                    #angles
                    if action[0]=='clockwise':
                        degrees+=int(action[1])
                    elif action[0]=='counterclockwise':
                        degrees-=int(action[1])
        
            
                    
                print(f"I'm at ({cordinates[0]:.0f}, {cordinates[1]:.0f}) facing {degrees} degrees")
            #turtle gui
        if args.graphical:
            rover=turtle.Turtle()
            rover.color(args.graphical)
            rover.left(90)
            for action in state :
                value = int(action[1])  
                if action[0] == 'forward':
                    rover.forward(value*10)
                elif action[0]=='backward':
                    rover.backward(value*10)
                elif action[0] == 'clockwise':
                    rover.right(value)  
                elif action[0] == 'counterclockwise':
                    rover.left(value)  
            turtle.done()
if __name__=='__main__':
    main()
    
