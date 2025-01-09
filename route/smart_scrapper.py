from fastapi import APIRouter, HTTPException, Depends
from schema.user import User
from schema.smart_scrapper import HomePageScrapperIn, HomePageScrapperOut
from logic.auth import get_current_active_user
from logic.smart_scrapper import scrape_homepage, smart_openai_analyzer

router = APIRouter()


# Example items belonging to the current user
@router.post("/smart_scrapping/", response_model=HomePageScrapperOut)
async def scrape_home(
    data: HomePageScrapperIn, current_user: User = Depends(get_current_active_user)
):
    scrapped_content, code = scrape_homepage(url=data.url)

    # Validation for scrapped content
    if code == 200:
        if "need to enable javascript" in scrapped_content.lower():
            raise HTTPException(
                status_code=400, detail=f"Failed to extract data: {scrapped_content}"
            )

        return smart_openai_analyzer(
            content=scrapped_content,
            api_key=data.openai_key,
            model=data.model,
            structured_output=HomePageScrapperOut,
        )

    raise HTTPException(
        status_code=code, detail=f"Failed to extract data: {scrapped_content}"
    )
