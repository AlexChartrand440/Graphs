"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {};

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set();
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2);
        else:
            raise IndexError("That vertex does not exist!");

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id];

    def bft(self, starting_vertex):

        tv = Queue();

        v = set();
        
        tv.enqueue(starting_vertex);

        while tv.size() > 0:
            n = tv.dequeue();
            if n not in v:
                print(n);
                v.add(n);
                for a in self.vertices[n]:
                    tv.enqueue(a);

    def dft(self, starting_vertex):
        
        tv = Stack();

        v = set();
        
        tv.push(starting_vertex);

        while tv.size() > 0:
            n = tv.pop();
            if n not in v:
                print(n);
                v.add(n);
                for a in self.vertices[n]:
                    tv.push(a);

    def dft_recursive(self, starting_vertex, visited):
        if starting_vertex not in visited:
            print(starting_vertex);
            visited.append(starting_vertex);
            for a in self.vertices[starting_vertex]:
                self.dft_recursive(a, visited);

    def bfs(self, starting_vertex, destination_vertex):
        
        tv = Queue();

        v = set();
        
        tv.enqueue([starting_vertex]);

        while tv.size() > 0:
            p = tv.dequeue();
            if p is None:
                continue;
            if p[len(p) - 1] == destination_vertex:
                return p;
            elif p[len(p) - 1] not in v:
                v.add(p[len(p) - 1]);
                for a in self.vertices[p[len(p) - 1]]:
                    b = p.copy();
                    b.append(a);
                    tv.enqueue(b);

    def dfs(self, starting_vertex, destination_vertex):
        tv = Stack();

        v = set();
        
        tv.push([starting_vertex]);

        while tv.size() > 0:
            p = tv.pop();
            if p is None:
                continue;
            if p[len(p) - 1] == destination_vertex:
                return p;
            elif p[len(p) - 1] not in v:
                v.add(p[len(p) - 1]);
                for a in self.vertices[p[len(p) - 1]]:
                    b = p.copy();
                    b.append(a);
                    tv.push(b);

    def dfs_recursive(self, starting_vertex, destination_vertex, s, visited):
        # s.push([starting_vertex]);
        # p = s.pop();
        print('aaaaaaaaa 4: ' + str(s));
        s.append([starting_vertex]);
        if s[len(s) - 1][len(s[len(s) - 1]) - 1] == destination_vertex:
            return s[len(s) - 1];
        elif s[len(s) - 1][len(s[len(s) - 1]) - 1] not in visited:
            print('aaaaaa: ' + str(s[len(s) - 1][len(s[len(s) - 1]) - 1]))
            print('aaaaaa 2: ' + str(s[len(s) - 1]))
            visited.append(s[len(s) - 1][len(s[len(s) - 1]) - 1]);
            for a in self.vertices[s[len(s) - 1][len(s[len(s) - 1]) - 1]]:
                b = s[len(s) - 1].copy();
                b.append(a);
                print('aaaaa 3: ' + str(b));
                s.append(b);
                self.dfs_recursive(a, destination_vertex, b, visited);

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
    print('BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT');
    graph.dft(1)
    print('DFT RECURSIVE');
    graph.dft_recursive(1, [])

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
    print(graph.dfs_recursive(1, 6, [], []))
