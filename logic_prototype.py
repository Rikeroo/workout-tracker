import time
from datetime import date

class Workout:
    """
    Takes timezone 'date' and list of exercise objects 'exercises'
    
    """
    def __init__(self, date, exercises):
        """Initialises Workout object

        Args:
            date ('date' object): Date of workout start
            exercises (List of 'Exercise' objects): 
        """
        self.date = date
        self.exercises = exercises
        self.volume = 0
        self.update()
    
    def __str__(self):
        exercises_str = ""
        for e in self.exercises:
            exercises_str += f"{e}"
        return f"Date: {self.date}\nVolume: {self.volume}\n{exercises_str}"
   
    def update(self):
        vol_total = 0
        for e in self.exercises:
           vol_total += e.volume
        self.volume = vol_total
           
    
    # def getVolume(self):

# This might not be best practice, as this is just data?    
class Exercise:
    """
    Each exercise has list of sets with attributes: reps, weight
    e.g. exercise.getSet(x) returns array [set_num, weight, reps]
    """

    def __init__(self, name, sets, notes=""):
        """Initialises class with arguments: sets (2d list) and
        notes (string)

        Args:
            name (string): Name of exercise
            sets (list): 2D list [[set_num,weight,reps],...]
            notes (string): notes for specific exercise
        """
        self.name = name
        self.sets = sets
        self.notes = notes
        self.volume = 0
        self.update()
        
    def __str__(self):
        sets_str = ""
        for s in self.sets:
            sets_str += f"Set: {s[0]}, Weight: {s[1]}, Reps: {s[2]}\n"
        return f"Name: {self.name}\n{sets_str}"
    
    def update(self):
        total = 0
        for s in self.sets:
            total += s[1]*s[2]
        self.volume = total
    
    def getVolume(self):
        self.update()
        return self.volume
            
            
test_sets = [[1, 10, 10],
            [2, 20, 10],
            [3, 30, 8],
            [4, 40, 5],
            [5, 50, 5]]

# Create test exercise objects
e1 = Exercise('Finger Pulls',test_sets)
e2 = Exercise('Test Exercise 2', test_sets)
print(e1)
print(e2)

# print(f"Volume: {e1.getVolume()}")

# Put Exercises into a workout
w1 = Workout(date.today(),[e1,e2])
print(w1)
# print(f"Workout Volume: {w1.volume}")