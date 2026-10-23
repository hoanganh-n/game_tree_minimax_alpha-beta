# PHÂN CÔNG NHIỆM VỤ CHI TIẾT — NHÓM 10
**Dự án:** Cây trò chơi: Minimax và Alpha–Beta (4 sinh viên · 10 ngày · bảo vệ 15–20 phút)  
**Môn học:** Biểu diễn tri thức và tìm kiếm nâng cao — IAI–UET–VNU  
**Quy chuẩn chấm điểm:** 85 điểm sản phẩm chung + 15 điểm bảo vệ cá nhân

---

## 1. BẢNG TỔNG QUAN PHÂN CÔNG & TRÁCH NHIỆM

| Thành viên | Mảng chủ trì | Bài tính tay / Khảo sát | Test phụ trách (`test_nhom.py`) | Kiểm tra chéo |
|---|---|---|---|---|
| **Người 1** | Mô hình cây & Thuật toán Minimax | Bài B1 ($T_0$ Minimax, 16 lá) | • **Test 1:** Điểm âm + không sửa input<br>• **Test 2:** Utility 0 + đường đi tối ưu $PV$ | Đọc và giải thích vết Alpha–Beta (`output/trace_T0.json`) |
| **Người 2** | Thuật toán Alpha–Beta & Cắt tỉa | Bài B2 ($T_0$ Alpha–Beta)<br>Bài B4 (Phân tích cây $T_1$) | • **Test 3:** Cây $T_1$ (hòa giả & action)<br>• **Test 4:** Cắt tỉa, `bound` & đẳng thức đếm | Đối chiếu bảng Minimax của Người 1 với kết quả `returns` |
| **Người 3** | Dữ liệu riêng & Khảo sát tham số | Bài B3 (Khảo sát $T(t)$, affine)<br>Tính tay cây riêng $N_2$ (8 lá, gốc MIN) | • **Test 5:** Tham số $T_0(t)$ tại $t=10,11,14$<br>• **Test 6:** Cây riêng $N_2$ (gốc MIN)<br>• **Test 7:** Bắt lỗi số lá / sai kiểu dữ liệu | Kiểm tra các mốc tham số $t$ trong JSON thực nghiệm |
| **Người 4 (Nhóm trưởng)** | Thực nghiệm hệ thống, Tích hợp & Báo cáo | Tính nhẩm kịch bản test tích hợp | • **Test 8:** Hòa thật theo thứ tự LR/RL<br>• **Test 9:** Bật/tắt trace & tích hợp JSON | Kiểm tra toàn bộ file JSON, CSV, 9 unit test và đóng gói |

Bộ test hiện có **9 test** (phân bổ 2–2–3–2), đáp ứng yêu cầu ít nhất 8 test và mỗi người ít nhất 2 test. Số test bên dưới khớp tiền tố `test_01` đến `test_09` trong mã nguồn.

---

## 2. GÓI CÔNG VIỆC CHI TIẾT TỪNG THÀNH VIÊN

### 👤 NGƯỜI 1: MÔ HÌNH CÂY, MINIMAX & TÍNH TAY B1
* **Mã nguồn cần nắm vững:**
  * `tree_model.py`: Cách dựng cây nhị phân luân phiên MAX/MIN từ danh sách lá phẳng (`make_tree`), duyệt cây (`walk`), kiểm tra tính hợp lệ (`validate_tree`).
  * `search.py`: Khối xử lý đệ quy thuật toán Minimax.
* **Bài tính tay nộp bài (Bài B1):**
  * Chạy thuật toán **Minimax** trên cây $T_0$ gồm 16 lá: `[9, 12, 11, 10, 8, 15, 14, 13, 4, 5, 3, 6, 100, 101, 90, 95]`, thứ tự từ Trái sang Phải (LR).
* **2 Unit Test phụ trách viết vào `test_nhom.py`:**
  * **Test 1 (Tính tay độc lập 1):** Cây toàn điểm âm, kiểm tra mảng lá đầu vào không bị hàm thay đổi.
  * **Test 2:** Xử lý đúng lá có điểm bằng 0 (utility 0 là lá hợp lệ, khác `None`), kiểm tra đường đi tối ưu của Minimax.
* **Phần viết báo cáo:** Soạn nháp Mục 1 (Bài toán) và Mục 2 (Công thức truy hồi Minimax, mã giả).
* **Bàn giao cho Nhóm trưởng:** File viết tay/PDF bài B1; mã nguồn 2 hàm test; nội dung nháp Mục 1 & 2.

---

### 👤 NGƯỜI 2: ALPHA–BETA, TÍNH TAY B2 & PHÂN TÍCH CÂY T1 (B4)
* **Mã nguồn cần nắm vững:**
  * `search.py`: Khối Alpha–Beta, cơ chế truyền cửa sổ $[\alpha, \beta]$, điều kiện cắt $\alpha \ge \beta$, và gán cờ `bound` (`UPPER`, `LOWER`, `EXACT`).
* **Bài tính tay nộp bài (Bài B2):**
  * Chạy thuật toán **Alpha–Beta** trên cây $T_0$ (16 lá, LR). Khởi tạo gốc $[\alpha, \beta] = [-\infty, +\infty]$.
  * Ghi lại chi tiết sự thay đổi của $\alpha, \beta$ qua từng nút và chỉ ra đúng **3 vị trí cắt tỉa**
* **Phân tích hiện tượng cây $T_1$ (Bài B4):**
* **2 Unit Test phụ trách viết vào `test_nhom.py`:**
  * **Test 3 (Tính tay độc lập 2):** Cây $T_1$ kiểm tra đồng thời cả `value` lẫn `action` để bắt lỗi hòa giả giữa các cận.
  * **Test 4:** Cắt tỉa, hướng cận `bound = UPPER` và kiểm tra đẳng thức số đếm (`visited == expanded + leaves`).
* **Phần viết báo cáo:** Soạn nháp Mục 3 (Quy tắc không được nhầm) và Mục 6 (Phân tích chi tiết hiện tượng trên cây $T_1$).
* **Bàn giao cho Nhóm trưởng:** File viết tay/PDF bài B2 và B4; mã nguồn 2 hàm test; nội dung nháp Mục 3 & 6.

---

### 👤 NGƯỜI 3: DỮ LIỆU RIÊNG (N1/N2), KHẢO SÁT THAM SỐ T(t) & TÍNH TAY N2
* **Mã nguồn cần nắm vững:**
  * `tao_du_lieu.py`: Cơ chế sinh dữ liệu ngẫu nhiên với seed cố định.
  * `data_cases.py`: Cấu trúc cây tham số $T(t)$ và biến đổi affine.
* **Sinh dữ liệu riêng của nhóm:**
  * Chạy `python tao_du_lieu.py --seed <seed_nhom>` để sinh file `du_lieu_nhom.json` chứa (Hoàng Anh làm rồi nhé): 
    * $N_1$: 16 lá, người chơi ở gốc là MAX.
    * $N_2$: 8 lá, người chơi ở gốc là MIN.
* **Bài tính tay nộp bài:**
  * *Tính tay độc lập trên cây riêng $N_2$ (8 lá, gốc MIN):* Vẽ cây 8 lá từ dữ liệu sinh ra, tính tay từng bước theo cả Minimax và Alpha–Beta (chú ý gốc là MIN chọn giá trị nhỏ nhất). Xác định giá trị gốc, action và các vết cắt tỉa.
  * *Khảo sát tham số $T(t)$ (Bài B3):* Khảo sát cây $T_0$ khi thay lá đầu tiên $L_{01} = t \in \{8, 10, 11, 12, 14\}$. Tìm công thức $V(R)$ theo $t$, ngưỡng đổi action từ $A$ sang $B$, ngưỡng cắt bỏ lá $L_{04}$. Khảo sát biến đổi affine $u \mapsto 2u - 7$.
* **3 Unit Test phụ trách trong `test_nhom.py`:**
  * **Test 5 — `test_05_t0_parameter`:** Với $t=10,11,14$, kiểm tra cả Minimax và Alpha–Beta trả lần lượt $(10,A)$, $(11,A)$, $(12,A)$; số lá Alpha–Beta đọc lần lượt là 10, 9, 9.
  * **Test 6 — `test_06_n2_root_min`:** Kiểm tra N2 có gốc MIN; cả hai thuật toán với LR/RL đều trả `value = -13`, `action = B`.
  * **Test 7 — `test_07_invalid_leaf_data`:** Kiểm tra `ValueError` với 3 lá, utility chuỗi hoặc bool. Hiện test chưa kiểm tra utility số thực.
* **Phần viết báo cáo:** Soạn nháp Mục 5 (Khảo sát tham số) và Mục 7 (Bảng kết quả 2 cây riêng $N_1, N_2$).
* **Bàn giao cho Nhóm trưởng:** File `du_lieu_nhom.json` và số seed; file viết tay/PDF bài tính tay $N_2$ và $T(t)$; mã nguồn 3 hàm test; nội dung nháp Mục 5 & 7.

---

### 👤 NGƯỜI 4 (NHÓM TRƯỞNG): THỰC NGHIỆM, TÍCH HỢP & BÁO CÁO TỔNG HỢP
* **Thực nghiệm hệ thống (CLI Execution):**
  * Chạy 24 cấu hình bắt buộc: `python run.py --batch --tag bat_buoc` (xuất ra `output/bat_buoc.json` và `.csv`).
  * Chạy 8 cấu hình riêng: `python run.py --data du_lieu_nhom.json --tag tu_tao` (xuất ra `output/tu_tao.json` và `.csv`).
  * Xuất vết trace phục vụ demo: `python run.py --case T0 --algo alphabeta --trace --tag trace_T0`.
* **2 Unit Test phụ trách viết vào `test_nhom.py`:**
  * **Test 8 — `test_08_hoa_that_theo_LR_RL`:** Với lá `[2,5,2,7]`, cả hai thuật toán trả value 2; LR chọn A, RL chọn B khi hòa thật.
  * **Test 9 — `test_09_trace_bat_tat_va_tich_hop_json`:** Nạp N1 từ `du_lieu_nhom.json`; bật/tắt trace Alpha–Beta giữ nguyên value, action và các số đếm được kiểm tra; trace tắt rỗng, trace bật có sự kiện; kiểm tra `visited == expanded + leaves`.
* **Tích hợp kiểm thử & Chất lượng:**
  * Tích hợp 9 test vào `test_nhom.py`: Người 1 phụ trách 1–2, Người 2 phụ trách 3–4, Người 3 phụ trách 5–7, Người 4 phụ trách 8–9. Mỗi người có ít nhất 2 test.
  * Chạy kiểm thử chính thức để xuất file log nộp bài: `python3 chay_kiem_thu.py` (sinh ra `output/ket_qua_test.txt`).
* **Hoàn thiện bộ hồ sơ nộp bài:**
  * Ghép bài tính tay của Người 1, 2, 3 thành file duy nhất: `TinhTay.pdf` 
  * Soạn thảo và xuất báo cáo chính: `BaoCao.pdf`.
  * Soạn slide thuyết trình: `ThuyetTrinh.pptx` (6–8 slide theo `DanY_BaoVe.md`).
  * Điền đầy đủ thông tin vào `README_NOP.md` và `DongGop.md`.
* **Đóng gói nghiệm thu:**
  * Chạy kiểm tra và đóng gói: `python dong_goi.py` $\to$ sinh file `Nhom10_CayTroChoi_GiuaKy.zip`.
  * Phối hợp cùng thành viên khác giải nén chạy thử nghiệm trên máy sạch.

---
Nếu có viết 1 số phần trong báo cáo, thì các bạn viết vào file .tex cho mình nhé, mình sẽ tổng hợp lại và hoàn thiện sau.
