# README BÀI NỘP NHÓM 10

**Nhóm / lớp / 4 thành viên:**
- **Nhóm:** Nhóm 10 
-  Lớp: UET.AI2014_1
- **Bốn thành viên:**
  1. Hoàng Trung Hiếu MSSV: 25022849
  2. Trần Nguyên Hiển Minh  MSSV: 25022950
  3. Lê Bảo Ngân  MSSV: 25022958
  4. Nguyễn Hoàng Anh  MSSV: 25022772

**Python / hệ điều hành / ngày chạy:** Python 3.14.4 / Linux (WSL2, Ubuntu 26.04 x86_64) / Ngày chạy: 25/10/2026.

---

## Tái chạy

Giải nén ZIP, mở thư mục chứa `run.py`. Mã chỉ dùng thư viện chuẩn Python

```text
python kiem_tra_moi_truong.py
python chay_mau.py
python -m unittest -v test_nhom
python chay_kiem_thu.py
python run.py --batch --tag bat_buoc
python run.py --data du_lieu_nhom.json --tag tu_tao
python run.py --case T0 --algo alphabeta --trace --tag trace_T0
```


**Kiểm tra bổ sung:**
- Chạy toàn bộ 35 unit test (test mẫu, ví dụ và test nhóm):
  ```text
  python -m unittest -v test_mau test_nhom_mau test_nhom
  ```
- Tái tạo vết khảo sát tham số $T_0(t)$ với $t = 11$ (đối chiếu cắt lá $L04$):
  ```text
  python run.py --t 11 --algo alphabeta --order LR --trace --tag t11
  ```

---

## Dữ liệu và kết quả

- **Tệp dữ liệu: du_lieu_nhom.json; seed/cách tạo:**
  - Tệp dữ liệu: `du_lieu_nhom.json`.
  - Seed: `2579`.
  - Cách tạo: chạy lệnh `python tao_du_lieu.py --seed 2579`.
  - Dữ liệu sinh ra:
    - Cây $N_1$: 16 lá, người chơi ở gốc là MAX, utility trong $[-20, 30]$.
    - Cây $N_2$: 8 lá, người chơi ở gốc là MIN, utility trong $[-20, 30]$.
  - Cùng seed 2579 luôn tái lập chính xác cùng dữ liệu. Thêm `--overwrite` nếu cần tạo lại.

- **JSON/CSV chung 24 cấu hình:**
  - Tệp lưu: `output/bat_buoc.json` và `output/bat_buoc.csv`.
  - Số lượng: đúng 24 cấu hình (khớp 24 dòng dữ liệu CSV và 24 phần tử JSON).
  - Thành phần gồm:
    - 12 cấu hình cơ bản: $T_0, T_1, T_2 \times \{\text{Minimax}, \text{Alpha--Beta}\} \times \{\text{LR}, \text{RL}\}$.
    - 10 cấu hình tham số: $T_0(t)$ với $t \in \{8, 10, 11, 12, 14\} \times 2$ thuật toán (thứ tự LR).
    - 2 cấu hình affine: biến đổi utility $u \mapsto 2u - 7$ trên $T_0$ (2 thuật toán, thứ tự LR).
  - Tất cả các dòng đều thỏa mãn bất biến `visited == expanded + leaves`.

- **JSON/CSV riêng 8 cấu hình:**
  - Tệp lưu: `output/tu_tao.json` và `output/tu_tao.csv`.
  - Số lượng: đúng 8 cấu hình (2 cây $N_1, N_2 \times 2$ thuật toán $\times 2$ thứ tự LR/RL).
  - Kết quả tại gốc:
    - Cây $N_1$ (16 lá, gốc MAX): `value = 13`, `action = A`.
    - Cây $N_2$ (8 lá, gốc MIN): `value = -13`, `action = B`.
  - Cả hai thuật toán (Minimax, Alpha–Beta) và cả hai thứ tự (LR, RL) đều cho cùng `value` và `action`.
  - Khớp 8 dòng dữ liệu CSV, tất cả đều thỏa mãn `visited == expanded + leaves`.

- **Trace và phép tính tay đối chiếu:**
  - `output/trace_T0.json`, `output/trace_T0.csv`: Vết chạy Alpha–Beta trên $T_0$ (LR). Kết quả `value = 10`, `action = A`, 22 visited, 12 expanded, 10 lá, 3 lần cắt tại các gốc $L10, L12, B2$, cờ cận `UPPER`.
  - `output/t11.json`, `output/t11.csv`: Alpha–Beta trên $T_0(t)$ với $t = 11$, LR có trace: `value = 11`, `action = A`, 9 lá đọc (cắt $L04$).
  - `TinhTay.pdf`: Bản PDF 14 trang tổng hợp bài tính tay độc lập các bài B1, B2, B3, B4 và cây riêng $N_2$.
  - Mọi kết quả tính tay độc lập đều khớp 100% với kết quả chạy từ mã nguồn.

- **Log kiểm thử thật và kết quả:**
  - Tệp log: `output/ket_qua_test.txt` sinh bởi lệnh `python chay_kiem_thu.py`.
  - Kết quả: **9 test nhóm PASS**, `OK`, `EXIT_CODE=0`.
  - Bộ kiểm thử riêng trong `test_nhom.py` gồm 9 test, phân bổ 2–2–3–2:
    - Hoàng Trung Hiếu: Test 1 (điểm âm, giữ nguyên input), Test 2 (utility 0, đường đi tối ưu).
    - Trần Nguyên Hiển Minh: Test 3 (bắt hòa giả trên $T_1$), Test 4 (cắt tỉa, cờ cận và số đếm trên $T_0$).
    - Lê Bảo Ngân: Test 5 (khảo sát tham số $t$), Test 6 (cây riêng $N_2$ gốc MIN), Test 7 (bắt lỗi số lá/kiểu dữ liệu).
    - Nguyễn Hoàng Anh: Test 8 (hòa thật theo LR/RL), Test 9 (bật/tắt trace và tích hợp JSON).
  - Có 4 test có tính tay độc lập ghi rõ trong docstring (Test 1, 2, 3, 4).
  - Chạy toàn bộ 3 bộ test (`test_mau`, `test_nhom_mau`, `test_nhom`): **35/35 test PASS**.

- **Tệp nhóm sửa/thêm, lý do:**
  - *Mã thuật toán và mô hình:* Giữ nguyên 100% mã nguồn gốc (`tree_model.py`, `search.py`, `data_cases.py`, `run.py`, `tao_du_lieu.py`, `chay_kiem_thu.py`, `dong_goi.py`, `test_mau.py`).
  - *Tệp nhóm thêm mới phục vụ bài nộp:*
    - `test_nhom.py`: 9 unit test kiểm tra các ca biên, cắt tỉa, tham số và tích hợp.
    - `du_lieu_nhom.json`: Dữ liệu 2 cây riêng $N_1, N_2$ sinh từ seed cố định 2579.
    - `output/`: Thư mục lưu kết quả chạy thực nghiệm (JSON, CSV, trace và log kiểm thử).
    - `TinhTay.pdf`: File PDF 14 trang tổng hợp bài tính tay chi tiết B1–B4 và $N_2$.
    - `BaoCao`: Báo cáo giữa kỳ.
    - `ThuyetTrinh`: Slide thuyết trình và bảo vệ giữa kỳ của nhóm.
    - `thu_loi.py`: Thử nghiệm cố tình tạo lỗi để chứng minh năng lực bắt lỗi của bộ test.
    - `README_NOP.md`, `DongGop.md`: Tài liệu nghiệm thu bài nộp và bảng đóng góp nhóm.

- **Lỗi chưa sửa / giới hạn:**
  - Không có lỗi thuật toán trong mã nguồn chính thức; cả 35 unit test đều PASS và 32 cấu hình thực nghiệm đều khớp kết quả đối chiếu. Thời gian chạy `elapsed_ms` biến thiên tùy theo máy.
  - Giới hạn thực nghiệm: cây trò chơi quy mô nhỏ ($\le 16$ lá, nhị phân, độ sâu tối đa 4); thứ tự duyệt nhánh cố định (LR/RL) chưa áp dụng sắp xếp nước di động.

---

Người đã giải nén chạy lại trên máy khác / ngày / kết quả:Hoàng Trung Hiếu / 25/10/2026 / chạy thành công, không bị lỗi

