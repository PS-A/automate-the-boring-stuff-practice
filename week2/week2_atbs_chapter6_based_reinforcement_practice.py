# Flight Seat Map Viewer

# Defining function.
def seat_map_layout(seat_map):
    col_widths = [0] * len(seat_map)
    for i in range(len(seat_map)):
            col_widths[i] += max(len(item) for item in seat_map[i])
            print(i)

    for r in range(len(seat_map[0])):
        row = ""
        for c in range(len(seat_map)):
            row += seat_map[c][r].rjust(col_widths[c]) + " "
        print(row)

# Defining list and calling function.
seats = [
    ['1A', '1B', '1C'],
    ['2A', 'X',  '2C'],
    ['3A', '3B', 'X'],
    ['4A', '4B', '4C']
]

seat_map_layout(seats)