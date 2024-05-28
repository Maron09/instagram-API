from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware
from middleware import TimeoutMiddleware

# Import the functions from the other scripts
from profile_data import retrieve_profile_info
from user_post import retrieve_post_metrics
from media import get_post_details

app = FastAPI(middleware=[
    Middleware(TimeoutMiddleware, timeout=60)  # Set a global timeout of 15 seconds
])

@app.get('/v1/api/profile')
def profile_info(username: str = Query(..., description="Username of the profile to retrieve")):
    try:
        profile_data = retrieve_profile_info(username)
        if profile_data is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return JSONResponse(content=profile_data)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Still needs work
# @app.get('/v1/api/user_posts')
# def user_posts(username: str = Query(..., description="Username to retrieve posts for")):
#     try:
#         posts = retrieve_post_metrics(username)
#         if posts is None:
#             raise HTTPException(status_code=404, detail="Posts for user not found")
#         return JSONResponse(content=posts)
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



@app.get('/v1/api/media')
def media_posts(url: str = Query(..., description="URL of the media to retrieve details for")):
    try:
        media_url = get_post_details(url)
        if media_url is None:
            raise HTTPException(status_code=404, detail="Media Info not found")
        return JSONResponse(content=media_url)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
