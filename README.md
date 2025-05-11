# 🧩 Maze AI Game – Thuật toán tìm đường trong mê cung bằng AI

Dự án mô phỏng quá trình một nhân vật AI tự động giải một mê cung bằng các thuật toán trí tuệ nhân tạo khác nhau. Được xây dựng bằng thư viện `pygame`, trò chơi hỗ trợ nhiều thuật toán tìm đường và có giao diện sinh động, trực quan.

---

## 🎮 Cách chơi

1. **Chạy file `tempCodeRunnerFile.py`** để vào màn hình Start Game.
2. Nhấn **Start** để vào giao diện chính (`Main.py`) và bắt đầu chơi.
3. Trong giao diện chính:
   - Chọn thuật toán AI bằng **AI Menu**
   - Nhấn **Auto-Play** để AI thực hiện giải mê cung
   - Nhấn **Reset** để tạo mê cung mới
   - Nhấn **Exit** để thoát trò chơi

---

## 🧠 Thuật toán tích hợp

| Tên thuật toán          | Mô tả ngắn gọn                                            |
|-------------------------|------------------------------------------------------------|
| **BFS**                | Tìm kiếm theo chiều rộng (Breadth-First Search)            |
| **A\***                | Sử dụng heuristic (Manhattan distance) để tối ưu hóa        |
| **Simulated Annealing**| Tối ưu gần đúng, có yếu tố xác suất                         |
| **CSP Solver**         | Giải bài toán ràng buộc với forward checking                |
| **DQN**                | Mô phỏng học tăng cường bằng Deep Q-Network                |
| **No Observation**     | AI mù – không quan sát bản đồ, chỉ dò tìm ngẫu nhiên        |

---

## 📁 Cấu trúc thư mục (bên trong `src/`)

src/
├── AI.py # Logic di chuyển và trạng thái AI
├── Algorithms.py # Các thuật toán tìm đường
├── ControlPanel.py # Giao diện nút và xử lý sự kiện
├── Main.py # Giao diện chính của trò chơi
├── Maze.py # Tạo và hiển thị mê cung
├── Welcome.py # (Tuỳ chọn) màn hình mở đầu
├── tempCodeRunnerFile.py # Màn hình Start Game (nút Start → Main.py)
├── assets/
│ ├── Picture/ # Hình ảnh: nhân vật, phần thưởng, đích, tường
│ └── Music/ # Nhạc nền và hiệu ứng âm thanh
└── README.md # Tài liệu hướng dẫn này
