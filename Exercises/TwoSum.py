class Edge (object):
    def __init__(Self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_dest(self):
        return self.dest

    def __str__(self):
        return '{}->{}'.format(self.src, self.dest)


class WeightedEdge(Edge):
    super().__init__(self, self.src, self.dest)
    self.total_distance = total_distance
    self.outdoor_distance = outdoor_distance