from pygame import Vector2


# based on http://clintbellanger.net/articles/isometric_math/
def to_isometric_position(orthographic_vector: Vector2, cell_size: Vector2) -> Vector2:
    x_position = (orthographic_vector.x - orthographic_vector.y) * (cell_size.x / 2)
    y_position = (orthographic_vector.x + orthographic_vector.y) * (cell_size.y / 2)

    return Vector2(x_position, y_position)


def isometric_offset(
    isometric_vector: Vector2, screen_dimensions: Vector2, cell_size: Vector2
) -> Vector2:
    x_offset = (screen_dimensions.x / 2) - isometric_vector.x - cell_size.x / 2
    y_offset = (screen_dimensions.y / 2) - isometric_vector.y - cell_size.x / 2
    return Vector2(x_offset, y_offset)
