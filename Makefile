install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

lint:
	uv run ruff check brain_games

build:
	uv build

package-install:
	uv tool install ./dist/brain_games-0.1.0-py3-none-any.whl --force