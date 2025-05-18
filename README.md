# 🤖 ĐỒ ÁN CUỐI KỲ – TRÍ TUỆ NHÂN TẠO  
## 📍 TÊN ĐỀ TÀI: ỨNG DỤNG AI GIẢI BÀI TOÁN MÊ CUNG BẰNG NHIỀU THUẬT TOÁN TÌM KIẾM

---

## 👨‍🎓 THÔNG TIN NHÓM THỰC HIỆN

- **Họ và tên**: Phạm Ngọc Mạnh - 23110262
                 Trương Thanh Thành - 23133069
                 Nguyễn Tấn Tài - 23133066  
- **Giảng viên hướng dẫn**: Ths. Phan Thị Huyền Trang
- **Trường**: ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP. HỒ CHÍ MINH 

---

## 🔍 MỤC TIÊU DỰ ÁN

Dự án được xây dựng nhằm mô phỏng và trực quan hóa quá trình **giải bài toán tìm đường trong mê cung** bằng các **thuật toán trí tuệ nhân tạo**. Qua đó giúp sinh viên:

- Hiểu bản chất các thuật toán tìm kiếm cổ điển và hiện đại
- So sánh hiệu quả của từng thuật toán thông qua số bước và hành vi
- Biết cách triển khai ứng dụng AI đơn giản bằng thư viện `pygame` trong Python

---

## 🎮 CHỨC NĂNG CHÍNH

- Tạo **mê cung ngẫu nhiên** với kích thước 35x25
- Chọn và chạy **một trong sáu thuật toán tìm đường**
- Theo dõi **đường đi của AI**, hiển thị trên mê cung
- Giao diện trực quan với **âm thanh, hình ảnh, hiệu ứng**
- Thống kê và **lưu lại số bước di chuyển** của từng thuật toán vào file `.txt`
- Giao diện điều khiển bao gồm: bắt đầu, chọn thuật toán, reset, xóa đường đi

---

## 🧭 MÔ TẢ BẢN ĐỒ MÊ CUNG (MAP)

- Mỗi mê cung được chia thành lưới 35x25 ô
- Các ô được mã hóa như sau:
  - **Start (bắt đầu)**: ô màu xanh lá cây
  - **Goal (đích đến)**: ô màu đỏ
  - **Tường (chướng ngại)**: màu đen hoặc ảnh `hangrao.jpg`
  - **Đường đi AI đã đi qua**: màu tím
  - **Phần thưởng (reward)**: ảnh `selectbackground.jpg`
  - **Vật cản (obstacle)**: ảnh `iconbom.png`

📷 *Hình ảnh bản đồ mê cung mẫu:*  
![image](https://github.com/user-attachments/assets/ad7d8719-a2a1-432d-8523-dbf9afaa7c01)


---

## 📊 THỐNG KÊ SỐ BƯỚC TỪ CÁC THUẬT TOÁN

| Thuật toán                  | Số bước ví dụ |
|-----------------------------|----------------|
| Simulated Annealing (SA)    | 27             |
| No Observation (Sensorless) | 91             |
| CSP Solver                  | 34             |
| Deep Q-Network (DQN)        | 42             |
| A* Search                   | 21             |
| Breadth-First Search (BFS)  | 28             |

📷 *Hình minh họa biểu đồ thống kê:*  
![image](https://github.com/user-attachments/assets/50f5af06-242e-4d8a-9859-e16491615459)

---

## 🧠 GIẢI THÍCH CÁC THUẬT TOÁN (KÈM HÌNH MINH HOẠ ĐƯỜNG ĐI)

---

### 🧪 1. Simulated Annealing (SA)

**Mô tả:**  
SA là một thuật toán tối ưu hoá dựa trên cơ chế mô phỏng quá trình tôi luyện kim loại. Nó cho phép chọn các hướng đi kém tối ưu ở giai đoạn đầu (nhiệt độ cao), và dần "lạnh lại", chỉ giữ các hướng tốt hơn khi nhiệt độ giảm.

**Tính chất:**  
- Khả năng thoát local optimum
- Đường đi có thể ban đầu không hợp lý nhưng dần hội tụ

📷 *Hình minh hoạ đường đi của SA:*  
![image](https://github.com/user-attachments/assets/10e65788-4cff-44c5-855f-aa45c4eeb51e)

---

### 🔍 2. No Observation Search (Sensorless)

**Mô tả:**  
Không có cảm biến để biết đích ở đâu, thuật toán sẽ di chuyển ngẫu nhiên trong không gian cho đến khi tìm thấy goal. Đây là tình huống khó trong AI, khi tác nhân không có thông tin về trạng thái hiện tại.

**Tính chất:**  
- Tốn thời gian
- Không tối ưu
- Phù hợp với môi trường không quan sát được

📷 *Hình minh hoạ đường đi của NO_OBS:*  
![image](https://github.com/user-attachments/assets/6243ac10-d3d6-4311-88d5-c6e55d9dcec0)

lý do thuật toán không chạy được:
+ Goal không được gán 2 trong grid, nên thuật toán không bao giờ nhận ra đích.

+ Dùng visited chặn lối quay lại khiến agent dễ bị kẹt, không tìm được đường.
---

### 🧩 3. CSP Solver (Constraint Satisfaction)

**Mô tả:**  
Thuật toán này coi việc tìm đường như bài toán ràng buộc. Kết hợp giữa **Backtracking** và **Forward Checking** để đảm bảo mỗi bước đi không gây mâu thuẫn hoặc đưa đến ngõ cụt.

**Tính chất:**  
- Tránh đường sai từ đầu
- Có thể hơi chậm, nhưng chính xác và logic
- Hiệu quả trong mê cung chặt

📷 *Hình minh hoạ đường đi của CSP:*  
![image](https://github.com/user-attachments/assets/28489c02-bc5d-487e-a729-631277d11bfd)

---

### 🧠 4. Deep Q-Network (DQN)

**Mô tả:**  
Thuật toán học tăng cường, mô phỏng cách AI học từ kinh nghiệm quá khứ để tối ưu hành động hiện tại. Trong đồ án, DQN được đơn giản hóa để hoạt động không cần mô hình mạng.

**Tính chất:**  
- Mang tính học hỏi – cải thiện theo thời gian
- Có thể sai sót trong giai đoạn đầu
- Đường đi linh hoạt, không cứng nhắc

📷 *Hình minh hoạ đường đi của DQN:*  
![image](https://github.com/user-attachments/assets/c294cee2-39b3-40f4-9f0f-bab17b48304e)

---

### 🧭 5. A* Search

**Mô tả:**  
Thuật toán tìm kiếm có định hướng. Nó tính tổng chi phí từ start đến vị trí hiện tại và ước lượng khoảng cách còn lại đến goal.

**Tính chất:**  
- Tối ưu đường đi nếu hàm `heuristic` tốt
- Nhanh, hiệu quả
- Dễ triển khai

📷 *Hình minh hoạ đường đi của A*:*  
![image](https://github.com/user-attachments/assets/1fb424eb-0d42-4aa2-a788-2698fb87c4e9)


---

### 🌐 6. Breadth-First Search (BFS)

**Mô tả:**  
BFS tìm kiếm theo lớp, mở rộng tất cả các trạng thái kế tiếp trước khi đi sâu hơn. Do đó nó **luôn tìm được đường đi ngắn nhất**, nếu có.

**Tính chất:**  
- Đảm bảo tìm đúng
- Không heuristic
- Có thể tốn bộ nhớ khi mê cung rộng

📷 *Hình minh hoạ đường đi của BFS:*  
![image](https://github.com/user-attachments/assets/ccf1dcd0-2022-48cd-ae7b-140d99c7ab1c)

ở map này đường BFS giống 
---

## 📂 CẤU TRÚC THƯ MỤC DỰ ÁN

```bash
DO_AN_CUOI_KY_AI/
├── src/
│   ├── Maze.py
│   ├── Main.py
│   ├── Algorithms.py
│   ├── AI.py
│   ├── ControlPanel.py
│   ├── Music/
│   └── Picture/
├── images/
│   ├── maze_map.png
│   ├── statistics_chart.png
│   ├── sa_path.png
│   ├── no_obs_path.png
│   ├── csp_path.png
│   ├── dqn_path.png
│   ├── a_star_path.png
│   └── bfs_path.png
├── algorithm_statistics.txt
└── README.md
