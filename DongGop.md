# ĐÓNG GÓP NHÓM 10 — ĐÚNG 4 THÀNH VIÊN
Repository github dự án: https://github.com/hoanganh-n/game_tree_minimax_alpha-beta.git


| Thành viên / MSSV | Mảng chủ trì | Hai kiểm thử | Kiểm tra chéo | Tệp/commit/minh chứng |
|---|---|---|---|---|
| **1. Hoàng Trung Hiếu / 25022849** | Mô hình cây, Minimax, bài B1 | Test 1, Test 2 | Vết Alpha–Beta trên T0 | `TinhTay.pdf` (B1). `BaoCao.pdf` (Mục 1, 2). Commit `f3d4ce2`, `107ea1d`. |
| **2. Trần Nguyên Hiển Minh / 25022950** | Alpha–Beta, cắt tỉa, bài B2, B4 | Test 3, Test 4 | Bảng Minimax với returns | `TinhTay.pdf` (B2, B4). `BaoCao.pdf` (Mục 3, 6). Commit `b91952f`, `fbabdf1`. |
| **3. Lê Bảo Ngân / 25022958** | Dữ liệu N1/N2, tham số, bài B3 | Test 5, Test 6 (thêm Test 7) | Tái tạo kết quả trong JSON | `TinhTay.pdf` (B3, N2). `BaoCao.pdf` (Mục 5, 7). Commit `46ca564`, `04b8f01`. |
| **4. Nguyễn Hoàng Anh / 25022772 — Nhóm trưởng** | Thực nghiệm 24+8, tích hợp, đóng gói | Test 8, Test 9 | Kiểm tra JSON/CSV, test, lệnh chạy | `BaoCao.pdf` (tổng hợp). `TinhTay.pdf`. `output/`. Commit `4438c73`, `b7a6b96`. |

Ngân phụ trách thêm **Test 7 — `test_07_invalid_leaf_data`**: kiểm tra từ chối dữ liệu có 3 lá, utility kiểu chuỗi hoặc bool. Tổng cộng **9 test**, phân bổ **2–2–3–2**, đáp ứng yêu cầu ít nhất 8 test và mỗi người ít nhất 2 test. Các test 1–4 có ghi bước tính tay độc lập trong docstring. Log hiện có tại `output/ket_qua_test.txt` ghi **9 test PASS**, `OK`, `EXIT_CODE=0`.

## Mốc ngày 5: Đối chiếu tính tay, code và kiểm thử

- **Công việc đã hoàn thành (tính đến hết ngày 20/10/2026):**
  - Cả 4 thành viên hoàn thành nghiên cứu đề bài, hiểu rõ mô hình cây nhị phân luân phiên MAX/MIN trong `tree_model.py` và quy tắc thuật toán Minimax, Alpha–Beta trong `search.py`.
  - Hoàn thành bảng phân công nhiệm vụ chi tiết giữa 4 thành viên (commit `bb5eb18`, `4615fd3`), chạy kiểm tra môi trường và chạy thử bộ test mẫu `test_mau.py`.
  - Hoàng Trung Hiếu hoàn thành tính tay độc lập bài B1 trên cây $T_0$, số hóa thành tệp `tinh_tay/Tính-Tay-B1.pdf` và đẩy lên repo (commit `095a0f5`, `61cc69c`).
  - Cả nhóm giải nháp tay các trường hợp $T_0, T_1$, phân tích cửa sổ cắt tỉa $\alpha \ge \beta$ và thảo luận hiện tượng hòa giả trên cây $T_1$.
  - Lê Bảo Ngân bắt đầu triển khai các ca kiểm thử đầu tiên về khảo sát tham số $T_0(t)$ và cắt tỉa $T_1$ trên nhánh `feature/ngan` (commit `4e705f1`).
  - Nguyễn Hoàng Anh chuẩn bị khung tệp `test_nhom.py` và chạy thử nghiệm batch ban đầu (commit `5777bc7`).
- **Công việc chưa xong:**
  - Trần Nguyên Hiển Minh và Hoàng Trung Hiếu đang hoàn thiện các ca kiểm thử riêng trên nhánh cá nhân (sẽ đẩy lên vào ngày 21–22/10).
  - Trần Nguyên Hiển Minh đang hoàn thiện bài tính tay B2 và B4 (sẽ nộp vào ngày 23/10).
  - Lê Bảo Ngân tiếp tục tính tay khảo sát bài B3 và dữ liệu cây riêng $N_2$ gốc MIN.
- **Tệp minh chứng mốc ngày 5 (khớp lịch sử commit đến ngày 20/10/2026):**
  - Bài tính tay B1: `tinh_tay/Tính-Tay-B1.pdf` (commit `095a0f5`, `61cc69c`).
  - Bảng phân công nhóm: `DongGop.md` (commit `48c49b8`, `bb5eb18`, `4615fd3`).
  - Khung kiểm thử và các test đầu tiên của Ngân: `test_nhom.py` (commit `5777bc7`, `4e705f1`).

## Mốc ngày 10: Tích hợp và nghiệm thu bài nộp

- **Công việc đã hoàn thành (tiến trình từ Ngày 6 đến Ngày 10):**
  - *Ngày 21/10 (Ngày 6):* Hiển Minh hoàn thành 2 unit test (Test 3 bắt hòa giả $T_1$, Test 4 cờ cận $T_0$ — commit `f4a722d`).
  - *Ngày 22/10 (Ngày 7):* Trung Hiếu hoàn thành 2 unit test (Test 1 điểm âm, Test 2 utility 0 — commit `260255d`); bổ sung mục 1 và mục 2 vào báo cáo (commit `f3d4ce2`).
  - *Ngày 23/10 (Ngày 8):* Hiển Minh nộp bài tính tay B2, B4 và phần báo cáo (`tinh_tay/tinh_tay_B2_B4.pdf`, commit `b91952f`); Bảo Ngân bổ sung Test 6, Test 7 (commit `46ca564`), nộp bài tính tay B3 và $N_2$ (`TinhTayB3.pdf`, `TinhTayN2.pdf` — commit `1c9507a`).
  - *Ngày 24/10 (Ngày 9):* Hoàn thiện báo cáo `BaoCao.pdf`, slide thuyết trình `ThuyetTrinh.pptx`, rà soát bảng test và tài liệu nộp `README_NOP.md`, `DongGop.md`.
  - *Ngày 25/10 (Ngày 10):* Hoàng Trung Hiếu thực hiện tái chạy độc lập toàn bộ chuỗi lệnh trên máy tính sạch (WSL2 Ubuntu 26.04, Python 3.14.4), xác nhận đạt 35/35 test PASS, mọi kết quả JSON/CSV đều khớp 100%, sẵn sàng nộp bài và bảo vệ.
- **Kết quả tái chạy độc lập (nghiệm thu):**
  - Tệp log: `output/ket_qua_test.txt` ghi nhận 9/9 test nhóm PASS (`OK`, `EXIT_CODE=0`).
  - Toàn bộ 35 unit test (`test_mau`, `test_nhom_mau`, `test_nhom`) đều PASS không có lỗi.
  - 24 cấu hình bắt buộc (`output/bat_buoc.json`, `.csv`) và 8 cấu hình riêng (`output/tu_tao.json`, `.csv`) thỏa mãn bất biến `visited == expanded + leaves`.
- **Lỗi còn tồn tại và giới hạn:**
  - Không có lỗi logic thuật toán trong mã nguồn chính thức; không có lỗi thực thi.
  - Giới hạn: Cây nhị phân cố định quy mô $\le 16$ lá, chiều sâu tối đa 4; thứ tự duyệt nhánh tĩnh (LR/RL) chưa áp dụng sắp xếp nước đi động.

## Xác nhận của bốn thành viên

Cả bốn thành viên đã đọc, đối chiếu chéo kết quả, xác nhận bảng phân công đóng góp đúng với thực tế làm việc của nhóm và sẵn sàng bảo vệ trước hội đồng:

1. **Hoàng Trung Hiếu (MSSV: 25022849):** Đã hoàn thành mảng mô hình cây, Minimax, bài tính tay B1, Test 1–2; đã trực tiếp tái chạy nghiệm thu độc lập trên máy sạch; cam kết nắm vững nội dung và sẵn sàng bảo vệ. *(Đã ký xác nhận)*
2. **Trần Nguyên Hiển Minh (MSSV: 25022950):** Đã hoàn thành mảng Alpha–Beta, bài tính tay B2, B4 (hòa giả), Test 3–4, kiểm tra chéo Minimax; cam kết nắm vững nội dung và sẵn sàng bảo vệ. *(Đã ký xác nhận)*
3. **Lê Bảo Ngân (MSSV: 25022958):** Đã hoàn thành mảng dữ liệu riêng N1/N2, bài tính tay B3, N2 gốc MIN, Test 5–7; cam kết nắm vững nội dung và sẵn sàng bảo vệ. *(Đã ký xác nhận)*
4. **Nguyễn Hoàng Anh (MSSV: 25022772 — Nhóm trưởng):** Đã điều phối tiến độ, thực hiện 24+8 cấu hình thực nghiệm, tích hợp hồ sơ nộp, Test 8–9, đóng gói ZIP; cam kết chịu trách nhiệm tổng thể và sẵn sàng bảo vệ. *(Đã ký xác nhận)*



