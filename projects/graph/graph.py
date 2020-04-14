"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        # self.visited = set()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue the first vertex, saving it to a variable
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # Print where we are
                print(path[-1])
                # mark as visited to not repeat
                visited.add(path[-1])
                # Use our function to get all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)  # Make a copy of the list, NOT a reference                    
                    new_path.append(next_vert) # Add the vert to the copied list
                    qq.enqueue(new_path) 


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        stack = Stack()
        # Push the starting point in
        stack.push(starting_vertex)
        # Make a set (visited) to keep track of where we have been
        visited = set()
        # While there is stuff in the stack continue working
        while stack.size() > 0:
            # Pop the first item out of the stack and into our variable
            vertex = stack.pop()
            # If not visited
            if vertex not in visited:
                # Print where we are
                print(vertex)
                # Add to visited to avoid repeating ourselves 
                visited.add(vertex)
                # Loop through and get all the neighbors using our function
                for next_vert in self.get_neighbors(vertex):
                    # Push each one to the stack
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Set visited if not done so already
        if visited is None:
            visited = set()

        # ***Track visited nodes calling the function recursively, on neighbors not visited***
        vertex = starting_vertex
        # If vertex not in visted
        if vertex not in visited:
            # Add vertex to visited
            visited.add(vertex)
            # Print our current vertex
            print(vertex)
            # Iterate over neighbors from vertex calling dft_recursive
            for neighbor in self.get_neighbors(vertex):
                self.dft_recursive(neighbor, visited) # We do nothing if there are no unvisited nodes

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue the first vertex out of the queue and into our variable
            path = qq.dequeue()
            # if not visited, search for vertex
            if path[-1] not in visited:
                # If we found what we're looking for, return it
                if path[-1] == destination_vertex:
                    return path                
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    # Make a copy of the list, NOT a reference
                    new_path = list(path)
                    # Add the vert to the copied list
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        # Returns none by default at the end

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # if not visited
            if path[-1] not in visited:
                # Return if we found what we're looking for
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)  # We copy the list to avoid mutating the original
                    new_path.append(next_vert) # Add the next neighbor
                    ss.push(new_path) # Push the list of neighbors to the stack

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # First run through will be None, set it
        if visited is None:
            visited = set()

        # If we don't have a path yet set it
        if path is None:
            path = []

        # We only want to do the work on a node/neighbor we haven't visited yet
        if starting_vertex not in visited:
            # First step is to add it to the visited array so we don't repeat our work
            visited.add(starting_vertex)
            # Copy the path, do not just append!
            path_copy = path.copy()
            path_copy.append(starting_vertex) # Appended to the copied path
            # If we found what we're looking for return it
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                # Create a new path/list recursively
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_copy)
                # Return the path only if we were able to find it
                if new_path is not None:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

