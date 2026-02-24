from fastapi import Query

def standard_query_param(
    limit: int = Query(10, ge=1, le=100, description="Max items")
):
    return {"limit": limit}