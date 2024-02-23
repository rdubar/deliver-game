import math
import cairocffi as cairo

def draw_board(filename="game_board.png"):
    # A4 size in pixels at 300 DPI: 2480x3508 (scaled down to 1240x1754 for simplicity)
    WIDTH, HEIGHT = 1754, 1240
    # Creating the cairo surface and context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    
    # Fill background with white
    ctx.set_source_rgb(1, 1, 1)  # White
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.fill()

    # Setup for rounded rectangles
    outer_margin = 20  # Margin for the outer rectangle
    inner_margin = 200  # Distance between outer and inner rectangle
    corner_radius = 50

    # Outer rounded rectangle
    draw_rounded_rectangle(ctx, outer_margin, outer_margin, WIDTH - 2*outer_margin, HEIGHT - 2*outer_margin, corner_radius)
    
    # Inner rounded rectangle
    draw_rounded_rectangle(ctx, outer_margin + inner_margin, outer_margin + inner_margin, WIDTH - 2*(outer_margin + inner_margin), HEIGHT - 2*(outer_margin + inner_margin), corner_radius)

    # Draw divisions between the rectangles
    draw_divisions(ctx, outer_margin, inner_margin, corner_radius, WIDTH, HEIGHT)

    # Save the file
    surface.write_to_png(filename)

def draw_rounded_rectangle(ctx, x, y, width, height, corner_radius):
    ctx.set_source_rgb(0, 0, 0)  # Black color for the rectangles
    ctx.set_line_width(2)
    arc_to_bezier = 0.55228475
    c = corner_radius * arc_to_bezier
    
    ctx.new_path()
    ctx.move_to(x + corner_radius, y)
    ctx.rel_line_to(width - 2 * corner_radius, 0)
    ctx.rel_curve_to(c, 0, corner_radius, c - corner_radius, corner_radius, c)
    ctx.rel_line_to(0, height - 2 * corner_radius)
    ctx.rel_curve_to(0, c, c - corner_radius, corner_radius, -corner_radius, corner_radius)
    ctx.rel_line_to(-width + 2 * corner_radius, 0)
    ctx.rel_curve_to(-c, 0, -corner_radius, -c + corner_radius, -corner_radius, -c)
    ctx.rel_line_to(0, -height + 2 * corner_radius)
    ctx.rel_curve_to(0, -c, corner_radius - c, -corner_radius, corner_radius, -corner_radius)
    ctx.close_path()
    
    ctx.stroke()

def draw_divisions(ctx, outer_margin, inner_margin, corner_radius, WIDTH, HEIGHT):
    ctx.set_source_rgb(0, 0, 0)  # Black color for division lines
    ctx.set_line_width(1)

    # Calculate positions for divisions
    outer_rect_start_x, outer_rect_start_y = outer_margin, outer_margin
    outer_rect_end_x, outer_rect_end_y = WIDTH - outer_margin, HEIGHT - outer_margin
    inner_rect_start_x, inner_rect_start_y = outer_margin + inner_margin, outer_margin + inner_margin
    inner_rect_end_x, inner_rect_end_y = WIDTH - (outer_margin + inner_margin), HEIGHT - (outer_margin + inner_margin)

    # Total perimeter for divisions (approximation)
    perimeter = 2 * (WIDTH - 2*outer_margin + HEIGHT - 2*outer_margin) - 8 * corner_radius

    # Length allocated for each division
    division_length = perimeter / 64

    # Number of divisions on each side (approximation, adjusting for corners)
    divisions_per_side = int((WIDTH - 2 * outer_margin) / division_length / 2)

    # Horizontal divisions - top and bottom
    for i in range(1, divisions_per_side + 1):
        division_pos = outer_margin + i * (WIDTH - 2 * outer_margin) / (divisions_per_side + 1)
        # Top division
        ctx.move_to(division_pos, outer_rect_start_y)
        ctx.line_to(division_pos, inner_rect_start_y)
        ctx.stroke()
        # Bottom division
        ctx.move_to(division_pos, outer_rect_end_y)
        ctx.line_to(division_pos, inner_rect_end_y)
        ctx.stroke()

    # Vertical divisions - left and right, adjusted for corner radius
    divisions_per_vertical_side = int((HEIGHT - 2 * outer_margin - 2 * corner_radius) / division_length / 2)
    for i in range(1, divisions_per_vertical_side + 1):
        division_pos = outer_margin + corner_radius + i * (HEIGHT - 2 * (outer_margin + corner_radius)) / (divisions_per_vertical_side + 1)
        # Left division
        ctx.move_to(outer_rect_start_x, division_pos)
        ctx.line_to(inner_rect_start_x, division_pos)
        ctx.stroke()
        # Right division
        ctx.move_to(outer_rect_end_x, division_pos)
        ctx.line_to(inner_rect_end_x, division_pos)
        ctx.stroke()


# Drawing the board
draw_board()
