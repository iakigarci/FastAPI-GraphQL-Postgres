from typing import Dict, Optional

from app.db.postgres import storage

async def get_blogs(
    skip: Optional[int] = 0, limit: Optional[int] = 100
) -> Optional[Dict]:
    query = blog.select(offset=skip, limit=limit)
    result = await database.fetch_all(query=query)
    return [dict(blog) for blog in result] if result else None