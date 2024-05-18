run:
	@poetry run uvicorn warframe_manager.app:app --reload

format:
	@poetry run black warframe_manager/ tests/
	@poetry run isort warframe_manager/ tests/


test:
	@poetry run pytest tests/ --cov 