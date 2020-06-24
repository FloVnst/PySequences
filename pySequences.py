import matplotlib.pyplot as plt


class Sequence:

    def __init__(self, sequenceType: str, formula, sequenceName: str = "u"):
        """
        :param sequenceType: "function", "recurrenceRelation" or "pointsList"
        :param formula: data enabling to calculate the sequence values

            Examples :

            *   if sequenceType parameter is equal to "function" :
                    u(n) = 3n + 5 :
                    formula parameter will be equal to  :
                        formula = lambda n : 3n + 5

            *   if sequenceType parameter is equal to "recurrenceRelation" :
                    u_n+1 = u_n * 3 + 1
                    u_2 = 5
                    formula parameter will be equal to the tuple (n0, u_n0, i, u_nPlusI):
                        formula = (2, 5, 1, lambda u_n : u_n * 3 + 1)

            *   if sequenceType parameter is equal to "pointsList" :
                    For the set {(0,7), (1,5), (2,3), (3,1.5), (4,1)},
                    formula parameter will be equal to the following list :
                        formula = {0: 7, 1: 5, 2: 3, 3: 1.5, 4: 1}

        :param sequenceName: the sequence name ("u" is the default value)
        :return: None
        """

        self.name = sequenceName

        # dictionary storing the constants used to calculate the coordinates of the sequence points
        self.constants = {}

        # dictionary storing the sequence points
        self.pointsList = {}

        # sequence obtained from a function
        if sequenceType == "function":
            self.type = "function"
            self.formula = formula

        # sequence obtained from a recurrence relation
        elif sequenceType == "recurrenceRelation":
            self.type = "recurrenceRelation"
            self.n0 = formula[0]  # n-coordinate for which we already know the y-ordinate
            self.u_n0 = formula[1]  # y-coordinate for the n0 abscissa-position
            self.stepI = formula[2]  # step i between each n-coordinate (integer)
            self.u_nPlusI = formula[3]  # recurrence relation between n and n + i (aka n + step) (a lambda function)
            self.pointsList = {self.n0: self.u_n0}

        # sequence obtained from a points list
        elif sequenceType == "pointsList" and isinstance(formula, dict):
            self.type = "pointsList"
            self.pointsList = formula

        else:
            print("---\nERROR: unrecognized sequence type.\nsequenceType parameter can only take \"function\","
                  "\"recurrenceRelation\" and \"pointsList\" as value.\nRead the documentation for more information."
                  "\n---")
            self.type = None

    def calc(self, n, store_point: bool = False):
        """
        Calculate the y-ordinate for a given n-position
        :param n: the n-position for which to calculate the y-ordinate
        :param store_point: boolean precising if the new calculated point must be stored in self.pointsList
        :return: the y-ordinate for the given n-position
        """
        if self.type == "function":
            result = self.formula(n)
            if store_point:
                self.pointsList[n] = result
            return result

        elif self.type == "recurrenceRelation":
            u_n = self.u_n0
            if n >= self.n0 + 1:
                for n_temp in range(self.n0 + 1, n + 1, self.stepI):
                    u_n = self.u_nPlusI(u_n)
                    if n == n_temp and store_point:
                        self.pointsList[n] = u_n
            return u_n

        elif self.type == "pointsList":
            if n in self.pointsList.keys():
                return self.pointsList[n]
            else:
                print("WARNING: none point with n = " + str(n) + " is stored in Sequence.pointsList.")

    def printAllStoredPoints(self):
        """
        Displaying of the coordinates of the stored sequence points.
        :return: None
        """
        for n, u_n in self.pointsList.items():
            print(self.name + "_" + str(n) + " = " + str(u_n))

    def draw(self, markerSize: float = 2, markerColor="0"):
        """
        Display all the terms of the sequence on a graph.
        :param markerSize: the size of the points on the graph
        :param markerColor: the color of the points on the graph
        :return None
        """
        for n, u_n in self.pointsList.items():
            plt.scatter(n, u_n, markerSize, markerColor)
        plt.show()


class Trace:
    def __init__(self, pointsList=None, markerSize: float = 2, markerColor="0"):
        """
        Trace object defined by a list of points.
        :param pointsList: a list of points under the following form : {n: u_n, n': u_n', n'': u_n'', ...}
        :param markerSize: the size of the points on the graph
        :param markerColor: the color of the points on the graph
        :return: None
        """
        if pointsList is None:
            pointsList = {}
        self.pointsList = pointsList

        for n, y in pointsList.items():
            plt.scatter(n, y, markerSize, markerColor)

    def addPoint(self, n, y, markerSize: float = 2, markerColor="0"):
        """
        Add a point to the trace object.
        :param n: the n-coordinate of the point to add
        :param y: the y-coordinate of the point to add
        :param markerSize: the size of the point on the graph
        :param markerColor: the color of the point on the graph
        :return: None
        """
        self.pointsList[n] = y
        plt.scatter(n, y, markerSize, markerColor)

    def addPoints(self, pointsList: dict, markerSize: float = 2, markerColor="0"):
        """
        Add several points to the trace object.
        :param pointsList: a list of points under the form {n0: y_n0, n1: y_n1, ...}
        :param markerSize: the size of the points on the graph
        :param markerColor: the color of the points on the graph
        :return: None
        """
        for n, y in pointsList.items():
            self.addPoint(n, y, markerSize, markerColor)

    def draw(self):
        """
        Draw on a graph all the points added.
        :return: None
        """
        plt.show()
