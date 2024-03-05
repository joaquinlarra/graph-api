class GraphError(Exception):
    pass

class NodeNotFoundError(GraphError):
    pass

class CycleDetectedError(GraphError):
    pass
