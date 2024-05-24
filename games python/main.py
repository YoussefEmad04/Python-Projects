import tkinter as tk
from tkinter import messagebox
from collections import deque
import random
import string


class SudokuGenerator:
    def __init__(self, size):
        self.size = size
        self.box_size = int(self.size ** 0.5)

    def generate_board(self):
        board = [[0] * self.size for _ in range(self.size)]
        self.solve_board(board)
        self.remove_numbers(board)
        return board

    def is_valid_move(self, board, row, col, num):
        for i in range(self.size):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row = row - row % self.box_size
        start_col = col - col % self.box_size
        for i in range(self.box_size):
            for j in range(self.box_size):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve_board(self, board):
        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == 0:
                    for num in range(1, self.size + 1):
                        if self.is_valid_move(board, row, col, num):
                            board[row][col] = num
                            if self.solve_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def remove_numbers(self, board):
        num_to_remove = 40 if self.size == 9 else 4
        for _ in range(num_to_remove):
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            while board[row][col] == 0:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
            temp = board[row][col]
            board[row][col] = 0
            temp_board = [row[:] for row in board]
            if not self.has_unique_solution(temp_board):
                board[row][col] = temp

    def has_unique_solution(self, board):
        solver = SudokuSolverDFS(board)
        solver.solve()
        return solver.num_solutions == 1


class SudokuSolverDFS:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.box_size = int(self.size ** 0.5)
        self.num_solutions = 0

    def is_valid_move(self, row, col, num):
        for i in range(self.size):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row = row - row % self.box_size
        start_col = col - col % self.box_size
        for i in range(self.box_size):
            for j in range(self.box_size):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty_cell(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        return None, None

    def solve(self):
        row, col = self.find_empty_cell()
        if row is None and col is None:
            self.num_solutions += 1
            return True

        for num in range(1, self.size + 1):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def display_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))


class MazeGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [['#'] * cols for _ in range(rows)]
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == '#'

    def generate_maze(self, start_row, start_col, end_row, end_col):
        self.maze[start_row][start_col] = 'S'
        self.maze[end_row][end_col] = 'E'
        self.dfs(start_row, start_col)

    def dfs(self, row, col):
        random.shuffle(self.directions)
        for dr, dc in self.directions:
            new_row, new_col = row + 2 * dr, col + 2 * dc
            if self.is_valid_move(new_row, new_col):
                self.maze[row + dr][col + dc] = ' '
                self.maze[new_row][new_col] = ' '
                self.dfs(new_row, new_col)

    def display_maze(self):
        for row in self.maze:
            print(''.join(row))


class MazeSolverDFS:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.path = []

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and not self.visited[row][col] and self.maze[row][col] != '#'

    def dfs(self, row, col):
        if not self.is_valid_move(row, col):
            return False

        self.visited[row][col] = True
        self.path.append((row, col))

        if self.maze[row][col] == 'E':
            return True

        for dr, dc in self.directions:
            if self.dfs(row + dr, col + dc):
                return True

        self.path.pop()
        return False

    def solve(self, start_row, start_col):
        if not self.is_valid_move(start_row, start_col):
            print("Invalid starting position")
            return None

        if self.dfs(start_row, start_col):
            print("Path found:")
            for row, col in self.path:
                print(f"({row}, {col}) -> ", end="")
            print("End")
            return self.path
        else:
            print("No path found")
            return None


class WordLadderGame:
    def __init__(self, word_list):
        self.word_list = set(word_list)

    def generate_word_list(self, num_words, word_length):
        word_list = []
        current_word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        word_list.append(current_word)
        for _ in range(num_words - 1):
            next_word = self.generate_next_word(current_word)
            word_list.append(next_word)
            current_word = next_word
        return word_list

    def generate_next_word(self, word):
        word = list(word)
        index = random.randint(0, len(word) - 1)
        char = random.choice(string.ascii_lowercase)
        word[index] = char
        return ''.join(word)

    def get_neighbors(self, word):
        neighbors = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i + 1:]
                if new_word != word and new_word in self.word_list:
                    neighbors.append(new_word)
        return neighbors

    def find_shortest_path(self, start_word, end_word):
        if start_word not in self.word_list or end_word not in self.word_list:
            return None

        queue = deque([(start_word, [start_word])])
        visited = set([start_word])

        while queue:
            current_word, path = queue.popleft()
            if current_word == end_word:
                return path
            for neighbor in self.get_neighbors(current_word):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None


class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Game")
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_screen()

        title_label = tk.Label(self.root, text="Choose a Puzzle", font=("Helvetica", 16))
        title_label.pack(pady=10)

        sudoku_button = tk.Button(self.root, text="Sudoku", command=self.play_sudoku, width=20, height=2)
        sudoku_button.pack(pady=5)

        maze_button = tk.Button(self.root, text="Maze", command=self.play_maze, width=20, height=2)
        maze_button.pack(pady=5)

        word_ladder_button = tk.Button(self.root, text="Word Ladder", command=self.play_word_ladder, width=20, height=2)
        word_ladder_button.pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def play_sudoku(self):
        self.clear_screen()

        size = 9
        sudoku_generator = SudokuGenerator(size)
        sudoku_board = sudoku_generator.generate_board()

        solver = SudokuSolverDFS(sudoku_board)

        board_frame = tk.Frame(self.root)
        board_frame.pack()

        for i in range(size):
            for j in range(size):
                entry = tk.Entry(board_frame, width=3, font=("Helvetica", 16), justify='center')
                entry.grid(row=i, column=j)
                if sudoku_board[i][j] != 0:
                    entry.insert(0, sudoku_board[i][j])
                    entry.config(state='disabled')

        solve_button = tk.Button(self.root, text="Solve", command=lambda: self.solve_sudoku(solver, board_frame))
        solve_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.create_main_menu)
        back_button.pack(pady=5)

    def solve_sudoku(self, solver, board_frame):
        solver.solve()
        for i in range(solver.size):
            for j in range(solver.size):
                entry = board_frame.grid_slaves(row=i, column=j)[0]
                entry.config(state='normal')
                entry.delete(0, tk.END)
                entry.insert(0, solver.board[i][j])
                entry.config(state='disabled')

    def play_maze(self):
        self.clear_screen()

        rows, cols = 10, 20
        start_row, start_col = 0, 1
        end_row, end_col = rows - 1, cols - 2

        maze_generator = MazeGenerator(rows, cols)
        maze_generator.generate_maze(start_row, start_col, end_row, end_col)

        maze_frame = tk.Frame(self.root)
        maze_frame.pack()

        self.maze_labels = []
        for i in range(rows):
            row_labels = []
            for j in range(cols):
                label = tk.Label(maze_frame, text=maze_generator.maze[i][j], font=("Helvetica", 16), width=2, height=1)
                label.grid(row=i, column=j)
                row_labels.append(label)
            self.maze_labels.append(row_labels)

        solve_button = tk.Button(self.root, text="Solve", command=lambda: self.solve_maze(maze_generator.maze, start_row, start_col))
        solve_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.create_main_menu)
        back_button.pack(pady=5)

    def solve_maze(self, maze, start_row, start_col):
        maze_solver = MazeSolverDFS(maze)
        if maze_solver.solve(start_row, start_col):
            for (row, col) in maze_solver.path:
                self.maze_labels[row][col].config(bg='yellow')
        else:
            messagebox.showinfo("Maze Solver", "No path found")

    def play_word_ladder(self):
        self.clear_screen()

        num_words = 20
        word_length = 5
        word_list = WordLadderGame([]).generate_word_list(num_words, word_length)
        start_word = word_list[0]
        end_word = word_list[-1]

        word_ladder_game = WordLadderGame(word_list)
        shortest_path = word_ladder_game.find_shortest_path(start_word, end_word)

        if shortest_path:
            word_list_label = tk.Label(self.root, text=f"Word List: {word_list}", wraplength=400)
            word_list_label.pack(pady=5)

            start_label = tk.Label(self.root, text=f"Start Word: {start_word}")
            start_label.pack(pady=5)

            end_label = tk.Label(self.root, text=f"End Word: {end_word}")
            end_label.pack(pady=5)

            path_label = tk.Label(self.root, text=f"Shortest Path: {' -> '.join(shortest_path)}", wraplength=400)
            path_label.pack(pady=10)
        else:
            messagebox.showinfo("Word Ladder", "No transformation path exists between the given words.")

        back_button = tk.Button(self.root, text="Back", command=self.create_main_menu)
        back_button.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()
