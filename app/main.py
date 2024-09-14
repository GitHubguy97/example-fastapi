from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API !!!!"}










# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', 
#                                  password = 'Ludachris1997', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("The error was: ", error)
#         time.sleep(2)


# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts """)
#     posts = cursor.fetchall()
#     print(posts)
#     return {"data": posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#                    (post.title, post.content, post.published) )
#     new_post = cursor.fetchall()
#     conn.commit()
#     return {"data": new_post}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""SELECT * FROM posts WHERE id = (%s)""", ( str(id) ) )
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
#     print(post)
#     return {"post_detail": post}


# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute(""" DELETE FROM posts WHERE id = (%s) RETURNING * """, ( str(id) ))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if not deleted_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
#     print(deleted_post)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
#                    ( post.title, post.content, post.published, str(id) ))
    
#     updated_post = cursor.fetchone()

#     conn.commit()

#     if updated_post ==  None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")

#     return {"data": updated_post}