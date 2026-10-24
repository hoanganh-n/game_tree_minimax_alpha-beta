import unittest

from data_cases import case, parameter_tree
from search import solve
from tree_model import load_cases, make_tree


class TestNhom10(unittest.TestCase):


    def test_01_am_va_khong_sua_input(self):
        """Test 1: Toàn điểm âm và bảo toàn mảng dữ liệu đầu vào.
        Tính tay: A1=max(-3,-7)=-3; A2=max(-1,-5)=-1; A=min(-3,-1)=-3;
        B1=max(-9,-2)=-2; B2=max(-6,-4)=-4; B=min(-2,-4)=-4;
        R=max(-3,-4)=-3, chọn A.
        """
        leaves=[-3,-7,-1,-5,-9,-2,-6,-4]
        original=list(leaves)
        tree=make_tree(leaves)
        for algo in ("minimax","alphabeta"):
            r=solve(tree, algo, "LR")
            self.assertEqual((r["value"],r["action"]),(-3,"A"))
        self.assertEqual(leaves,original)

    def test_02_utility_zero_va_duong_di_toi_uu(self):
        """Test 2: Utility 0 là lá hợp lệ và đường đi tối ưu.
        Tính tay: A1=max(0,-3)=0; A2=max(6,2)=6; A=min(0,6)=0;
        B1=max(-5,-1)=-1; B2=max(4,1)=4; B=min(-1,4)=-1;
        R=max(0,-1)=0, chọn A. PV: R -> A -> A1 -> L01.
        """
        tree=make_tree([0,-3,6,2,-5,-1,4,1])
        r=solve(tree,"minimax","LR")
        self.assertEqual((r["value"],r["action"]),(0, "A"))
        self.assertEqual(r["principal_variation"],["R", "A", "A1", "L01"])
        self.assertEqual(r["leaves"],8)



    def test_03_T1_false_tie(self):
        """Test 3: Kiểm tra cây T1 bắt lỗi hòa giả giữa các cận.
        Tính tay độc lập: A = min(10, 12) = 10;
        B = min(10, 2) = 2; R phải chọn A với giá trị 10.
        Nếu chỉ kiểm tra value sẽ bỏ sót kết quả sai (10, B).
        """
        for algorithm in ("minimax", "alphabeta"):
            with self.subTest(algorithm=algorithm):
                result = solve(case("T1"), algorithm=algorithm, order="LR")
                self.assertEqual(
                    (result["value"], result["action"]),
                    (10, "A"),
                )

    def test_04_T0_pruning_bounds_and_counts(self):
        """Test 4: Vết tính tay Alpha-Beta trên T0, cờ cận và số đếm.
        Tính tay: A trả về 10 -> B nhận alpha = 10.
        B11 đọc 4 và cắt L10; B12 đọc 3 và cắt L12;
        B trả về 4 và cắt toàn bộ cây con B2.
        """
        result = solve(case("T0"), algorithm="alphabeta", order="LR")

        self.assertEqual((result["value"], result["action"]), (10, "A"))
        self.assertEqual(result["pruned_roots"], ["L10", "L12", "B2"])
        self.assertEqual(
            result["leaf_order"],
            ["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08",
             "L09", "L11"],
        )
        self.assertEqual(
            set(result["unvisited_nodes"]),
            {"L10", "L12", "B2", "B21", "B22", "L13", "L14", "L15", "L16"},
        )
        for node, expected_value in (("B11", 4), ("B12", 3), ("B", 4)):
            with self.subTest(node=node):
                returned = result["returns"][node]
                # UPPER có nghĩa là giá trị thực <= giá trị trả về
                self.assertEqual(returned["value"], expected_value)
                self.assertEqual(returned["bound"], "UPPER")

        # 12 internal nodes + 10 leaves = 22 visited nodes
        expected_counts = {
            "visited": 22,
            "expanded": 12,
            "leaves": 10,
            "cutoffs": 3,
            "pruned_branches": 3,
            "max_depth": 4,
        }
        for field, expected in expected_counts.items():
            with self.subTest(statistic=field):
                self.assertEqual(result[field], expected)
        self.assertEqual(
            result["visited"], result["expanded"] + result["leaves"]
        )


    def test_05_t0_parameter(self):
        """Test 5: Khảo sát tham số T0(t) khi t in {10, 11, 14}.
        Khảo sát giá trị gốc và số lá Alpha-Beta đọc được.
        """
        expected = {
            10: (10, 10),
            11: (11, 9),
            14: (12, 9),
        }

        for t, (value, ab_leaves) in expected.items():
            with self.subTest(t=t):
                tree = parameter_tree(t)

                mm = solve(tree, "minimax", "LR")
                ab = solve(tree, "alphabeta", "LR")

                self.assertEqual((mm["value"], mm["action"]), (value, "A"))
                self.assertEqual((ab["value"], ab["action"]), (value, "A"))
                self.assertEqual(ab["leaves"], ab_leaves)

    def test_06_n2_root_min(self):
        """Test 6: Kiểm tra cây N2 có lượt đi đầu tiên là MIN."""
        cases = dict(load_cases("du_lieu_nhom.json"))
        tree = cases["N2"]

        self.assertEqual(tree.player, "MIN")

        for algo in ("minimax", "alphabeta"):
            for order in ("LR", "RL"):
                with self.subTest(algo=algo, order=order):
                    r = solve(tree, algo, order)

                    self.assertEqual(r["value"], -13)
                    self.assertEqual(r["action"], "B")

    def test_07_invalid_leaf_data(self):
        """Test 7: Kiểm tra số lá không hợp lệ hoặc utility sai kiểu."""
        invalid_cases = [
            [1, 2, 3],
            [1, "abc", 3, 4],
            [1, True, 3, 4],
        ]

        for leaves in invalid_cases:
            with self.subTest(leaves=leaves):
                with self.assertRaises(ValueError):
                    make_tree(leaves, root_player="MAX")


    def test_08_hoa_that_theo_LR_RL(self):
        """Test 8: Hiện tượng hòa thật theo thứ tự duyệt LR/RL."""
        tree = make_tree([2,5,2,7])
        for algo in ('minimax','alphabeta'):
            r_lr = solve(tree,algo,"LR")
            r_rl = solve(tree,algo,"RL")

            self.assertEqual(r_lr["value"],2)
            self.assertEqual(r_rl["value"],2)
            self.assertEqual(r_lr["action"],'A')
            self.assertEqual(r_rl["action"],'B')

    def test_09_trace_bat_tat_va_tich_hop_json(self):
        """Test 9: Bật/tắt trace không đổi kết quả và tích hợp json."""
        cases = dict(load_cases("du_lieu_nhom.json"))
        tree_n1 = cases["N1"]

        r_off = solve(tree_n1,"alphabeta",trace=False)
        r_on = solve(tree_n1,"alphabeta",trace=True)

        for key in ('value', 'action', 'visited', 'expanded', 'leaves', 'cutoffs'):
            self.assertEqual(r_off[key],r_on[key])

        self.assertEqual(len(r_off["trace"]),0)
        self.assertGreater(len(r_on["trace"]),0)

        for r in (r_off, r_on):
            self.assertEqual(r['visited'], r['expanded'] + r['leaves'])

if __name__ == "__main__":
    import unittest
    import test_nhom

    test_nhom.solve = solve
    unittest.main(module=test_nhom)