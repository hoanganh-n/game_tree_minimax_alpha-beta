# Nội dung thuyết trình — Nhóm 10

**Đề tài:** Cây trò chơi: Minimax và Alpha–Beta — chọn đúng hành động, giải thích được nhánh cắt.

Tài liệu dùng để dựng `ThuyetTrinh.pptx` gồm **7 slide**, trình bày trong **5 phút**, sau đó **demo 3 phút**. Nội dung bám theo [dàn ý bảo vệ](DanY_BaoVe.md) và [báo cáo của nhóm](MauBaoCao/BaoCao.tex).

**Câu hỏi xuyên suốt:** Làm sao bỏ bớt nhánh mà vẫn chọn đúng nước đi? Và vì sao đúng điểm vẫn có thể chọn sai?

Theo [đề bài](De_Nhom10_SinhVien.pdf), nhóm khảo sát cây trò chơi có sẵn, với utility ở lá đã cho. Mỗi nút biểu diễn một trạng thái, mỗi cạnh là một hành động, mỗi đường xuống lá là một diễn biến ván chơi. Trọng tâm là lựa chọn khi đối thủ cũng chơi tối ưu, giải thích nhánh cắt và kiểm chứng kết quả.



## Slide 1 — Nhánh có lá 101 có phải lựa chọn tốt nhất?

### Nội dung trên slide

**CÂY TRÒ CHƠI: MINIMAX VÀ ALPHA–BETA**

*Chọn đúng hành động — giải thích được nhánh cắt*

- Mỗi lượt chọn một nhánh; hai người luân phiên MAX/MIN.
- MAX muốn điểm cao, MIN muốn điểm thấp; điểm kết thúc nhìn từ phía MAX.
- **Nếu đối thủ cũng chơi tối ưu, MAX nên chọn nhánh nào?**

### Hình minh họa

Vẽ cây T0 rút gọn `R (MAX) → A, B (MIN)`. Đánh dấu lá 101 nằm trong nhánh B. Chưa điền giá trị A/B để người nghe suy nghĩ; slide tiếp theo sẽ trả lời. Khi rút gọn, dùng dấu ba chấm cho các tầng bị lược và giữ đúng vị trí lá.

**Ý dẫn sang slide 2:** Muốn chọn đúng, phải tính cả phản ứng của đối thủ.

## Slide 2 — Minimax: chọn kết quả có thể bảo đảm

### Nội dung trên slide

**Tính từ lá lên gốc:** lá trả utility; MAX lấy lớn nhất, MIN lấy nhỏ nhất.

```text
V(s) = utility(s)                  nếu s là lá
V(s) = max V(c), c ∈ Children(s)    nếu s là MAX
V(s) = min V(c), c ∈ Children(s)    nếu s là MIN
```

**T0, thứ tự LR — tính tay và chương trình cùng kết quả:**

- `A = min(10, 13) = 10`; `B = min(4, 100) = 4`.
- `R = max(10, 4) = 10` → **action = A**.
- Đường chơi tối ưu: **R → A → A1 → A12 → L04**.
- Minimax đọc đủ **16 lá** để tìm lựa chọn này.

### Hình minh họa

Vẽ cây T0 rút gọn đến tầng `A1, A2, B1, B2`, ghi giá trị `10, 13, 4, 100` rồi truyền lên A/B/R. Đường chơi đầy đủ có thể đặt thành một dòng bên dưới.

**Điểm cần nói:** B chứa lá 101 nhưng MIN sẽ chọn B1, ép kết quả xuống 4. Chọn A bảo đảm 10 khi hai bên chơi tối ưu.

**Ý dẫn sang slide 3:** Đã biết cách chọn đúng, liệu có cần đọc hết các lá?

## Slide 3 — Có cần đọc hết cây để chọn đúng?

### Nội dung trên slide

- Xét A trước: MAX đã có lựa chọn bảo đảm **10**.
- Sang B: MIN có thể chọn B1, đưa kết quả xuống **không quá 4**.
- MAX sẽ giữ A → **không cần xét B2**.
- Alpha–Beta dùng cận α/β để nhận ra các nhánh không thể cải thiện lựa chọn.

**T0/LR:**

| Thống kê | Minimax | Alpha–Beta |
|---|---:|---:|
| Value / action | 10 / A | 10 / A |
| Lá đã đọc | 16 | 10 |

**Bỏ L10, L12 và cây con B2 → tiết kiệm 37,5% số lá.**

### Hình minh họa

Trên cây T0, làm mờ L10, L12 và toàn bộ B2. Thêm chú thích tại B11: “Nhận α = 10; đọc L09 = 4; MIN cắt vì 4 ≤ 10”.

**Chú thích ngắn:** MAX cắt khi `best >= beta`; MIN cắt khi `best <= alpha`. Giữ cửa sổ đã cập nhật khi chuyển sang con tiếp theo (`search.py`, dòng 43, 49–60).

**Ý dẫn sang slide 4:** Một nhánh chưa đọc hết sẽ trả về thông tin gì? Có thể coi số đó là giá trị thật không?

## Slide 4 — Đúng điểm vẫn có thể chọn sai nước đi

### Nội dung trên slide

```text
                  R: MAX
                 /      \
             A: MIN    B: MIN
              /  \      /  \
             10  12    10   2
```

- Giá trị thật: **A = 10, B = 2, R = 10** → chọn **A**.
- LR: xét A trước → B nhận `alpha = 10`.
- B đọc lá 10 rồi cắt lá 2, trả **10, UPPER**: `V(B) <= 10`.
- Chọn action bằng `>=` có thể trả sai **(10, B)**; MAX thực nhận 2 nếu MIN chơi tối ưu.

**Cận không nhất thiết là giá trị thật. Chọn action phải dùng so sánh nghiêm.**

### Hình minh họa

Vẽ T1 đúng bốn lá; gạch nhánh đến lá 2 và đặt nhãn “chưa đọc” khi minh họa lần chạy LR. Phân biệt nhãn “giá trị thật B = 2” với “số trả B = 10, UPPER”.

**Ý dẫn sang slide 5:** Nhóm cần bằng chứng nào để xác nhận chương trình chọn đúng, kể cả ở những tình huống dễ nhầm?

## Slide 5 — Nhóm kiểm chứng lựa chọn như thế nào?

### Nội dung trên slide

**Tính tay độc lập → chạy chương trình → đối chiếu → kiểm thử tự động.**

- T0: cùng `(value, action) = (10, A)`; vết cắt khớp tính tay.
- T1: kiểm cả value và action để bắt trường hợp **đúng điểm, sai nhánh**.
- Bộ test bao phủ điểm âm, utility 0, gốc MIN, hòa LR/RL, số đếm và trace.

| Thử lỗi trên bản sao | Minh chứng phát hiện |
|---|---|
| Khởi tạo MAX bằng 0 | Test 1 với toàn điểm âm: action không hợp lệ, Minimax lỗi khi dựng đường chơi |
| Chọn action tại MAX bằng `>=` | Test 3 trên T1: trả `(10, B)` thay vì `(10, A)` |

**Log hiện có: 9/9 test đạt; có bốn test với kỳ vọng tính tay độc lập được nêu trong báo cáo.**

### Hình minh họa

Dùng sơ đồ bốn bước kiểm chứng và bảng hai lỗi. Đặt “9/9 test đạt” thành minh chứng cuối slide. Nguồn: `test_nhom.py`, `output/ket_qua_test.txt`, mục 8 của báo cáo.

**Ý dẫn sang slide 6:** Khi đã kiểm chứng tính đúng, nhóm khảo sát việc cắt tỉa thay đổi thế nào theo dữ liệu và thứ tự.

## Slide 6 — Khi nào Alpha–Beta tiết kiệm được nhiều lá?

### Nội dung trên slide

**24 cấu hình bắt buộc + 8 cấu hình riêng; N1/N2 dùng seed 2579.**

| Cây | Value / action ở cả LR và RL | Lá Minimax | Lá AB/LR | Lá AB/RL |
|---|---|---:|---:|---:|
| T0 | 10 / A | 16 | 10 | 16 |
| N1 — MAX | 13 / A | 16 | 9 | 16 |
| N2 — MIN | −13 / B | 8 | 8 | 6 |

**Không có thứ tự luôn tốt nhất:** LR tốt hơn trên T0/N1; RL tốt hơn trên N2.

**Thay dữ liệu có thể đổi cả giá trị và mức cắt tỉa:**

- Thay L01 bằng `t = 10, 11, 14`: value lần lượt `10, 11, 12`; số lá AB/LR là `10, 9, 9`.
- Đổi toàn bộ utility `u → 2u − 7`: value `10 → 13`, vẫn chọn A và đọc 10 lá.

### Hình minh họa

Dùng biểu đồ cột nhóm cho số lá trên T0/N1/N2. Hai nhận xét về thay dữ liệu đặt thành chú thích ngắn bên dưới; chỉ trình bày xu hướng, phần tính khoảng đầy đủ nằm trong báo cáo.

**Điểm cần nói:** Xét nhánh có lợi sớm giúp thiết lập cận hiệu quả. Phép đổi utility có hệ số dương bảo toàn thứ tự nên giữ lựa chọn và vị trí cắt trong cấu hình này.

**Nguồn:** `output/bat_buoc.json` (24 cấu hình), `output/tu_tao.json` (8 cấu hình), `du_lieu_nhom.json`.

**Ý dẫn sang slide 7:** Từ các ví dụ và thực nghiệm, nhóm rút ra điều gì về chọn nước đi?

## Slide 7 — Bỏ bớt nhánh, vẫn cần bảo đảm chọn đúng

### Nội dung trên slide

**Ba kết luận:**

- Alpha–Beta giữ value/action ở gốc như Minimax với cùng thứ tự và quy tắc hòa.
- Hiệu quả cắt tỉa phụ thuộc thứ tự; cần phân biệt số cận và giá trị thật.
- Kiểm chứng cần xét cả điểm và hành động; số cận phải được hiểu đúng.

**Giới hạn:** cây tối đa 16 lá; chưa đo thời gian lặp và chưa khảo sát nhiều seed.


**Chuyển sang demo:** “Nhóm sẽ minh họa trên T1: dự đoán trước nhánh bị cắt, giải thích số cận, sau đó đổi thứ tự duyệt để đối chiếu.”


