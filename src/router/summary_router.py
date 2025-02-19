from fastapi import APIRouter, HTTPException, Depends
from Service.meeting_summary import MeetingSummarizer
from router.Schema.response import SummaryResponse

router = APIRouter()

def get_summarizer():
    return MeetingSummarizer()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_meeting(summarizer: MeetingSummarizer = Depends(get_summarizer)):
    try:
        summary = summarizer.summarize_meeting()
        return {"summary" : summary}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )