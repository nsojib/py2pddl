from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init


class AirCargoDomain(Domain):

    Cargo = create_type("Cargo")
    Airport = create_type("Airport")
    Plane = create_type("Plane")

    @predicate(Plane, Airport)
    def plane_at(self, p, a):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Cargo, Airport)
    def cargo_at(self, c, a):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Cargo, Plane)
    def in_(self, c, p):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @action(Cargo, Plane, Airport)
    def load(self, c, p, a):
        precond: list = [self.cargo_at(c,a), self.plane_at(p,a)]
        effect: list =  [~self.cargo_at(c, a), self.in_(c, p)]
        return precond, effect, []

    @action(Cargo, Plane, Airport)
    def unload(self, c, p, a):
        precond: list = [self.in_(c, p), self.plane_at(p,a)]
        effect: list =  [self.cargo_at(c,a) , ~self.in_(c,p)]
        return precond, effect, []

    @action(Plane, Airport, Airport)
    def fly(self, p, org, dst):
        precond: list = [self.plane_at(p, org)]
        effect: list = [~self.plane_at(p, org), self.plane_at(p, dst)]
        return precond, effect, []


class AirCargoProblem(AirCargoDomain):

    def __init__(self):
        super().__init__()
        """To fill in"""
        self.cargos = AirCargoDomain.Cargo.create_objs( [1, 2], prefix="c")
        self.planes = AirCargoDomain.Plane.create_objs( [1, 2], prefix="p")
        self.airports = AirCargoDomain.Airport.create_objs( ["sfo", "jfk"])


    @init
    def init(self) -> list:
        at =[
            self.cargo_at(self.cargos[1], self.airports["sfo"]),
            self.cargo_at(self.cargos[2], self.airports["jfk"]),
            self.plane_at(self.planes[1], self.airports["sfo"]),
            self.plane_at(self.planes[2], self.airports["jfk"]),
        ]
        return at

    @goal
    def goal(self) -> list:
        to =[
            self.cargo_at(self.cargos[1], self.airports["jfk"]),
            self.cargo_at(self.cargos[2], self.airports["sfo"])
        ]
        return to 
