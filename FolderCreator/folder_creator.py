import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path


class FolderCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("폴더 자동 생성기")
        self.root.geometry("600x560")
        self.root.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        pad = {"padx": 10, "pady": 5}

        # --- 루트 경로 ---
        frame_root = tk.LabelFrame(self.root, text="생성 위치", font=("맑은 고딕", 10))
        frame_root.pack(fill="x", **pad)

        self.var_root = tk.StringVar(value="D:\\")
        tk.Entry(frame_root, textvariable=self.var_root, font=("맑은 고딕", 10), width=48).pack(
            side="left", padx=6, pady=6
        )
        tk.Button(frame_root, text="찾아보기", command=self._browse_root).pack(side="left", padx=4)

        # --- 트리 ---
        frame_tree = tk.LabelFrame(self.root, text="폴더 구조  (더블클릭으로 이름 수정)", font=("맑은 고딕", 10))
        frame_tree.pack(fill="both", expand=True, **pad)

        self.tree = ttk.Treeview(frame_tree, selectmode="browse")
        self.tree.heading("#0", text="폴더 트리")
        self.tree.pack(side="left", fill="both", expand=True, padx=6, pady=6)

        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y", pady=6)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.bind("<Double-1>", self._on_double_click)

        # --- 폴더 추가 입력 ---
        frame_add = tk.LabelFrame(self.root, text="폴더 추가", font=("맑은 고딕", 10))
        frame_add.pack(fill="x", **pad)

        tk.Label(frame_add, text="폴더명:", font=("맑은 고딕", 10)).pack(side="left", padx=6)
        self.var_name = tk.StringVar()
        entry_name = tk.Entry(frame_add, textvariable=self.var_name, font=("맑은 고딕", 10), width=22)
        entry_name.pack(side="left", padx=4, pady=6)
        entry_name.bind("<Return>", lambda e: self._add_folder())

        tk.Button(frame_add, text="선택 항목 하위에 추가", command=self._add_folder).pack(side="left", padx=4)
        tk.Button(frame_add, text="최상위에 추가", command=self._add_top_folder).pack(side="left", padx=4)
        tk.Button(frame_add, text="삭제", fg="red", command=self._delete_folder).pack(side="left", padx=4)

        # --- 실행 버튼 ---
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(fill="x", padx=10, pady=8)

        tk.Button(
            frame_btn, text="D 드라이브에 폴더 생성", bg="#2196F3", fg="white",
            font=("맑은 고딕", 11, "bold"), height=2, command=self._create_folders
        ).pack(fill="x")

        self._load_default()

    def _load_default(self):
        recdata = self.tree.insert("", "end", text="RECDATA", open=True)
        for i in range(1, 11):
            self.tree.insert(recdata, "end", text=f"TEST{i}")

    def _browse_root(self):
        path = filedialog.askdirectory(title="생성 위치 선택")
        if path:
            self.var_root.set(path.replace("/", "\\") + "\\")

    def _add_folder(self):
        name = self.var_name.get().strip()
        if not name:
            messagebox.showwarning("입력 오류", "폴더명을 입력하세요.")
            return
        selected = self.tree.selection()
        parent = selected[0] if selected else ""
        self.tree.insert(parent, "end", text=name, open=True)
        self.var_name.set("")

    def _add_top_folder(self):
        name = self.var_name.get().strip()
        if not name:
            messagebox.showwarning("입력 오류", "폴더명을 입력하세요.")
            return
        self.tree.insert("", "end", text=name, open=True)
        self.var_name.set("")

    def _delete_folder(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("선택 없음", "삭제할 폴더를 선택하세요.")
            return
        name = self.tree.item(selected[0], "text")
        if messagebox.askyesno("삭제 확인", f"'{name}' 및 하위 폴더를 목록에서 삭제할까요?"):
            self.tree.delete(selected[0])

    def _on_double_click(self, event):
        item = self.tree.identify_row(event.y)
        if not item:
            return
        x, y, w, h = self.tree.bbox(item)
        current_name = self.tree.item(item, "text")

        entry = tk.Entry(self.tree, font=("맑은 고딕", 10))
        entry.insert(0, current_name)
        entry.select_range(0, "end")
        entry.place(x=x, y=y, width=w, height=h)
        entry.focus()

        def save(e=None):
            new_name = entry.get().strip()
            if new_name:
                self.tree.item(item, text=new_name)
            entry.destroy()

        entry.bind("<Return>", save)
        entry.bind("<FocusOut>", save)

    def _tree_to_dict(self, parent=""):
        result = {}
        for child in self.tree.get_children(parent):
            name = self.tree.item(child, "text")
            result[name] = self._tree_to_dict(child)
        return result

    def _create_recursive(self, base, tree):
        created, errors = [], []
        for name, subtree in tree.items():
            path = Path(base) / name
            try:
                path.mkdir(parents=True, exist_ok=True)
                created.append(str(path))
            except Exception as e:
                errors.append(f"{path}: {e}")
                continue
            sub_c, sub_e = self._create_recursive(str(path), subtree)
            created.extend(sub_c)
            errors.extend(sub_e)
        return created, errors

    def _create_folders(self):
        root_path = self.var_root.get().strip()
        if not root_path:
            messagebox.showwarning("경로 오류", "생성 위치를 입력하세요.")
            return

        tree_dict = self._tree_to_dict()
        if not tree_dict:
            messagebox.showwarning("구조 없음", "생성할 폴더를 먼저 추가하세요.")
            return

        if not messagebox.askyesno("확인", f"{root_path} 에 폴더를 생성하시겠습니까?"):
            return

        created, errors = self._create_recursive(root_path, tree_dict)

        msg = f"폴더 {len(created)}개 생성 완료!"
        if errors:
            msg += f"\n\n오류 {len(errors)}건:\n" + "\n".join(errors)
            messagebox.showwarning("완료 (오류 있음)", msg)
        else:
            messagebox.showinfo("완료", msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = FolderCreatorApp(root)
    root.mainloop()