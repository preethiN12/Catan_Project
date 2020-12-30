class Land:
    land_type = ''
    probability = 0
    position = 0
    edges = []
    vertices = []
    roads = []
    developments = []
    robber = ''

    def __init__(self, land_type, probability, position, edges, vertices, roads, developments, robber):
        self.land_type = land_type
        self.probability = probability
        self.position = position
        self.edges = edges
        self.vertices = vertices
        self.roads = roads
        self.developments = developments
        self.robber = robber

    def develop(self):
        return

    def get_resources(self):
        return

    def robber(self):
        return

    def build_a_road(self):
        return
