from room import Room
from player import Player
from world import World
from collections import deque;

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = set();

def bfs(starting_vertex):
        
    tv = deque();

    v = set();
        
    tv.append([(starting_vertex, None)]);

    while tv:
        p = tv.popleft();
        if p is None:
            continue;
        r = p[len(p) - 1][0]; 
        if r not in visited:
            return p;
        elif r not in v:
            v.add(r);
            for d in r.get_exits():
                connected_room = r.get_room_in_direction(d);
                b = p.copy();
                b.append((connected_room, d));
                tv.append(b);

opposites = {

    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'

}

def dfs(starting_vertex, starting_direction):
    tv = deque();

    v = set();
        
    tv.append([(starting_vertex, None)]);

    while tv:
        p = tv.pop();
        if p is None:
            continue;
        r = p[len(p) - 1][0]; 
        if len(r.get_exits()) == 1:
            return p;
        elif r not in v:
            v.add(r);
            for d in r.get_exits():
                connected_room = r.get_room_in_direction(d);
                if r == starting_vertex and d == opposites[starting_direction]:
                    continue;
                b = p.copy();
                b.append((connected_room, d));
                tv.append(b);

visited.add(world.starting_room);

def move(path):
    for room, direction in path:
        visited.add(room);
        if direction is None:
            continue;
        else:
            player.travel(direction);
            traversal_path.append(direction);

while len(world.rooms) != len(visited):
    path = bfs(player.current_room);
    move(path);
    path = dfs(player.current_room, path[-1][1]);
    move(path);
    
    print(path);

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
