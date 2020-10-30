
class WorldMap:
    def __init__(self):
        self.ZONENAME = ""
        self.DESCRIPTION = "description"
        self.EXAMINATION = "examination"
        self.SOLVED = False
        self.UP = "up", "north"
        self.DOWN = "down", "south"
        self.LEFT = "left", "west"
        self.RIGHT = "right", "east"

    def solved_places(self):
        solvedPlaces = {
            "a1": False,
            "a2": False,
            "a3": False,
            "a4": False,
            "b1": False,
            "b2": False,
            "b3": False,
            "b4": False,
            "c1": False,
            "c2": False,
            "c3": False,
            "c4": False,
            "d1": False,
            "d2": False,
            "d3": False,
            "d4": False,
        }

    def zonemaps(self):
        areas = {
            ###### A #####
            "a1": {
                self.ZONENAME: "",
                self.DESCRIPTION: "tower of city",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "",
                self.DOWN: "b1",
                self.LEFT: "",
                self.RIGHT: "a2",
            },
            "a2": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "",
                self.DOWN: "b2",
                self.LEFT: "a1",
                self.RIGHT: "a3",
            },
            "a3": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "",
                self.DOWN: "b3",
                self.LEFT: "a2",
                self.RIGHT: "a4",
            },
            "a4": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "",
                self.DOWN: "b4",
                self.LEFT: "a3",
                self.RIGHT: "",
            },
            ##### B #####
            "b1": {
                self.ZONENAME: "",
                self.DESCRIPTION: "yahallo, welcome to my city!!",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "a1",
                self.DOWN: "c1",
                self.LEFT: "",
                self.RIGHT: "b2",
            },
            "b2": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "a2",
                self.DOWN: "c2",
                self.LEFT: "b1",
                self.RIGHT: "b3",
            },
            "b3": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "a3",
                self.DOWN: "c3",
                self.LEFT: "b2",
                self.RIGHT: "b4",
            },
            "b4": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "a4",
                self.DOWN: "c4",
                self.LEFT: "b3",
                self.RIGHT: "",
            },
            #### C #####
             "c1": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "b1",
                self.DOWN: "d1",
                self.LEFT: "",
                self.RIGHT: "c2",
            },
            "c2": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "b2",
                self.DOWN: "d2",
                self.LEFT: "c1",
                self.RIGHT: "c3",
            },
            "c3": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "b3",
                self.DOWN: "d3",
                self.LEFT: "c2",
                self.RIGHT: "c4",
            },
            "c4": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "b4",
                self.DOWN: "d4",
                self.LEFT: "c3",
                self.RIGHT: "",
            },
            ###### D #######
             "d1": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "c1",
                self.DOWN: "",
                self.LEFT: "",
                self.RIGHT: "d2",
            },
            "d2": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "c2",
                self.DOWN: "",
                self.LEFT: "d1",
                self.RIGHT: "d3",
            },
            "d3": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "c3",
                self.DOWN: "",
                self.LEFT: "d2",
                self.RIGHT: "d4",
            },
            "d4": {
                self.ZONENAME: "",
                self.DESCRIPTION: "description",
                self.EXAMINATION: "examine",
                self.SOLVED: False,
                self.UP: "c4",
                self.DOWN: "",
                self.LEFT: "d3",
                self.RIGHT: "",
            },

        }
        
        return areas
