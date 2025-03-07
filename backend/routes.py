from fastapi import APIRouter
from ai_meal_planner import generate_meal_plan
from scraper import scrape_prices

router = APIRouter()

@router.post("/meal-plan")
async def create_meal_plan(diet: str, calories: int):
    return generate_meal_plan(diet, calories)

@router.get("/scrape-prices")
async def get_prices(item: str):
    return scrape_prices(item)
