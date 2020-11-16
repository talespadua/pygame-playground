import pytest
from pygame import Vector2
from game.math.isometric_calculator import to_isometric_position, isometric_offset


class TestToIsometricPosition:
    @pytest.fixture()
    def isometric_coordinates(
        self, orthogonal_coordinates: Vector2, tile_size: Vector2
    ) -> Vector2:
        return to_isometric_position(orthogonal_coordinates, tile_size)

    @pytest.mark.parametrize(
        "tile_size, orthogonal_coordinates, expected_coordinates",
        [
            (Vector2(64, 64), Vector2(0, 0), Vector2(0, 0)),
            (Vector2(64, 64), Vector2(2, 1), Vector2(32, 96)),
        ],
    )
    def test_orthogonal_translate_to_isometric(
        self,
        tile_size: Vector2,
        orthogonal_coordinates: Vector2,
        expected_coordinates: Vector2,
        isometric_coordinates: Vector2,
    ) -> None:
        assert isometric_coordinates == expected_coordinates


class TestIsometricOffset:
    @pytest.fixture()
    def isometric_coordinates(
        self, orthogonal_coordinates: Vector2, tile_size: Vector2
    ) -> Vector2:
        return to_isometric_position(orthogonal_coordinates, tile_size)

    @pytest.fixture()
    def offset(
        self,
        isometric_coordinates: Vector2,
        screen_dimensions: Vector2,
        tile_size: Vector2,
    ) -> Vector2:
        isometric_off = isometric_offset(
            isometric_coordinates, screen_dimensions, tile_size
        )
        return isometric_off

    @pytest.fixture()
    def centered_cell_position(
        self, isometric_coordinates: Vector2, offset: Vector2, tile_size: Vector2
    ) -> Vector2:
        x_position = isometric_coordinates.x + offset.x + tile_size.x / 2
        y_position = isometric_coordinates.y + offset.y + tile_size.y / 2
        return Vector2(x_position, y_position)

    @pytest.mark.parametrize(
        "tile_size, orthogonal_coordinates, screen_dimensions",
        [(Vector2(64, 64), Vector2(2, 2), Vector2(1024, 768))],
    )
    def test_isometric_offset(
        self,
        tile_size: Vector2,
        orthogonal_coordinates: Vector2,
        screen_dimensions: Vector2,
        isometric_coordinates: Vector2,
        centered_cell_position: Vector2,
        offset: Vector2,
    ) -> None:
        assert centered_cell_position.x == screen_dimensions.x / 2
        assert centered_cell_position.y == screen_dimensions.y / 2
