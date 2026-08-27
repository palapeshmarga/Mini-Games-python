import flet as ft
from Tests import generate_nums

def main(page: ft.Page):
    page.title = "Sudoku"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.bgcolor = "#41215e"
    
    if page.web or page.platform in [ft.PagePlatform.WINDOWS, ft.PagePlatform.MACOS, ft.PagePlatform.LINUX]:
        page.window.width = 450
        page.window.height = 800
        page.window.resizable = True
        page.window.center()

    selected_square = None

    def Start(e):
        nonlocal selected_square
        selected_square = None
        page.clean() 

        # Generate a fresh puzzle on game start
        puzzle_nums = generate_nums()
        nums_iter = iter(puzzle_nums)

        grid = ft.GridView(
            expand=False,
            runs_count=9,   
            child_aspect_ratio=1.0,  
            spacing=2,               
            run_spacing=2,
            width=360,
            height=360,
        )

        def validate_board():
            """Evaluates duplicate numbers in rows, columns, and 3x3 blocks."""
            for container in grid.controls:
                val = container.content.value
                r, c = container.data["pos"]
                is_fixed = container.data["fixed"]

                # Reset to default background colors
                if container == selected_square:
                    container.bgcolor = ft.Colors.BLUE_100
                elif is_fixed:
                    container.bgcolor = ft.Colors.GREY_200
                else:
                    container.bgcolor = ft.Colors.WHITE

                if not val:
                    continue

                # Check for conflicts across the grid
                has_conflict = False
                for other in grid.controls:
                    if other == container or not other.content.value:
                        continue
                    
                    o_val = other.content.value
                    o_r, o_c = other.data["pos"]

                    same_row = (r == o_r)
                    same_col = (c == o_c)
                    same_block = (r // 3 == o_r // 3) and (c // 3 == o_c // 3)

                    if o_val == val and (same_row or same_col or same_block):
                        has_conflict = True
                        break

                if has_conflict:
                    container.bgcolor = ft.Colors.RED_100

        def square_clicked(e):
            nonlocal selected_square
            # Only allow selecting editable (non-fixed) cells
            if not e.control.data["fixed"]:
                selected_square = e.control
                validate_board()
                page.update()

        def number_button_clicked(e):
            nonlocal selected_square
            num_placed = str(e.control.data)

            if selected_square is not None:
                selected_square.content.value = num_placed
                validate_board()
                page.update()

        def clear_button_clicked(e):
            nonlocal selected_square
            if selected_square is not None:
                selected_square.content.value = ""
                validate_board()
                page.update()

        # Build 9x9 Grid
        for r in range(9):
            for c in range(9):
                current_num = next(nums_iter)
                is_fixed = current_num != ""

                border_top = ft.BorderSide(1, ft.Colors.BLACK) if r == 0 else ft.BorderSide(0, ft.Colors.TRANSPARENT)
                border_left = ft.BorderSide(1, ft.Colors.BLACK) if c == 0 else ft.BorderSide(0, ft.Colors.TRANSPARENT)
                border_bottom = ft.BorderSide(3, ft.Colors.BLACK) if r in [2, 5, 8] else ft.BorderSide(1, ft.Colors.BLACK)
                border_right = ft.BorderSide(3, ft.Colors.BLACK) if c in [2, 5, 8] else ft.BorderSide(1, ft.Colors.BLACK)

                grid.controls.append(
                    ft.Container(
                        content=ft.Text(
                            current_num, 
                            color=ft.Colors.BLACK if is_fixed else ft.Colors.BLUE_900, 
                            weight=ft.FontWeight.BOLD if is_fixed else ft.FontWeight.NORMAL, 
                            size=20
                        ),
                        alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.GREY_200 if is_fixed else ft.Colors.WHITE,
                        border=ft.Border(
                            top=border_top,
                            bottom=border_bottom,
                            left=border_left,
                            right=border_right
                        ),
                        on_click=square_clicked,
                        data={"pos": (r, c), "fixed": is_fixed}
                    )
                )

        # Build 1-9 Number Selector Row
        num_btns = [
            ft.ElevatedButton(
                content=ft.Text(str(n), size=18, weight=ft.FontWeight.BOLD),
                width=38,
                height=45,
                data=n,
                on_click=number_button_clicked,
                style=ft.ButtonStyle(padding=0)
            ) for n in range(1, 10)
        ]
        
        # Action button to erase a number from a selected cell
        clear_btn = ft.ElevatedButton(
            content = ft.Icon(ft.Icons.BACKSPACE_OUTLINED, size=18),
            width=45,
            height=45,
            on_click=clear_button_clicked,
            style=ft.ButtonStyle(padding=0)
        )

        controls_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=4,
            controls=num_btns + [clear_btn]
        )

        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[grid, controls_row]
            )
        )
        page.update() 

    def Home():
        start_button = ft.ElevatedButton(
            content=ft.Text("Start", size=25, weight=ft.FontWeight.BOLD),
            on_click=Start,  
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            height=60,
            width=150,
        )
        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                controls=[start_button]
            )
        )

    Home()

ft.app(target=main)