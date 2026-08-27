import asyncio
import flet as ft
from Tests import generate_nums


# --- Timer Manager ---
class GameTimer:

    def __init__(self):
        self.seconds = 0
        self.is_paused = False
        self.is_running = False

    def reset(self):
        self.seconds = 0
        self.is_paused = False
        self.is_running = True


async def main(page: ft.Page):
    page.title = "Sudoku"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.bgcolor = "#A16600"

    # Screen alignment configuration for responsiveness across desktop & mobile
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    if page.web or page.platform in [
        ft.PagePlatform.WINDOWS,
        ft.PagePlatform.MACOS,
        ft.PagePlatform.LINUX,
    ]:
        page.window.width = 450
        page.window.height = 800
        page.window.resizable = True
        await page.window.center()

    selected_square = None
    selected_difficulty = None
    is_note_mode = False
    timer = GameTimer()

    def Start(e):
        nonlocal selected_square, is_note_mode
        selected_square = None
        is_note_mode = False
        page.clean()

        # Reset & Start Timer Loop
        timer.reset()

        puzzle_nums = generate_nums(selected_difficulty)
        nums_iter = iter(puzzle_nums)

        # --- Top Header UI: Difficulty (Left) | Timer & Pause (Right) ---
        diff_label = ft.Text(
            f"Difficulty: {selected_difficulty}",
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
        )

        timer_text = ft.Text(
            "00:00", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE
        )


        def toggle_pause(e=None):
            # Pause timer and blur/disable board
            timer.is_paused = True
            pause_btn.icon = ft.Icons.PLAY_ARROW
            pause_btn.tooltip = "Resume"
            board_wrapper.opacity = 0.05
            board_wrapper.disabled = True
            page.update()

            def continue_click(e):
                # Resume game and close dialog
                timer.is_paused = False
                pause_btn.icon = ft.Icons.PAUSE
                pause_btn.tooltip = "Pause"
                board_wrapper.opacity = 1.0
                board_wrapper.disabled = False
                pause_dialog.open = False
                page.update()

            def restart_click(e):
                # Reset game to Home screen and close dialog
                pause_dialog.open = False
                Home()

            pause_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Game Paused"),
                content=ft.Text("What would you like to do?"),
                actions=[
                    ft.Button(content=ft.Text("Restart"), on_click=restart_click),
                    ft.Button(content=ft.Text("Continue"), on_click=continue_click),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )

            page.show_dialog(pause_dialog)

        pause_btn = ft.IconButton(
            icon=ft.Icons.PAUSE,
            icon_color=ft.Colors.WHITE,
            tooltip="Pause",
            on_click=toggle_pause,
        )

        header_row = ft.Row(
            width=360,
            controls=[
                diff_label,
                ft.Row(
                    controls=[timer_text, pause_btn],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
        )

        # Timer Task
        async def run_timer():
            while timer.is_running:
                if not timer.is_paused:
                    mins = timer.seconds // 60
                    secs = timer.seconds % 60
                    timer_text.value = f"{mins:02d}:{secs:02d}"
                    page.update()
                    timer.seconds += 1
                await asyncio.sleep(1)

        page.run_task(run_timer)

        # --- Sudoku Grid ---
        grid = ft.GridView(
            expand=False,
            runs_count=9,
            child_aspect_ratio=1.0,
            spacing=2,
            run_spacing=2,
            width=360,
            height=360,
        )

        def get_conflicting_cells():
            """Finds all cells that violate Sudoku rules (same row, col, or 3x3 block)."""
            conflicts = set()
            controls = grid.controls

            for i in range(81):
                val1 = controls[i].data["value"]
                if not val1:
                    continue
                r1, c1 = controls[i].data["pos"]

                for j in range(i + 1, 81):
                    val2 = controls[j].data["value"]
                    if not val2 or val1 != val2:
                        continue
                    r2, c2 = controls[j].data["pos"]

                    same_row = r1 == r2
                    same_col = c1 == c2
                    same_block = (r1 // 3 == r2 // 3) and (c1 // 3 == c2 // 3)

                    if same_row or same_col or same_block:
                        conflicts.add(controls[i])
                        conflicts.add(controls[j])

            return conflicts

        def check_win(conflicts):
            """Returns True if every cell is filled and there are zero conflicts."""
            if len(conflicts) > 0:
                return False

            for container in grid.controls:
                if container.data["value"] == "":
                    return False
            return True

        def update_notes():
            """Evaluates notes and marks duplicates in the same row/col as red."""
            for container in grid.controls:
                r, c = container.data["pos"]
                notes = container.data["notes"]

                if not notes:
                    continue

                line_values = set()
                for other in grid.controls:
                    o_r, o_c = other.data["pos"]
                    o_val = other.data["value"]
                    if (r == o_r or c == o_c) and o_val != "":
                        line_values.add(o_val)

                for num in list(notes.keys()):
                    if num in line_values:
                        if container.data["value"] == "":
                            notes[num].color = ft.Colors.RED
                    else:
                        notes[num].color = ft.Colors.GREY_600

                note_controls = [
                    notes[str(n)] if str(n) in notes else ft.Container()
                    for n in range(1, 10)
                ]
                container.data["note_grid"].controls = note_controls

            page.update()

        def highlight_board():
            """Updates grid background colors, highlights matching numbers, conflicts, and win state."""
            sel_val = selected_square.data["value"] if selected_square else None
            conflicts = get_conflicting_cells()

            for container in grid.controls:
                val = container.data["value"]
                is_fixed = container.data["fixed"]

                if container in conflicts:
                    container.bgcolor = ft.Colors.RED_100
                elif container == selected_square:
                    container.bgcolor = ft.Colors.BLUE_200
                elif sel_val and val == sel_val and val != "":
                    container.bgcolor = ft.Colors.GREY_500
                elif is_fixed:
                    container.bgcolor = ft.Colors.GREY_200
                else:
                    container.bgcolor = ft.Colors.WHITE

            update_notes()

            if check_win(conflicts):
                timer.is_running = False

                def play_again_click(e):
                    page.clean()
                    Home()

                dialog = ft.AlertDialog(
                    title=ft.Text("Congratulations!"),
                    content=ft.Text(
                        f"You solved the puzzle correctly in {timer_text.value}!"
                    ),
                    actions=[
                        ft.Button(
                            content=ft.Text("Play Again"),
                            on_click=play_again_click,
                        )
                    ],
                )
                page.show_dialog(dialog)

        def square_clicked(e):
            nonlocal selected_square
            selected_square = e.control
            highlight_board()
            page.update()

        def number_button_clicked(e):
            nonlocal selected_square
            if selected_square is None or selected_square.data["fixed"]:
                return

            num_placed = str(e.control.data)

            if is_note_mode:
                notes = selected_square.data["notes"]
                if num_placed in notes:
                    del notes[num_placed]
                else:
                    notes[num_placed] = ft.Text(
                        num_placed,
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREY_600,
                    )
            else:
                selected_square.data["notes"].clear()
                selected_square.data["value"] = num_placed
                selected_square.data["main_text"].value = num_placed

            highlight_board()
            page.update()

        def clear_button_clicked(e):
            nonlocal selected_square
            if selected_square is not None and not selected_square.data["fixed"]:
                selected_square.data["value"] = ""
                selected_square.data["main_text"].value = ""
                selected_square.data["notes"].clear()
                highlight_board()
                page.update()

        def toggle_note_mode(e):
            nonlocal is_note_mode
            is_note_mode = not is_note_mode
            note_btn.bgcolor = (
                ft.Colors.AMBER_300 if is_note_mode else ft.Colors.WHITE
            )
            page.update()

        # Build 9x9 Grid (All 81 cells)
        for r in range(9):
            for c in range(9):
                current_num = next(nums_iter)
                is_fixed = current_num != ""

                border_top = (
                    ft.BorderSide(1, ft.Colors.BLACK)
                    if r == 0
                    else ft.BorderSide(0, ft.Colors.TRANSPARENT)
                )
                border_left = (
                    ft.BorderSide(1, ft.Colors.BLACK)
                    if c == 0
                    else ft.BorderSide(0, ft.Colors.TRANSPARENT)
                )
                border_bottom = (
                    ft.BorderSide(3, ft.Colors.BLACK)
                    if r in [2, 5, 8]
                    else ft.BorderSide(1, ft.Colors.BLACK)
                )
                border_right = (
                    ft.BorderSide(3, ft.Colors.BLACK)
                    if c in [2, 5, 8]
                    else ft.BorderSide(1, ft.Colors.BLACK)
                )

                main_text = ft.Text(
                    current_num,
                    color=(
                        ft.Colors.BLACK if is_fixed else ft.Colors.BLUE_900
                    ),
                    weight=(
                        ft.FontWeight.BOLD if is_fixed else ft.FontWeight.NORMAL
                    ),
                    size=20,
                )

                note_grid = ft.GridView(
                    runs_count=3,
                    child_aspect_ratio=1.0,
                    spacing=0,
                    run_spacing=0,
                    expand=True,
                )

                cell_container = ft.Container(
                    content=ft.Stack(
                        controls=[
                            note_grid,
                            ft.Container(
                                content=main_text, alignment=ft.Alignment.CENTER
                            ),
                        ]
                    ),
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.GREY_200 if is_fixed else ft.Colors.WHITE,
                    border=ft.Border(
                        top=border_top,
                        bottom=border_bottom,
                        left=border_left,
                        right=border_right,
                    ),
                    on_click=square_clicked,
                    data={
                        "pos": (r, c),
                        "fixed": is_fixed,
                        "value": current_num,
                        "main_text": main_text,
                        "note_grid": note_grid,
                        "notes": {},
                    },
                )
                grid.controls.append(cell_container)

        # Build Keypad Controls
        row1_btns = [
            ft.Button(
                content=ft.Text(str(n), size=18, weight=ft.FontWeight.BOLD),
                width=45,
                height=45,
                data=n,
                on_click=number_button_clicked,
                style=ft.ButtonStyle(padding=0),
            )
            for n in range(1, 5)
        ]

        clear_btn = ft.Button(
            content=ft.Icon(ft.Icons.BACKSPACE_OUTLINED, size=18),
            width=45,
            height=45,
            on_click=clear_button_clicked,
            style=ft.ButtonStyle(padding=0),
        )

        row2_btns = [
            ft.Button(
                content=ft.Text(str(n), size=18, weight=ft.FontWeight.BOLD),
                width=45,
                height=45,
                data=n,
                on_click=number_button_clicked,
                style=ft.ButtonStyle(padding=0),
            )
            for n in range(5, 10)
        ]

        note_btn = ft.Button(
            content=ft.Icon(ft.Icons.EDIT_NOTE, size=22),
            width=45,
            height=45,
            on_click=toggle_note_mode,
            bgcolor=ft.Colors.WHITE,
            style=ft.ButtonStyle(padding=0),
        )

        controls_column = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=6,
                    controls=row1_btns + [clear_btn],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=6,
                    controls=row2_btns + [note_btn],
                ),
            ],
        )

        board_wrapper = ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
                controls=[grid, controls_column],
            ),
            animate_opacity=200,
        )

        # Centered Root Screen Layout
        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=15,
                controls=[header_row, board_wrapper],
            )
        )
        page.update()

    def Home():
        nonlocal selected_difficulty
        timer.is_running = False

        start_btn = ft.Button(
            content=ft.Text("Start", size=22, weight=ft.FontWeight.BOLD),
            on_click=Start,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            disabled=True,
            height=50,
            width=140,
        )

        def set_difficulty(e):
            nonlocal selected_difficulty
            selected_difficulty = e.control.data

            for btn in level_buttons:
                if btn.data == selected_difficulty:
                    btn.bgcolor = ft.Colors.AMBER_400
                    btn.color = ft.Colors.BLACK
                else:
                    btn.bgcolor = ft.Colors.WHITE
                    btn.color = ft.Colors.BLACK

            start_btn.disabled = False
            page.update()

        level_buttons = [
            ft.Button(
                content=ft.Text(lvl),
                data=lvl,
                on_click=set_difficulty,
                width=100,
                height=45,
                bgcolor=ft.Colors.WHITE,
                color=ft.Colors.BLACK,
            )
            for lvl in ["Easy", "Normal", "Hard"]
        ]

        page.clean()
        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=25,
                controls=[
                    ft.Text(
                        "SUDOKU",
                        size=36,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Select Difficulty:", size=18, color=ft.Colors.WHITE
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                        controls=level_buttons,
                    ),
                    start_btn,
                ],
            )
        )
        page.update()

    Home()


ft.run(main)