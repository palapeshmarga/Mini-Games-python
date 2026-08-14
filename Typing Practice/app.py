import flet as ft
import time
import threading
import os
import random

def load_text_from_file(difficulty: str) -> str:
    lines_list = []
    filename = f"{difficulty.lower()}.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            if lines not in lines_list:
                lines_list.append(lines)
                return random.choice(lines)
    
    defaults = {
        "Easy": "cat dog run sun sky blue fast tree book page jump",
        "Normal": "python programming makes building desktop applications fun and interactive",
        "Hard": "asynchronous event driven architectures require careful state handling"
    }
    return defaults.get(difficulty, defaults["Normal"])

def main(page: ft.Page):
    page.title = "TypeMaster - Speed & Accuracy"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 30
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    selected_difficulty = "Normal"
    target_text = ""
    had_error = []
    
    current_level = 1
    current_score = 0
    target_score = 100
    
    inactivity_timer = None
    is_test_active = False
    start_time = None

    def close_dialog_and_restart(e):
        inactivity_dialog.open = False
        page.update()
        reset_test()

    inactivity_dialog = ft.AlertDialog(
        title=ft.Text("Inactivity Timeout", color=ft.Colors.ORANGE_400, weight=ft.FontWeight.BOLD),
        content=ft.Text("It seems you weren't here, let's start over!"),
        actions=[
            ft.TextButton("Try Again", on_click=close_dialog_and_restart)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.dialog = inactivity_dialog

    level_label = ft.Text(f"Level {current_level}", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_400)
    score_label = ft.Text(f"Score: {current_score} / {target_score}", size=18, weight=ft.FontWeight.W_500)
    wpm_label = ft.Text("0 WPM", size=18, color=ft.Colors.GREEN_300)
    
    target_text_display = ft.Text(spans=[], size=22)
    typing_input = ft.TextField(
        hint_text="Type here...",
        autofocus=True,
        width=600,
        visible=False,
    )

    def reset_inactivity_timer():
        nonlocal inactivity_timer
        if inactivity_timer:
            inactivity_timer.cancel()
        
        if is_test_active:
            inactivity_timer = threading.Timer(5.0, trigger_inactivity_reset)
            inactivity_timer.start()

    def trigger_inactivity_reset():
        nonlocal is_test_active
        is_test_active = False
        inactivity_dialog.open = True
        page.update()

    def check_level_up(points_gained: int):
        nonlocal current_score, current_level, target_score
        current_score += points_gained
        
        while current_score >= target_score:
            current_level += 1
            if current_level == 2:
                target_score = 250
            else:
                target_score = int(target_score * 1.7)
                
        level_label.value = f"Level {current_level}"
        score_label.value = f"Score: {current_score} / {target_score}"

    def update_text_rendering(user_input: str):
        spans = []
        for i, char in enumerate(target_text):
            if i < len(user_input):
                typed_char = user_input[i]
                if typed_char == char:
                    if had_error[i]:
                        spans.append(ft.TextSpan(char, style=ft.TextStyle(color=ft.Colors.ORANGE_400, weight=ft.FontWeight.BOLD)))
                    else:
                        spans.append(ft.TextSpan(char, style=ft.TextStyle(color=ft.Colors.GREEN_400, weight=ft.FontWeight.BOLD)))
                else:
                    had_error[i] = True
                    spans.append(ft.TextSpan(
                        char, 
                        style=ft.TextStyle(
                            color=ft.Colors.RED_400, 
                            decoration=ft.TextDecoration.UNDERLINE, 
                            weight=ft.FontWeight.BOLD
                        )
                    ))
            else:
                spans.append(ft.TextSpan(char, style=ft.TextStyle(color=ft.Colors.GREY_600)))
        
        target_text_display.spans = spans

    def on_typing_change(e):
        nonlocal is_test_active, start_time
        user_input = e.control.value
        
        if not is_test_active and len(user_input) > 0:
            is_test_active = True
            start_time = time.time()

        reset_inactivity_timer()
        update_text_rendering(user_input)

        if start_time and len(user_input) > 0:
            elapsed_min = (time.time() - start_time) / 60.0
            if elapsed_min > 0:
                words_typed = len(user_input) / 5.0
                wpm = int(words_typed / elapsed_min)
                wpm_label.value = f"{wpm} WPM"

        if len(user_input) == len(target_text):
            if inactivity_timer:
                inactivity_timer.cancel()
            is_test_active = False
            
            correct_count = sum(1 for i, c in enumerate(user_input) if c == target_text[i] and not had_error[i])
            points = correct_count * 2
            check_level_up(points)
            reset_test()

        page.update()

    typing_input.on_change = on_typing_change

    def start_game(difficulty: str):
        nonlocal selected_difficulty
        selected_difficulty = difficulty
        difficulty_card.visible = False
        game_container.visible = True
        reset_test()

    def reset_test():
        nonlocal target_text, had_error, is_test_active, start_time
        if inactivity_timer:
            inactivity_timer.cancel()
        
        is_test_active = False
        start_time = None
        target_text = load_text_from_file(selected_difficulty)
        had_error = [False] * len(target_text)
        
        typing_input.value = ""
        typing_input.visible = True
        
        update_text_rendering("")
        page.update()

    difficulty_card = ft.Card(
        content=ft.Container(
            padding=30,
            content=ft.Column(
                [
                    ft.Text("Select Difficulty", size=26, weight=ft.FontWeight.BOLD),
                    ft.Text("Choose a level to load your practice text", color=ft.Colors.GREY_400),
                    ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                    ft.Row(
                        [
                            ft.Button("Easy", color=ft.Colors.GREEN_400, on_click=lambda e: start_game("Easy")),
                            ft.Button("Normal", color=ft.Colors.BLUE_400, on_click=lambda e: start_game("Normal")),
                            ft.Button("Hard", color=ft.Colors.RED_400, on_click=lambda e: start_game("Hard")),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True
            )
        )
    )

    game_container = ft.Column(
        [
            ft.Row([level_label, score_label, wpm_label], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=600),
            ft.Divider(height=30, color=ft.Colors.GREY_800),
            ft.Container(
                content=target_text_display,
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.SURFACE,
                width=600,
            ),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            typing_input,
            ft.Button("Change Difficulty", on_click=lambda e: show_difficulty_screen())
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False
    )

    def show_difficulty_screen():
        nonlocal is_test_active
        if inactivity_timer:
            inactivity_timer.cancel()
        is_test_active = False
        game_container.visible = False
        difficulty_card.visible = True
        page.update()

    page.add(difficulty_card, game_container)

ft.run(main)