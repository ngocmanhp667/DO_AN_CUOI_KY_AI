# Algorithms.py
import pygame
import random
import math
from Maze import Maze
from pygame.locals import *
from queue import PriorityQueue
from queue import PriorityQueue
from collections import deque


def play_next_music():
    # Hàm để phát nhạc tiếp theo
    pygame.mixer.music.load("D:/GameTTNT-20250506T175324Z-001/GameTTNT/src/Music/nhac.mp3")
    pygame.mixer.music.play()

# Thuật toán imulated_annealing
def simulated_annealing(maze):
    start = (maze.start_x, maze.start_y)
    goal = (maze.end_x, maze.end_y)

    max_attempts = 5
    for attempt in range(max_attempts):
        current = start
        path = [current]
        visited = set([current])

        temperature = 100.0
        cooling_rate = 0.99

        def energy(pos):
            return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

        for _ in range(1000):  # Giới hạn số bước
            if current == goal:
                print(f"SA success (attempt {attempt+1}), steps: {len(path)}")
                return path

            neighbors = maze.get_neighbors(current[0], current[1])
            neighbors = [n for n in neighbors if n not in visited]
            if not neighbors:
                break

            neighbors.sort(key=energy)  # Ưu tiên gần goal
            if random.random() < 0.2:
                next_node = random.choice(neighbors)
            else:
                next_node = neighbors[0]

            delta_e = energy(current) - energy(next_node)

            if delta_e > 0 or math.exp(delta_e / temperature) > random.random():
                current = next_node
                visited.add(current)
                path.append(current)

            temperature *= cooling_rate

        print(f"SA attempt {attempt+1} failed")

    print("SA: Failed to find a path after max attempts.")
    return []

def searching_with_no_observation(maze):
    start = (maze.start_x, maze.start_y)
    goal = (maze.end_x, maze.end_y)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # phải, xuống, trái, lên

    queue = deque()
    visited = set()
    queue.append((start, [start]))
    visited.add(start)

    while queue:
        current_pos, path = queue.popleft()

        if current_pos == goal:
            return path

        # Bản chất "mù": không quan sát, chỉ thử các hướng
        random.shuffle(directions)  # để không đi cố định

        for dx, dy in directions:
            nx, ny = current_pos[0] + dx, current_pos[1] + dy
            next_pos = (nx, ny)

            # Không dùng get_neighbors, chỉ kiểm tra tường khi "đã bước tới"
            if 0 <= nx < maze.width and 0 <= ny < maze.height:
                if maze.grid[ny][nx] == 0 and next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))

    return []  # Không tìm được đường

# Thuật toán solve_with_csp
def solve_with_csp(maze):
    start = (maze.start_x, maze.start_y)
    goal = (maze.end_x, maze.end_y)
    path = []
    visited = set()

    def is_valid(pos):
        x, y = pos
        return (
            0 <= x < maze.width and
            0 <= y < maze.height and
            maze.grid[y][x] == 0 and
            pos not in visited
        )

    def forward_check(pos):
        # Nếu không còn bước đi nào hợp lệ từ đây → return False
        neighbors = maze.get_neighbors(pos[0], pos[1])
        return any(is_valid(n) for n in neighbors)

    def backtrack(current):
        if current == goal:
            path.append(current)
            return True

        visited.add(current)
        neighbors = maze.get_neighbors(current[0], current[1])

        for neighbor in neighbors:
            if is_valid(neighbor) and forward_check(neighbor):
                if backtrack(neighbor):
                    path.append(current)
                    return True

        visited.remove(current)
        return False

    if backtrack(start):
        path.reverse()
        return path
    else:
        return []

# Thuật toán run_dqn_agent
def run_dqn_agent(maze):
    start = (maze.start_x, maze.start_y)
    goal = (maze.end_x, maze.end_y)
    current = start
    path = [current]
    visited = set([current])

    def q_value(pos):
        return - (abs(pos[0] - goal[0]) + abs(pos[1] - goal[1]))

    for step in range(2000):  # Tối đa 1000 bước
        if current == goal:
            print(f"DQN: Reached goal in {len(path)} steps.")
            return path

        neighbors = maze.get_neighbors(current[0], current[1])
        neighbors = [n for n in neighbors if n not in visited]

        if not neighbors:
            print(f"DQN: Stuck at step {step}, no unvisited neighbors.")
            break

        if random.random() < 0.2:
            next_node = random.choice(neighbors)
        else:
            next_node = max(neighbors, key=q_value)

        current = next_node
        path.append(current)
        visited.add(current)

    print("DQN: Failed to reach goal.")
    return []
def astar(maze):
    start = (maze.start_x, maze.start_y)
    goal = (maze.end_x, maze.end_y)

    frontier = PriorityQueue()
    frontier.put((0, start))

    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for neighbor in maze.get_neighbors(current[0], current[1]):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

    # Truy ngược đường đi
    path = []
    current = goal
    while current != start:
        if current not in came_from:
            print("A*: No path found")
            return []
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    print(f"A*: Path found with {len(path)} steps.")
    return path
def bfs(maze):
    start = (maze.start_x, maze.start_y)
    goal = (maze.end_x, maze.end_y)

    queue = deque()
    queue.append((start, [start]))  # (vị trí hiện tại, đường đi đến đó)

    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            print(f"BFS: Path found with {len(path)} steps.")
            return path

        for neighbor in maze.get_neighbors(current[0], current[1]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("BFS: No path found.")
    return []