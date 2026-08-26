from flet import controls

from Tests import *
import flet as ft

background_color = "#2f1745"



def main(page: ft.Page):

    # ئامادەکردنی پەنجەرەی دەستپێک

    page.title = "Cross-Platform App"
    page.theme_mode = ft.ThemeMode.SYSTEM
    
    if page.web or page.platform in [ft.PagePlatform.WINDOWS, ft.PagePlatform.MACOS, ft.PagePlatform.LINUX]:
        page.window.width = 450
        page.window.height = 800
        page.window.resizable = True
        page.window.center()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = "#41215e"

    def Start(e):
        page.clean() 

        # ژمارەی نێو خانەکان
        nums_iter = iter(Nums)

        grid = ft.GridView(
            expand=False,
            runs_count=9,   
            child_aspect_ratio=1.0,  
            spacing=5,               
            run_spacing=5,
        )


        def square_clicked(e):
            clicked_number = e.control.content.value
            clicked_r, clicked_c = e.control.data # Get coordinates of the clicked square

            # For empty squares
            if clicked_number == "":
                for container in grid.controls:
                    container.bgcolor = ft.Colors.WHITE
                e.control.bgcolor = ft.Colors.WHITE_38
                page.update()
                return

            # Color logic
            for container in grid.controls:
                curr_r, curr_c = container.data # Get coordinates of the current loop square
                
                # Reset all to white first
                container.bgcolor = ft.Colors.WHITE
                
                # If the number matches the clicked number
                if container.content.value == clicked_number:
                    # Check if it's in the same row, same column, or same 3x3 block
                    same_row = (curr_r == clicked_r)
                    same_col = (curr_c == clicked_c)
                    same_block = (curr_r // 3 == clicked_r // 3) and (curr_c // 3 == clicked_c // 3)
                    
                    # Is this the exact square we just clicked?
                    is_self = (curr_r == clicked_r and curr_c == clicked_c)

                    if not is_self and (same_row or same_col or same_block):
                        # Conflict found! Make it red
                        container.bgcolor = ft.Colors.RED
                    else:
                        # No conflict (or it's the clicked square itself), highlight normally
                        container.bgcolor = ft.Colors.WHITE_38

            page.update()


        for r in range(9):
            for c in range(9):
                try:
                    current_num = next(nums_iter)
                except StopIteration:
                    break 

                # Determine custom borders for Sudoku grid lines
                # Outer bounds use a standard thin edge, inner 3x3 lines get thick edges
                border_top = ft.BorderSide(1, ft.Colors.BLACK) if r == 0 else ft.BorderSide(0, ft.Colors.TRANSPARENT)
                border_left = ft.BorderSide(1, ft.Colors.BLACK) if c == 0 else ft.BorderSide(0, ft.Colors.TRANSPARENT)
                
                # If it's the edge of a 3x3 block (index 2 or 5) or the outer frame (index 8), make it thick
                border_bottom = ft.BorderSide(4, ft.Colors.BLACK) if r in [2, 5, 8] else ft.BorderSide(1, ft.Colors.BLACK)
                border_right = ft.BorderSide(4, ft.Colors.BLACK) if c in [2, 5, 8] else ft.BorderSide(1, ft.Colors.BLACK)

                grid.controls.append(
                    ft.Container(
                        content=ft.Text(str(current_num), color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD, size=24),
                        alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.Border(
                            top=border_top,
                            bottom=border_bottom,
                            left=border_left,
                            right=border_right
                        ),
                        on_click=square_clicked,
                        data=(r, c)  # <--- Add this line to pass the coordinates
                    )
                )

        page.add(grid)
        page.update() 


    def Home():
        start_button = ft.ElevatedButton(
            content=ft.Text(
                "Start",
                size=25,
                weight=ft.FontWeight.BOLD,
            ),
            on_click=Start,  
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            height=80,
            width=150,
        )

        # Wrap the button inside a Container with margin or padding
        positioned_button = ft.Container(
            content=start_button,
            margin=ft.Padding.only(top=450, left=25), # Sets offset from top and left
        )
        
        page.add(positioned_button)

    Home()
 
ft.app(target=main)
