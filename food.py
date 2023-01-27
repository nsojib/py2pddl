from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init


class FoodDomain(Domain):

    Person = create_type("Person")
    Robot = create_type("Robot")
    Landmark = create_type("Landmark")

    @predicate(Robot, Landmark)
    def robot_at(self, r, loc):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Person, Landmark)
    def person_at(self, p, loc):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Landmark)
    def food_location(self, loc):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Person)
    def asked_caregiver_help(self, p):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate()
    def robot_updated_1(self):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate()
    def robot_updated_2(self):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate()
    def init_move_to_landmark(self):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate()
    def init_guide_person_to_landmark_attempt(self):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate()
    def guide_to_succeeded_attempt_1(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
        

    @predicate()
    def guide_to_succeeded_attempt_2(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
        
    @predicate()
    def remind_food_succeeded(self):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate()
    def remind_food_succeeded2(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
 

    @predicate()
    def tried_guide_person_landmark_1(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
        
    @predicate()
    def tried_guide_person_landmark_2(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
        

    @predicate()
    def enable_check_guide_1(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
        
    @predicate()
    def enable_check_guide_2(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
        

    @predicate()
    def success(self):
        """Complete the method signature and specify
        the respective types in the decorator"""
        


    @action(Robot, Person, Landmark)
    def detectPerson(self, r, p, loc):
        precond: list = [self.robot_at(r, loc),~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = []  
        observe: list = [self.person_at(p, loc)] 
        return precond, effect, observe



    @action(Robot)
    def initMoveToLandmark(self, r):
        precond: list = [~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [ self.init_move_to_landmark()]   #TODO: forall
        return precond, effect, []

    @action(Robot, Landmark)
    def moveToLandmark(self, r, to):
        precond: list = [self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.robot_at(r, to), ~self.enable_check_guide_1(), ~self.enable_check_guide_2(), ~self.init_move_to_landmark()]
        return precond, effect, []

    @action(Robot, Person, Landmark)
    def InitguidePersonToLandmarkAttempt(self, r, p, to):
        precond: list = [self.robot_at(r, to), self.person_at(p, to), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.init_guide_person_to_landmark_attempt()]  #TODO: forall
        return precond, effect, []

    @action(Robot, Person, Landmark)
    def guidePersonToLandmarkAttempt1(self, r, p, to):
        precond: list = [~self.tried_guide_person_landmark_1(), self.food_location(to), ~self.init_move_to_landmark(), self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.robot_at(r, to), self.tried_guide_person_landmark_1(), self.enable_check_guide_1(), ~self.init_guide_person_to_landmark_attempt()]
        return precond, effect, []

    @action(Robot, Person, Landmark)
    def guidePersonToLandmarkAttempt2(self, r, p, to):
        precond: list = [self.tried_guide_person_landmark_1(), ~self.tried_guide_person_landmark_2(), self.food_location(to), ~self.init_move_to_landmark(), self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.robot_at(r, to), self.tried_guide_person_landmark_2(), self.enable_check_guide_2(), ~self.init_guide_person_to_landmark_attempt()]
        return precond, effect, []

    @action(Landmark)
    def checkGuideToSucceeded1(self, loc):
        precond: list = [self.tried_guide_person_landmark_1(), self.enable_check_guide_1(), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = []
        observe: list = [self.guide_to_succeeded_attempt_1()] 
        return precond, effect, observe

    @action(Landmark)
    def checkGuideToSucceeded2(self, loc):
        precond: list = [self.tried_guide_person_landmark_2(), self.enable_check_guide_2(), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [] 
        observe: list = [self.guide_to_succeeded_attempt_2()]
        return precond, effect, observe

    @action(Person, Landmark, Landmark)
    def UpdatePersonLoc1(self, p, _from, to):
        precond: list = [self.guide_to_succeeded_attempt_1(), self.person_at(p, _from), self.food_location(to), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [~self.person_at(p, _from), self.person_at(p, to)]
        return precond, effect, []


    @action(Person, Landmark, Landmark)
    def UpdatePersonLoc2(self, p, _from, to):  
        precond: list = [self.guide_to_succeeded_attempt_2(), self.person_at(p, _from), self.food_location(to), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [~self.person_at(p, _from), self.person_at(p, to)]
        return precond, effect, []

    @action()
    def UpdateSuccess1(self):
        precond: list = [self.remind_food_succeeded(), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.success()]

        return precond, effect, []

    @action()
    def UpdateSuccess2(self):
        precond: list = [~self.remind_food_succeeded(), self.remind_food_succeeded2(), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.success()]
        return precond, effect, []

    @action(Person)
    def UpdateSuccess3(self, p):
        precond: list = [~self.remind_food_succeeded(), ~self.remind_food_succeeded2(), self.asked_caregiver_help(p), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.success()]
        return precond, effect, []

    @action(Robot, Person, Landmark)
    def remindAutomatedFoodAt(self, r, p, loc):
        precond: list = [self.robot_at(r, loc), self.person_at(p, loc), self.food_location(loc), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = []
        observe: list = [self.remind_food_succeeded()]
        return precond, effect, observe 
 
    @action(Robot, Person, Landmark)
    def askCaregiverHelpFood1(self, r, p, loc):
        precond: list = [~self.remind_food_succeeded(), ~self.remind_food_succeeded2(), self.robot_at(r, loc), self.person_at(p, loc), ~self.init_move_to_landmark(), ~self.init_guide_person_to_landmark_attempt()]
        effect: list = [self.asked_caregiver_help(p)]
        return precond, effect, []

 
# observe actions should be defined unknown in problem file.
"""
remind cr encompass CR sit and motion sensor
scene 2: if first one failed, second one
scene 3: if first and second one failed, ask caregiver
omit some details.they are implicit.
"""
class FoodProblem(FoodDomain):

    def __init__(self):
        super().__init__()
        """To fill in""" 
        self.landmarks = FoodDomain.Landmark.create_objs(["kitchen", "couch", "home"])
        self.robots=FoodDomain.Robot.create_objs(['pioneer'])
        self.persons=FoodDomain.Person.create_objs(['nathan'])

    @init
    def init(self) -> list:
        at=[
            self.robot_at(self.robots["pioneer"], self.landmarks["home"]),
            self.food_location(self.landmarks['kitchen']), 
        ]
        unknowns=[
            self.person_at(self.persons["nathan"], self.landmarks["couch"]),  #TODO: unknown
            self.person_at(self.persons["nathan"], self.landmarks["kitchen"]),  #TODO: unknown
            self.person_at(self.persons["nathan"], self.landmarks["home"]),  #TODO: unknown
            self.guide_to_succeeded_attempt_1(),
            self.guide_to_succeeded_attempt_2(),
            self.remind_food_succeeded(),
            self.remind_food_succeeded2(),
        ]
        oneofs=[
            self.person_at(self.persons["nathan"], self.landmarks["couch"]),  #TODO: unknown
            self.person_at(self.persons["nathan"], self.landmarks["kitchen"]),  #TODO: unknown
            self.person_at(self.persons["nathan"], self.landmarks["home"]),  #TODO: unknown
        ]
 
        return at, unknowns , oneofs

    @goal
    def goal(self) -> list:
        g=[self.success()]
        return g
