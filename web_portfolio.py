
import math
import flet as ft
import time
import webbrowser
def main(page: ft.Page):
    global alto_pagina,ancho_pagina
    page.title = "Portfolio Nicolás Izquierdo"
    # page.scroll = "auto"
    page.padding = 0
    page.bgcolor = "#121212"  # Fondo negro oscuro
    
   
        
    def page_resize(e):
        global ancho_pagina,alto_pagina
        ancho_pagina = page.width
        alto_pagina = page.height
        
        # print(ancho_pagina)
        gradient_color_txt.begin=(0,int(ancho_pagina/2))
        gradient_color_txt.end=(ancho_pagina,int(ancho_pagina/2))
        page.update()
        
    def on_hover_update(e: ft.HoverEvent):
        global alto_pagina,ancho_pagina

        fondo_pagina.gradient.center.y=(2*((e.global_y/(alto_pagina))-0.5))
        fondo_pagina.gradient.center.x=(2*((e.global_x/(ancho_pagina))-0.5))

        fondo_pagina.update()
    page.on_resized = page_resize
    def pan_update(e: ft.DragUpdateEvent):
        pass
    

    def create_blurred_card(title: str, content: str):
        """Crea un recuadro con fondo transparente y efecto de blur."""
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=24, weight="bold", color="white"),
                    ft.Text(content, size=16, color="white"),
                ],
                spacing=10,
            ),
            bgcolor=ft.colors.with_opacity(0.2, "white"),  # Fondo semi-transparente
            border_radius=15,
            padding=20,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(blur_radius=20, spread_radius=5, color="rgba(255,255,255,0.1)"),
        )

    # Encabezado
    header = ft.Container(
        bgcolor=ft.colors.with_opacity(0.2,color=ft.colors.BLACK),
        # opacity=0.5,
        blur=5,
        border_radius=40,
        content=ft.Row(
            [
               
                # ft.Text("", size=15, weight="bold", color="white"),
                ft.Container(
                            alignment=ft.alignment.center_left,
                            content=ft.Text('Nicolás Izquierdo',color='white',size=15),
                            height=40,
                            padding=10,
                            expand=True,
                            on_click=lambda _: scroll_inicio(_)),
                ft.Row(

                    [
                        
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text('Sobre mí',color='white',size=15),
                            height=40,
                            padding=10,
                            expand=True,
                            on_click=lambda _: scroll_sobre_mi(_)),
                        
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text('Experiencia',color='white',size=15),
                            height=40,
                            padding=10,
                            expand=True,
                            on_click=lambda _: page.launch_url("#")
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text('Proyectos',color='white',size=15),
                            height=40,
                            padding=10,
                            expand=True,
                            on_click=lambda _: page.launch_url("https://github.com")
                        ),
                        # ft.TextButton("Estudios", on_click=lambda _: page.launch_url("#")),
                        # ft.TextButton("Experiencia", on_click=lambda _: page.launch_url("#")),
                        # ft.TextButton("Proyectos", on_click=lambda _: page.launch_url("https://github.com")),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=0,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        padding=ft.padding.symmetric(vertical=20, horizontal=30),
    )

    # Sección principal
    gradient_color_txt=ft.PaintLinearGradient(
                            # (17650, 16800), (17800, 16650), [ft.colors.RED, ft.colors.YELLOW]
                            # (600, 1200), (1900, 1200), ['#007f8a', '#b64f6d'],
                            # (0, 0.5), (1, 0.5), [ft.colors.RED, ft.colors.YELLOW],
                            (20, 300), (600, 300), [ '#803bff','#007f8a'],
                            
                            # (-0.8,0.2), (0.2,0.8), [ft.colors.RED, ft.colors.YELLOW]
                        
                        )
    def abrir_descarga(e):
        webbrowser.open("https://drive.google.com/file/d/1R1PzRddrdj3ZHG279sHbr9_CSEPJV3Qb/view?usp=sharing")

    def scroll_sobre_mi(e):
        page.controls[0].controls[0].scroll_to(offset=730,duration='1000')
        pass
    def scroll_inicio(e):
        page.controls[0].controls[0].scroll_to(offset=0,duration='1000')
        pass
    def cambiar_lado_seccion(e):
        if e.data=='true':
            for i in range(0,10,1):
                time.sleep(0.02)
                e.control.gradient=ft.LinearGradient(
                                            begin=ft.alignment.top_left,
                                            end=ft.alignment.bottom_right,
                                            colors=[
                                                '#007f8a','#803bff',
                                            ],
                                            tile_mode=ft.GradientTileMode.MIRROR,
                                            rotation= math.pi*i/10,)
                e.control.update()
        else:
            for i in range(10,0,-1):
                time.sleep(0.02)
                e.control.gradient=ft.LinearGradient(
                                            begin=ft.alignment.top_left,
                                            end=ft.alignment.bottom_right,
                                            colors=[
                                                '#007f8a','#803bff',
                                            ],
                                            tile_mode=ft.GradientTileMode.MIRROR,
                                            rotation= math.pi*i/10,)
                e.control.update()
        
        # page.update()
        # pass
    hero_section = ft.Container(
        # expand=True,
        # width=500,

        content=ft.Column(
            # expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,

            controls=[
                
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    # col={"sm": 4, "md": 4, "xl": 4},
                    # expand=True,
                    # width=500,
                    controls=[
                        ft.Container(
                                bgcolor='transparent',
                                width=500,
                                expand=1,
                                content=ft.Column(
                                    width=500,
                                    expand=1,
                                controls=[
                                    ft.Divider(height=70,color='transparent'),
                                    
                                    ft.Container(bgcolor="transparent",
                                                height=200,
                                                width=200,
                                                shape=ft.BoxShape.CIRCLE,
                                                alignment=ft.alignment.center,
                                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                                content=ft.Row(
                                                    expand=True,
                                                    controls=[
                                                ft.Image(src='/assets/1731888930625.png',fit=ft.ImageFit.FILL,expand=True)  
                                                ])),
                                    
                                    
                                    ft.Text(
                                        width=500,
                                        text_align=ft.TextAlign.CENTER,
                                        spans=[
                                            ft.TextSpan(
                                                "Hola soy ",
                                                ft.TextStyle(
                                                    size=40,
                                                    weight=ft.FontWeight.BOLD,
                                                    color='white'
                                                    
                                                ),
                                            ),
                                            
                                            ft.TextSpan(
                                                "Nicolás Izquierdo!",
                                                style=ft.TextStyle(
                                                    size=40,
                                                    weight=ft.FontWeight.BOLD,
                                                    foreground=ft.Paint(
                                                        gradient=gradient_color_txt
                                                        # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    ft.Divider(height=5,color='transparent'),
                                    ft.Row(
                                        width=500,
                                        expand=1,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                width=500,
                                                expand=1,
                                                content=ft.Text(
                                                    text_align=ft.TextAlign.CENTER,
                                                    spans=[
                                                        ft.TextSpan(
                                                            "Ingeniero Civil ",
                                                            style=ft.TextStyle(
                                                                size=18,
                                                                weight=ft.FontWeight.BOLD,
                                                                foreground=ft.Paint(
                                                                    gradient=gradient_color_txt
                                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                                ),
                                                            ),
                                                        ),
                                                        ft.TextSpan(
                                                            "y desarrollador de software en ",
                                                            ft.TextStyle(
                                                                size=18,
                                                                weight=ft.FontWeight.BOLD,
                                                                color='white'
                                                            ),
                                                        ),
                                                        ft.TextSpan(
                                                            "Python",
                                                            style=ft.TextStyle(
                                                                size=18,
                                                                weight=ft.FontWeight.BOLD,
                                                                foreground=ft.Paint(
                                                                    gradient=gradient_color_txt
                                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                                ),
                                                            ),
                                                        ),
                                                        ft.TextSpan(
                                                            ", apasionado por la porgramación y la tecnología.",
                                                            ft.TextStyle(
                                                                size=18,
                                                                weight=ft.FontWeight.BOLD,
                                                                color='white'
                                                            ),
                                                        ),
                                                    ],
                                                    # "Ingeniero Civil y desarrollador de software en Python, apasionado por la porgramación y la tecnología.",
                                                    # size=18,
                                                    # text_align="center",
                                                    # color="white",
                                                ),
                                            ),
                                            
                                        ]
                                    ),
                                    
                                    ft.Divider(height=5,color='transparent'),
                                    ft.Row(
                                        [
                                            ft.Container(
                                                width=140,
                                                height=40,
                                                border_radius=20,
                                                alignment=ft.alignment.center,
                                                on_hover=lambda _:cambiar_lado_seccion(_),
                                                on_click=lambda _: abrir_descarga(_),
                                                gradient=ft.LinearGradient(
                                                    begin=ft.alignment.top_left,
                                                    end=ft.alignment.bottom_right,
                                                    colors=[
                                                        '#803bff','#007f8a'
                                                    ],
                                                    tile_mode=ft.GradientTileMode.MIRROR,
                                                    rotation= 3,),
                                                content=ft.Text("Descargar CV",size=15,color='white',)
                                            ),
                                            ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Divider(height=85,color='transparent'),
                                    ft.Divider(height=40,color='transparent'),
                                    
                                    
                                    
                                ],
                                spacing=30,
                                horizontal_alignment="center",
                            ),
                        ),

                    ]
                ),
                ft.ResponsiveRow(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.MainAxisAlignment.START,
                        expand=True,
                        controls=[
                           
                            # ft.Container(
                            #     # width=200,
                            #     expand=True,
                            #     alignment=ft.alignment.center_left,
                            #     content=ft.Image('/assets/LEGO_logo.svg.png',expand=0,height=300,),
                               
                            # )

                            
                        ],
                        col={"sm": 6, "md": 0, "xl": 3},

                    ),
                    ft.Container(
                        width=500,
                        expand=1,
                        alignment=ft.alignment.center_right,
                        padding=10,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    spans=[
                                        ft.TextSpan(
                                            "Sobre mí",
                                            style=ft.TextStyle(
                                                size=40,
                                                weight=ft.FontWeight.BOLD,
                                                foreground=ft.Paint(
                                                    gradient=gradient_color_txt
                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                ),
                                            ),
                                        ),]),
                                ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    spans=[
                                        ft.TextSpan(
                                            "Me caracterizo por mi ",
                                            style=ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                color='white'
                                                # foreground=ft.Paint(
                                                #     gradient=gradient_color_txt
                                                #     # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                # ),
                                            ),
                                        ),
                                        
                                        ft.TextSpan(
                                            "organización, responsabilidad, creatividad",
                                            style=ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                foreground=ft.Paint(
                                                    gradient=gradient_color_txt
                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                ),
                                            ),
                                        ),
                                        ft.TextSpan(
                                            ", capacidad de adaptarme a diferentes",
                                            ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                color='white'
                                            ),),
                                        ft.TextSpan(
                                            " entornos y metodologías de trabajo.",
                                            style=ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                foreground=ft.Paint(
                                                    gradient=gradient_color_txt
                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                ),
                                            ),
                                        ),
                                        ft.TextSpan(
                                            " Proactivo y con facilidad para ",
                                            ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                color='white'
                                            ),
                                        ),
                                        ft.TextSpan(
                                            "trabajar en equipo.",
                                            style=ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                foreground=ft.Paint(
                                                    gradient=gradient_color_txt
                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                ),
                                            ),
                                        ),
                                        ft.TextSpan(
                                            " Experiencia en manejo de",
                                            ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                color='white'
                                            ),
                                        ),
                                        ft.TextSpan(
                                            " software para ingeniería",
                                            style=ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                foreground=ft.Paint(
                                                    gradient=gradient_color_txt
                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                ),
                                            ),
                                        ),
                                        ft.TextSpan(
                                            " y agilidad en el uso de varios",
                                            ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                color='white'
                                            ),
                                        ),
                                        ft.TextSpan(
                                            " lenguajes de programación",
                                            style=ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                foreground=ft.Paint(
                                                    gradient=gradient_color_txt
                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                ),
                                            ),
                                        ),
                                        ft.TextSpan(
                                            " con el fin de contribuir al desarrollo de ",
                                            ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                color='white'
                                            ),
                                        ),
                                        ft.TextSpan(
                                            "soluciones innovadoras",
                                            style=ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                foreground=ft.Paint(
                                                    gradient=gradient_color_txt
                                                    # gradient=ft.PaintLinearGradient(begin=ft.alignment.center_left,end=ft.alignment.center_right,colors=[ft.colors.RED, ft.colors.YELLOW])
                                                ),
                                            ),
                                        ),
                                        ft.TextSpan(
                                            " que mejoren la infraestructura y resuelvan desafíos complejos.",
                                            ft.TextStyle(
                                                size=18,
                                                weight=ft.FontWeight.NORMAL,
                                                color='white'
                                            ),
                                        ),
                                    ],
                                    # "Ingeniero Civil y desarrollador de software en Python, apasionado por la porgramación y la tecnología.",
                                    # size=18,
                                    # text_align="center",
                                    # color="white",
                                ),
            
                                
                            ]
                        ),
                        col={"sm": 6, "md": 6, "xl": 5},
                        # expand=True

                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                           
                            ft.Container(
                                # width=200,
                                expand=True,
                                alignment=ft.alignment.center,
                                content=ft.Image('/assets/LEGO_logo.svg.png',expand=0,height=300,),
                               
                            )

                            
                        ],
                        col={"sm": 6, "md": 6, "xl": 3},

                    ),
                    

                        
                    
                    

                ],
                run_spacing={"xs": 10}
                )
                      

                      ]
        ),
        

        
        padding=ft.padding.symmetric(vertical=60, horizontal=20),
        alignment=ft.alignment.center,
        bgcolor='transparent'
    )

    # Tarjetas con blur
    cards_section = ft.Container(
        content=ft.Row(
            scroll=True,

            controls=[
                create_blurred_card("Feature 1", "Description of feature 1."),
                create_blurred_card("Feature 2", "Description of feature 2."),
                create_blurred_card("Feature 3", "Description of feature 3."),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=ft.padding.symmetric(vertical=40, horizontal=20),
    )

    # Pie de página
    footer = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "Correo Electrónico: estebannizquierdoa10@gmail.com",
                            size=14,
                            color="white",
                            text_align="center",
                        ),

                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "Teléfono: +593 998236554",
                            size=14,
                            color="white",
                            text_align="center",
                        ),

                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "© 2024 Nicolás Izquierdo - Desarrollado con Flet Python.",
                            size=14,
                            color="white",
                            text_align="center",
                        ),

                    ]
                ),
                
                

            ]
        ),
        
        padding=ft.padding.symmetric(vertical=20, horizontal=30),
    )
    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.BASIC,
        drag_interval=10,
        on_hover=on_hover_update,
        
    )
    fondo_pagina=ft.Container(
        gd,
        expand=True,
        gradient=ft.RadialGradient(
                center=ft.alignment.center_right,
                radius=5,
                colors=[
                    ft.colors.GREY_900,  # yellow sun
                    "black",  # blue sky
                ],
                stops=[0, 2.0],
            ),

    )

    # Agregar todos los elementos a la página
    page.add(
        ft.Stack(
            
            controls=[
                fondo_pagina,
                
                
                ft.Column(
                    # expand=True,
                    controls=[
                        
                        hero_section,
                        cards_section,
                        footer,
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    
                    # auto_scroll=True
                ),
                ft.Container(
                    
                    padding=10,
                    bgcolor='transparent',
                    content=header,
                    
                    
                ),
                
                
            ],
            expand=True
        ),
        
        
        # cp,
        
    )
    page_resize(None)
    

ft.app(target=main,assets_dir='assets',view=ft.AppView.WEB_BROWSER)
