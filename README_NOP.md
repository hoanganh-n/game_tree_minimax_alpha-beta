# README BÀI NỘP NHÓM 10

Nhóm / lớp / 4 thành viên: **Nhóm 10 — UET.AI2014_1**.

1. Hoàng Trung Hiếu — MSSV 25022849.
2. Trần Nguyên Hiển Minh — MSSV 25022950.
3. Lê Bảo Ngân — MSSV 25022958.
4. Nguyễn Hoàng Anh — MSSV 25022772.

Python / hệ điều hành / ngày chạy: **Python 3.14.4 / Linux (WSL2, x86_64) / 24/10/2026**.

## Tái chạy

Giải nén ZIP, mở thư mục chứa `run.py`. Mã chỉ dùng thư viện chuẩn, yêu cầu Python ≥ 3.10. Môi trường kiểm tra dùng `python3`; có thể thay bằng `python` nếu máy đã cấu hình đúng phiên bản.

```text
python3 kiem_tra_moi_truong.py
python3 chay_mau.py
python3 -m unittest -v test_nhom
python3 chay_kiem_thu.py
python3 run.py --batch --tag bat_buoc
python3 run.py --data du_lieu_nhom.json --tag tu_tao
python3 run.py --case T0 --algo alphabeta --trace --tag trace_T0
```

## Dữ liệu và kết quả

- Tệp dữ liệu: `du_lieu_nhom.json`; seed **2579**, tạo bằng `python3 tao_du_lieu.py --seed 2579`. Gồm N1 (16 lá, gốc MAX) và N2 (8 lá, gốc MIN). Tệp hiện tại khớp dữ liệu sinh từ seed này; script chỉ ghi đè tệp có sẵn khi thêm `--overwrite`.
- JSON/CSV chung 24 cấu hình: `output/bat_buoc.json`, `output/bat_buoc.csv`; đã kiểm tra đủ 24 cấu hình (12 cơ bản, 10 tham số, 2 affine).
- JSON/CSV riêng 8 cấu hình: `output/tu_tao.json`, `output/tu_tao.csv`; đủ 2 cây × 2 thuật toán × 2 thứ tự. N1 trả `(value=13, action=A)`; N2 trả `(value=-13, action=B)` với cả Minimax/Alpha–Beta và LR/RL.
- Trace và phép tính tay đối chiếu: `output/trace_T0.json` (vết Alpha–Beta, T0, LR), `output/trace_T0.csv` (thống kê), `output/t11.json/.csv` (t = 11); bản tính tay tổng hợp `TinhTay.pdf`, bản thành phần trong `tinh_tay/`. T0, LR trả `(10, A)`; Alpha–Beta duyệt 22 nút, 10 lá, cắt 3 nhánh có gốc `L10`, `L12`, `B2`.
- Log kiểm thử thật và kết quả: `output/ket_qua_test.txt` ghi **9 test nhóm PASS**, `OK`, `EXIT_CODE=0`.**35/35 test PASS** (24 mẫu + 2 ví dụ + 9 nhóm); kết quả 32 cấu hình JSON khớp phép tính lại khi bỏ `elapsed_ms`, đều thỏa `visited == expanded + leaves`.
- Tệp nhóm sửa/thêm, lý do: `test_nhom.py` (9 test riêng, phân bổ 2–2–3–2); `du_lieu_nhom.json` (dữ liệu riêng tái lập); `output/` (thực nghiệm và log); `TinhTay.pdf` (tổng hợp tính tay); `MauBaoCao/BaoCao.tex`, `BaoCao.pdf` (nguồn và bản báo cáo); `README_NOP.md` (hướng dẫn tái chạy); `DongGop.md` (ghi đóng góp). Phân công chi tiết trong `phan_cong.md`.
- Lỗi chưa sửa / giới hạn: chưa phát hiện lỗi qua các kiểm tra trên; `elapsed_ms` thay đổi theo máy và lần chạy. Chưa có `ThuyetTrinh.pptx`; `DongGop.md` và nguồn báo cáo còn mục chưa điền, test chưa ghi tên/MSSV người phụ trách. Cần hoàn thiện trước khi chạy `python3 dong_goi.py` để tạo `Nhom10_CayTroChoi_GiuaKy.zip`. Chưa xác nhận nội dung/số trang PDF hoặc khả năng tái chạy trên máy khác.

Người đã giải nén chạy lại trên máy khác / ngày / kết quả: **Chưa thực hiện hoặc chưa có xác nhận**. Bổ sung người thực hiện, ngày và kết quả thực tế sau khi tái chạy; không ghi đã chạy khi chưa thực hiện.
